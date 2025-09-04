# ROBO-IPCA-PARQUET

Este projeto é um **robô em Python** que automatiza a coleta de dados do **IPCA** (Índice de Preços ao Consumidor Amplo) a partir do site do **SIDRA/IBGE**.  
O processo realiza as seguintes etapas:

1. Faz o download dos dados do IPCA em formato JSON.  
2. Normaliza o conteúdo para uma estrutura tabular (DataFrame).  
3. Salva os resultados em **Parquet** e **CSV**.  
4. Gera **logs** de execução e mantém métricas simples.  

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

- **Python 3.9+** ou superior.
- **Git** para clonar o repositório.


### 🔧 Instalação

Clonar o repositório

```
git clone https://github.com/marcioroliveira79/robo-ipca-parquet.git
```

```
cd robo-ipca-parquet
```
No Windows

```
setup.bat
```
No Linux
```
chmod +x setup.sh
./setup.sh
```

## ▶️ Execução

Se sua .venv não estiver ativada
Windows
```
.venv\Scripts\activate.bat
```
Linux
```
source .venv/bin/activate
```
Executar
```
python main.py
```

### 📊 Resultados

- Saída (resultados): database/out/
- Arquivos .csv e .parquet com timestamp no nome (ex.: ipca_04-09-2025-15-42.csv).
- Logs: database/log/
- Arquivos .log contendo os detalhes de cada execução.
- Entradas brutas: database/in/
- O JSON baixado diretamente do SIDRA/IBGE, salvo com timestamp.

## 📄 Exmplos de saídas

- database/out/ipca_04-09-2025-15-42.csv
- database/out/ipca_04-09-2025-15-42.parquet
- database/log/2025-09-04_15h42m10s.log
- database/in/ipca_bruto_20250904_154210.json

## 🛠️ Construído com

* [Visual Studio Code](https://code.visualstudio.com/) - Editor de código usado
* [Python](https://www.python.org/) - Linguagem de programação utilizada
