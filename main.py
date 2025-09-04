import os
import json
from datetime import datetime

from modules.funcs_auxiliares import (
    registrar_log,
    registrar_metrica,
    atualizar_heartbeat,
    garantir_diretorio,
    baixar_json_ipca,
    normalizar_json_ipca,
    salvar_resultados,
)

if __name__ == "__main__":
    # Pastas do projeto
    inicio = datetime.now()
    caminho_projeto = os.path.dirname(os.path.abspath(__file__))
    pasta_entrada  = os.path.join(caminho_projeto, "database", "in")
    pasta_saida    = os.path.join(caminho_projeto, "database", "out")
    pasta_logs     = os.path.join(caminho_projeto, "database", "log")
    garantir_diretorio(pasta_entrada); garantir_diretorio(pasta_saida); garantir_diretorio(pasta_logs)

    # Arquivos auxiliares
    arquivo_log = os.path.join(pasta_logs, datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss.log"))
    arquivo_hb  = os.path.join(pasta_logs, "heartbeat.txt")

    url_ipca = "https://sidra.ibge.gov.br/Ajax/JSon/Tabela/1/1737?versao=-1"

    try:
        registrar_log("Início do processo", arquivo_log)
        atualizar_heartbeat(arquivo_hb)

        # 1) Download sempre do zero 
        registrar_log("Etapa: download do JSON", arquivo_log)
        conteudo = baixar_json_ipca(url_ipca, arquivo_log, timeout=40)

        # Guardar o JSON bruto com timestamp (bom pra auditoria)
        caminho_json = os.path.join(pasta_entrada, f"ipca_bruto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(conteudo, f, ensure_ascii=False)

        # 2) Normalização
        registrar_log("Etapa: normalização", arquivo_log)
        df_ipca = normalizar_json_ipca(conteudo, arquivo_log)
        df_ipca.columns = [str(c).strip() for c in df_ipca.columns]

        # 3) Salvamento (Parquet/CSV)
        registrar_log("Etapa: salvamento", arquivo_log)
        caminhos = salvar_resultados(df_ipca, pasta_saida, nome_base="ipca", arquivo_log=arquivo_log)

        duracao = (datetime.now() - inicio).total_seconds()
        registrar_log(f"Processo concluído em {duracao:.2f}s", arquivo_log)
        registrar_metrica(os.path.join(pasta_logs, "metricas.csv"), "execucoes_ok", 1.0)

    except Exception as e:
        registrar_log(f"ERRO FATAL: {e}", arquivo_log, nivel="ERROR")
        registrar_metrica(os.path.join(pasta_logs, "metricas.csv"), "execucoes_falha", 1.0,
                          tags={"erro": str(e)[:180]})
        raise
