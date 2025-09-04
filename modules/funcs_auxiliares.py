import os
import csv
import json
import time
import random
import requests
import pandas as pd
from datetime import datetime
from typing import Any, Dict, List, Optional

# =============================================================================
# LOGS, MÉTRICAS E HEARTBEAT
# =============================================================================

def registrar_log(mensagem: str, arquivo_log: str, nivel: str = "INFO", contexto: Optional[Dict[str, Any]] = None) -> None:
    """
    Escreve uma linha de log no console e em arquivo (formato JSON por linha).
    Assim dá pra filtrar depois por nível, timestamp, etc.
    """
    os.makedirs(os.path.dirname(arquivo_log), exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = {"ts": ts, "nivel": nivel, "mensagem": mensagem}
    if contexto:
        linha["contexto"] = contexto

    print(f"[{ts}] [{nivel}] {mensagem}" + (f" | {json.dumps(contexto, ensure_ascii=False)}" if contexto else ""))
    with open(arquivo_log, "a", encoding="utf-8") as f:
        f.write(json.dumps(linha, ensure_ascii=False) + "\n")


def registrar_metrica(caminho_csv: str, nome: str, valor: float, tags: Optional[Dict[str, str]] = None) -> None:
    """
    Registra métricas simples em CSV (timestamp, nome, valor e tags em JSON).
    Bom pra criar um gráfico depois ou acompanhar tendência de execução.
    """
    os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)
    linha = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome": nome,
        "valor": valor,
        "tags": json.dumps(tags or {}, ensure_ascii=False),
    }
    novo_arquivo = not os.path.exists(caminho_csv)
    with open(caminho_csv, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["timestamp", "nome", "valor", "tags"])
        if novo_arquivo:
            w.writeheader()
        w.writerow(linha)


def atualizar_heartbeat(caminho_arquivo: str) -> None:
    """
    Heartbeat (batimento): arquivo com o último horário em que o bot "pulsou".
    Serve pra um job externo checar se está tudo vivo e no ritmo.
    """
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(datetime.now().isoformat())

# =============================================================================
# UTILS DE PASTA E JSON
# =============================================================================

def garantir_diretorio(caminho: str) -> None:
    os.makedirs(caminho, exist_ok=True)


def encontrar_lista_dict(objeto: Any) -> Optional[List[dict]]:
    """
    Vasculha o JSON recursivamente até achar uma lista de dicionários,
    que é a forma ideal de virar DataFrame.
    """
    if isinstance(objeto, list):
        if objeto and all(isinstance(x, dict) for x in objeto):
            return objeto
        for elemento in objeto:
            achou = encontrar_lista_dict(elemento)
            if achou is not None:
                return achou
    elif isinstance(objeto, dict):
        for _, valor in objeto.items():
            achou = encontrar_lista_dict(valor)
            if achou is not None:
                return achou
    return None

# =============================================================================
# PIPE DE DADOS: DOWNLOAD, NORMALIZAÇÃO, SALVAMENTO
# =============================================================================

def baixar_json_ipca(url: str, arquivo_log: str, timeout: int = 30,
                     tentativas: int = 3, espera_inicial: float = 1.5, multiplicador: float = 2.0,
                     espera_max: float = 20.0) -> dict:
    """
    Faz o download do JSON do SIDRA/IBGE com retry simples embutido.
    Backoff = a cada falha, espera um pouco mais antes de tentar de novo.
    Jitter = adiciona um "randômico" na espera pra evitar efeito manada.
    (Não usa decorator; tudo aqui dentro pra ficar explícito.)
    """
    cabecalhos = {
        "User-Agent": "Mozilla/5.0 (compatible; IPCA-Bot/1.0)",
        "Accept": "application/json, text/plain, */*",
    }
    espera = espera_inicial
    ultimo_erro = None

    for tentativa in range(1, tentativas + 1):
        try:
            registrar_log(f"Baixando dados do SIDRA (tentativa {tentativa}/{tentativas})...", arquivo_log,
                          nivel="DEBUG", contexto={"url": url})
            resp = requests.get(url, headers=cabecalhos, timeout=timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            ultimo_erro = e
            registrar_log(f"Falha no download: {e}", arquivo_log, nivel="WARN")
            if tentativa < tentativas:
                jitter = espera * random.uniform(0.0, 0.3)
                pausa = min(espera_max, espera + jitter)
                registrar_log(f"Aguardando {pausa:.1f}s para nova tentativa...", arquivo_log, nivel="DEBUG")
                time.sleep(pausa)
                espera = min(espera_max, espera * multiplicador)

    # se chegou aqui, esgotou as tentativas
    raise RuntimeError(f"Não foi possível baixar o JSON após {tentativas} tentativas: {ultimo_erro}")


def normalizar_json_ipca(conteudo: dict, arquivo_log: str) -> pd.DataFrame:
    """
    Converte o JSON em DataFrame:
    1) tenta achar uma lista de dicionários e cria o DF
    2) se não achar, usa json_normalize como fallback
    """
    registros = encontrar_lista_dict(conteudo)
    if registros:
        df = pd.DataFrame(registros)
        if not df.empty:
            registrar_log("Normalização concluída (lista de dicionários).", arquivo_log,
                          contexto={"linhas": len(df)})
            return df

    registrar_log("Usando fallback: json_normalize.", arquivo_log, nivel="WARN")
    df = pd.json_normalize(conteudo, max_level=2)
    if df.empty:
        raise ValueError("Não foi possível transformar o JSON em tabela.")
    registrar_log("Normalização concluída (json_normalize).", arquivo_log,
                  contexto={"linhas": len(df)})
    return df


def salvar_resultados(df: pd.DataFrame, pasta_saida: str, nome_base: str, arquivo_log: str) -> Dict[str, str]:
    """
    Salva o DataFrame em Parquet e CSV.
    Os nomes dos arquivos possuem timestamp: dd-mm-aaaa-hh-mm (pra saber quando foram gerados).
    """
    garantir_diretorio(pasta_saida)
    timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M")
    caminho_parquet = os.path.join(pasta_saida, f"{nome_base}_{timestamp}.parquet")
    caminho_csv     = os.path.join(pasta_saida, f"{nome_base}_{timestamp}.csv")

    df.to_parquet(caminho_parquet, index=False)
    df.to_csv(caminho_csv, index=False, encoding="utf-8")

    registrar_log("Arquivos salvos.", arquivo_log, contexto={"parquet": caminho_parquet, "csv": caminho_csv})
    registrar_metrica(os.path.join(os.path.dirname(arquivo_log), "metricas.csv"),
                      "linhas_salvas", float(len(df)), tags={"nome_base": nome_base, "timestamp": timestamp})
    return {"parquet": caminho_parquet, "csv": caminho_csv}
