# ROBO-IPCA-PARQUET

## 📌 Descrição
Este projeto é um **robô em Python** que automatiza a coleta de dados do **IPCA** (Índice de Preços ao Consumidor Amplo) a partir do site do **SIDRA/IBGE**.  
O processo realiza as seguintes etapas:

1. Faz o download dos dados do IPCA em formato JSON.  
2. Normaliza o conteúdo para uma estrutura tabular (DataFrame).  
3. Salva os resultados em **Parquet** e **CSV**.  
4. Gera **logs** de execução e mantém métricas simples.  

---

## 📂 Estrutura do Projeto
```text
robo-ipca-parquet/
│
├── database/           # Dados usados e gerados pelo robô
│   ├── in/             # Entradas (JSON bruto)
│   │   └── .dir
│   ├── log/            # Logs
│   │   └── .dir
│   └── out/            # Resultados (CSV/Parquet)
│       └── .dir
│
├── modules/            # Funções auxiliares
│   └── funcs_auxiliares.py
│
├── main.py             # Script principal
├── requirements.txt    # Dependências
├── setup.bat           # Instalação (Windows)
├── setup.sh            # Instalação (Linux/Mac)
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Este arquivo

git clone https://github.com/marcioroliveira79/robo-ipca-parquet.git
cd robo-ipca-parquet
