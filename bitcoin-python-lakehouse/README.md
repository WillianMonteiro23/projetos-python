# Bitcoin Data Pipeline

Este projeto implementa um **pipeline completo de Engenharia de Dados utilizando apenas Python**, executável **localmente** via **Jupyter Notebook (Anaconda)**.

O objetivo é demonstrar domínio de **ETL, consumo de APIs, modelagem de dados, formatos modernos (Parquet)** e **arquitetura de Data Lake / Lakehouse**, **sem dependência de ferramentas cloud ou engines distribuídas**.

---

## Objetivo do Projeto

- Extrair dados do preço do **Bitcoin** via API pública
- Converter valores de **USD para BRL**
- Persistir dados em múltiplos formatos (**JSON, CSV, Parquet**)
- Organizar dados seguindo **boas práticas de Data Lake**
- Realizar análises usando **SQL local (DuckDB)**
- Executar tudo **localmente**, de forma simples e reproduzível

---

## Tecnologias Utilizadas

- **Python 3.10+**
- **Anaconda**
- **Jupyter Notebook**
- **Pandas**
- **Requests**
- **PyArrow**
- **DuckDB**
- **APIs REST**
  - Coinbase (preço do Bitcoin)
  - CurrencyFreaks (USD para BRL)

---

## Arquitetura do Projeto (Local Lakehouse)

O projeto segue o conceito de **Lakehouse Architecture**, adaptado para execução local.

```text
bitcoin-python-lakehouse/
│
├── notebooks/
│   └── bitcoin_pipeline.ipynb
│
├── data/
│   ├── raw/
│   │   ├── json/
│   │   ├── csv/
│   │   └── parquet/
│   │
│   └── curated/
│       └── analytics.duckdb
│
├── requirements.txt
└── README.md



---

## Camadas de Dados

| Camada | Descrição |
|------|----------|
| **Raw** | Dados brutos extraídos diretamente das APIs |
| **Curated** | Dados organizados e prontos para análise |
| **Analytics** | Consultas SQL analíticas via DuckDB |

---

## Fluxo do Pipeline

1. **Extração**
   - Consulta à API da Coinbase para obter o preço spot do Bitcoin
   - Consulta à API CurrencyFreaks para taxa de câmbio USD → BRL

2. **Transformação**
   - Conversão do valor do Bitcoin de USD para BRL
   - Padronização dos campos
   - Inclusão de timestamp do evento

3. **Carga**
   - Persistência dos dados nos formatos:
     - **JSON** — dados brutos e legíveis
     - **CSV** — formato universal
     - **Parquet** — formato columnar otimizado

4. **Análise**
   - Leitura direta dos arquivos Parquet
   - Execução de consultas SQL usando DuckDB

---

## Modelo de Dados

| Coluna | Tipo | Descrição |
|------|------|----------|
| valor_usd | float | Preço do Bitcoin em USD |
| valor_brl | float | Preço do Bitcoin convertido para BRL |
| criptomoeda | string | Ativo negociado (BTC) |
| moeda_original | string | Moeda base retornada pela API |
| taxa_usd_brl | float | Taxa de conversão USD para BRL |
| timestamp | datetime | Data e hora da coleta |

---

## Persistência em múltiplos formatos estratégicos

Cada formato é usado com um **propósito específico**:

### JSON
- Rastreabilidade  
- Debug  
- Fidelidade ao dado original

### CSV
- Interoperabilidade  
- Uso rápido em ferramentas simples (Excel, Google Sheets)

### Parquet
- Formato columnar  
- Compactado  
- Leitura analítica rápida

---

## Valor Técnico

Esse projeto é muito valioso porque:

- Permite entender **arquitetura de pipelines profissionais** de forma **local e controlável**.
- Cobre todas as etapas de **engenharia de dados e analytics**, de forma prática.
- Ensina o uso de múltiplos formatos e bancos analíticos mesmo em **projetos pequenos**.