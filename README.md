# ROBO-IPCA-PARQUET

## 📌 Descrição
Este projeto é um **robô em Python** que automatiza a coleta de dados do **IPCA** (Índice de Preços ao Consumidor Amplo) a partir do site do **SIDRA/IBGE**.  
O processo realiza as seguintes etapas:

1. Faz o download dos dados do IPCA em formato JSON.  
2. Normaliza o conteúdo para uma estrutura tabular (DataFrame).  
3. Salva os resultados em **Parquet** (formato otimizado para análise) e **CSV**.  
4. Gera **logs** de execução e mantém métricas simples de processamento.  

---
<img width="251" height="235" alt="image" src="https://github.com/user-attachments/assets/23ea5d6c-87db-4b5f-ac7d-e117a8ae3231" />


Observação: os arquivos `.dir` servem apenas para manter as pastas no Git, já que o Git não versiona diretórios vazios.

---

instalacao_execucao:
  passo_1: # Clonar o repositório
    - comando: git clone https://github.com/marcioroliveira79/robo-ipca-parquet.git
    - comando: cd robo-ipca-parquet

  passo_2: # Criar ambiente virtual
    windows:
      - comando: setup.bat
    linux_mac:
      - comando: chmod +x setup.sh
      - comando: ./setup.sh

  passo_3: # Executar o robô
    - comando: python main.py

resultados:
  saida: "database/out/"
  exemplos_csv_parquet:
    - "ipca_04-09-2025-15-42.csv"
    - "ipca_04-09-2025-15-42.parquet"
  logs: "database/log/"
  exemplos_logs:
    - "2025-09-04_15h42m10s.log"
  entradas: "database/in/"
  exemplos_json:
    - "ipca_bruto_20250904_154210.json"

