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

Iremos clonar o repositório

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

### 🔩 Analise os testes de ponta a ponta

Explique que eles verificam esses testes e porquê.

```
Dar exemplos
```
### 📊 Resultados

- Saída (resultados): database/out/
- Arquivos .csv e .parquet com timestamp no nome (ex.: ipca_04-09-2025-15-42.csv).
- Logs: database/log/
- Arquivos .log contendo os detalhes de cada execução.
- Entradas brutas: database/in/
- O JSON baixado diretamente do SIDRA/IBGE, salvo com timestamp.

```
Dar exemplos
```

## 📦 Implantação

Adicione notas adicionais sobre como implantar isso em um sistema ativo

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - O framework web usado
* [Maven](https://maven.apache.org/) - Gerente de Dependência
* [ROME](https://rometools.github.io/rome/) - Usada para gerar RSS

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Um desenvolvedor** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;
* etc.


---
⌨️ com ❤️ por [Armstrong Lohãns](https://gist.github.com/lohhans) 😊
