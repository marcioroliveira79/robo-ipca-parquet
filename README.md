# ROBO-IPCA-PARQUET

## 📌 Descrição
Este projeto é um **robô em Python** que automatiza a coleta de dados do **IPCA** (Índice de Preços ao Consumidor Amplo) a partir do site do **SIDRA/IBGE**.  
O processo realiza as seguintes etapas:

1. Faz o download dos dados do IPCA em formato JSON.  
2. Normaliza o conteúdo para uma estrutura tabular (DataFrame).  
3. Salva os resultados em **Parquet** e **CSV**.  
4. Gera **logs** de execução e mantém métricas simples.  

---

## 📂 Estrutura do Projeto e Instalação/Execução
```text
robo-ipca-parquet/
│
├── database/
│   ├── in/      # Entradas (JSON bruto)
│   ├── log/     # Logs
│   └── out/     # Resultados (CSV/Parquet)
│
├── modules/     # Funções auxiliares
├── main.py      # Script principal
├── requirements.txt
├── setup.bat    # Instalação (Windows)
├── setup.sh     # Instalação (Linux/Mac)
├── .gitignore
└── README.md

🔹 Clonar o repositório
git clone https://github.com/marcioroliveira79/robo-ipca-parquet.git
cd robo-ipca-parquet

📦 Criar ambiente virtual no Windows
setup.bat 

🐧 Criar ambiente virtual no Linux/Mac
chmod +x setup.sh
./setup.sh

▶️ Executar o robô
python main.py

📊 Resultados
database/out/   -> Saída (CSV e Parquet, com timestamp no nome)
database/log/   -> Logs (.log)
database/in/    -> JSON bruto baixado do SIDRA/IBGE

📄 Exemplos de saída
database/out/ipca_04-09-2025-15-42.csv
database/out/ipca_04-09-2025-15-42.parquet
database/log/2025-09-04_15h42m10s.log
database/in/ipca_bruto_20250904_154210.json
