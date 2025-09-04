# ROBO-IPCA-PARQUET

## 📌 Descrição
Este projeto é um **robô em Python** que automatiza a coleta de dados do **IPCA** (Índice de Preços ao Consumidor Amplo) a partir do site do **SIDRA/IBGE**.  
O processo realiza as seguintes etapas:

1. Faz o download dos dados do IPCA em formato JSON.  
2. Normaliza o conteúdo para uma estrutura tabular (DataFrame).  
3. Salva os resultados em **Parquet** (formato otimizado para análise) e **CSV**.  
4. Gera **logs** de execução e mantém métricas simples de processamento.  

---

## 📂 Estrutura do Projeto
robo-ipca-parquet/
│
├── database/ # Base de dados local usada pelo robô
│ ├── in/ # Arquivos de entrada (JSON bruto baixado)
│ │ └── .dir
│ ├── log/ # Arquivos de log gerados durante execução
│ │ └── .dir
│ └── out/ # Arquivos de saída (CSV/Parquet)
│ └── .dir
│
├── modules/ # Módulos auxiliares em Python
│ └── funcs_auxiliares.py
│
├── main.py # Script principal do robô (orquestra todo o processo)
│
├── requirements.txt # Dependências do projeto
│
├── setup.bat # Script de instalação (Windows)
├── setup.sh # Script de instalação (Linux/Mac)
│
├── .gitignore # Ignora arquivos gerados automaticamente
└── README.md # Este arquivo


Observação: os arquivos `.dir` servem apenas para manter as pastas no Git, já que o Git não versiona diretórios vazios.

---

## ⚙️ Instalação

### Pré-requisitos
- **Python 3.9+** ou superior
- **Git** para clonar o repositório.

### Passo 1: Clonar o repositório
```bash
git clone https://github.com/marcioroliveira79/robo-ipca-parquet.git
cd robo-ipca-parquet

### Criar ambiente no Windows
setup.bat

### Criar ambiente no Linux
chmod +x setup.sh
./setup.sh

#### ▶️ Execução
python main.py

##### 📊 Resultados

Saída (resultados): database/out/
Arquivos .csv e .parquet com timestamp no nome (ex.: ipca_04-09-2025-15-42.csv).
Logs: database/log/
Arquivos .log contendo os detalhes de cada execução.
Entradas brutas: database/in/
O JSON baixado diretamente do SIDRA/IBGE, salvo com timestamp.

###### 📄 Exemplos de saída

database/out/ipca_04-09-2025-15-42.csv
database/out/ipca_04-09-2025-15-42.parquet
database/log/2025-09-04_15h42m10s.log
database/in/ipca_bruto_20250904_154210.json

