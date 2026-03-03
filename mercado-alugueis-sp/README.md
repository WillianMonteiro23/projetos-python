# Análise do Mercado de Aluguéis em São Paulo (2023)

## Sobre o Dataset

Este projeto utiliza o conjunto de dados disponível no Kaggle:  
https://www.kaggle.com/datasets/renatosn/sao-paulo-housing-prices  

O dataset contém informações sobre imóveis para aluguel na cidade de São Paulo, Brasil. Os dados foram extraídos da plataforma **QuintoAndar** por meio de técnicas de **web scraping** em **1º de maio de 2023**.

O conjunto contempla mais de **11 mil imóveis** distribuídos em **8 colunas**:

- `address` — Endereço do imóvel  
- `district` — Bairro  
- `area` — Área em metros quadrados (m²)  
- `bedrooms` — Número de quartos  
- `garage` — Número de vagas de garagem  
- `type` — Tipo do imóvel  
- `rent` — Valor do aluguel mensal  
- `total` — Custo total do imóvel  

**Importante:** Como os dados foram obtidos via web scraping, podem conter inconsistências, valores ausentes ou erros de registro. Em um cenário de produção, seria essencial validar a origem e o processo de coleta dos dados antes de qualquer aplicação analítica ou modelagem preditiva.

Mesmo com essas ressalvas, o dataset é extremamente valioso para análises do mercado imobiliário e para compreensão da desigualdade urbana na cidade de São Paulo.

---

# Objetivo do Projeto

O principal objetivo deste projeto é:

- Aplicar **Python** na resolução de um problema real.
- Explorar o mercado imobiliário de São Paulo sob uma perspectiva analítica.
- Entender a desigualdade urbana através da precificação dos imóveis.
- Investigar relações entre variáveis como área, número de quartos, garagem e localização.
- Identificar padrões de valorização em bairros nobres versus bairros populares.
- Avaliar quais fatores mais influenciam o valor total do imóvel.

Este projeto vai além de uma simples análise descritiva — ele busca transformar dados brutos em **insights estratégicos sobre estrutura urbana e desigualdade social**.

---

# 1. Análise Exploratória (EDA)

Antes de realizar qualquer inferência, foi necessário compreender profundamente o conjunto de dados.

## 1.1 Visão Geral do Dataset

Inicialmente, realizamos:

- Visualização das primeiras linhas
- Verificação das colunas existentes
- Tipos de dados
- Identificação de valores faltantes

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/mercado-alugueis-sp/images/df_head.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/mercado-alugueis-sp/images/df_tail.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/df_info.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/df_columns_linhas.png" width="50%"/>
</div>

---

## 1.2 Estatísticas Descritivas

Após transformar os dados em um DataFrame utilizando `pandas`, aplicamos o método `describe()` para entender o comportamento das variáveis numéricas.

Principais observações:

- O desvio padrão do `rent` é **2650.71**
- O desvio padrão do `total` é **3352.48**
- Valor mínimo de aluguel: **R$500**
- Valor máximo de aluguel: **R$25.000**
- Mediana do aluguel: **R$2415**
- Dados com maior composição de apartamentos

Essa grande dispersão indica **alta desigualdade dentro do mercado imobiliário paulista**.

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/df_describe_numeric.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/df_describe_objetc.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/imoveis_por_categoria.png" width="50%"/>
</div>

---

## 1.3 Boxplot — Visualização da Dispersão

O boxplot evidenciou:

- Forte concentração próxima à mediana
- Grande quantidade de **outliers**
- Extrema variação nos valores de aluguel

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/distribuicao_alugueis.png" width="50%"/>
</div>

---

## 1.4 Histograma — Distribuição

O histograma revelou uma **distribuição assimétrica com cauda longa à direita**, indicando presença de imóveis com valores muito acima da média.

Isso reforça a desigualdade presente na cidade.

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/histograma_valores_aluguel.png" width="50%"/>
</div>

---

# 2. Análise das Variáveis Categóricas

Ao analisar as variáveis categóricas:

- **61,7% dos imóveis são apartamentos**
- Resultado esperado, considerando a verticalização da cidade

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/distribuicao_quantidade_quartos.png" width="50%"/>
</div>

---

# 3. Características Estruturais

### 🛏️ Quartos
- Maioria entre **1 e 3 quartos**

### 🚗 Garagens
- Maioria entre **0 e 2 vagas**

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/distribuicao_quantidade_garagens.png" width="50%"/>
</div>

---

# 4. Tratamento de Dados

Durante a análise da variável `area`, identificamos imóveis com **0m²**, o que é impossível.

Em um ambiente corporativo, o ideal seria:
- Investigar o processo de coleta
- Validar a origem do erro
- Corrigir na fonte

Como não tínhamos essa possibilidade, adotamos o critério:

> Remover imóveis com área inferior a 10m².

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/describe_area_outlier.png" width="50%"/>
</div>

---

# 5. Análise Comparativa — Luxo vs Popular

Após entender os dados, partimos para uma análise comparativa.

A premissa:

> Bairros mais caros tendem a refletir maior poder aquisitivo e melhores condições estruturais.

## Estratégia

1. Selecionamos os **50 bairros mais caros**
2. Selecionamos os **50 bairros mais baratos**
3. Criamos dois datasets:
   - `top50_imoveis`
   - `bottom50_imoveis`
4. Identificamos os bairros predominantes
5. Criamos novos DataFrames:
   - `top_imoveis`
   - `bottom_imoveis`
6. Criamos a coluna `categoria_imovel`:
   - "Luxo"
   - "Popular"

> O bairro **Alphaville** foi removido da análise de luxo por concentrar 4 dos 10 bairros mais caros, o que nos tirava a oportunidade de explorar demais bairros.

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/top_10_alphaville.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/top_10_sem_alphaville.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/topdescribe.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/bottomdescribe.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/plot_aluguel_imoveis_categoria.png" width="50%"/>
</div>

---

## 5.1 Comparação de Aluguel por Categoria

O boxplot mostrou uma diferença brutal entre as categorias.

- Valorização superior a **10x**
- Diferença extremamente significativa

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/aluguel_por_tipo_por_categoria.png" width="50%"/>
</div>

---

## 5.2 Tipo de Imóvel e Valorização

Observação interessante:

- Casas, apartamentos e condomínios: valorização até **1000%**
- Studios e kitnets: valorização limitada a cerca de **400%**

Isso ocorre porque studios possuem limitação estrutural de área.

---

## 5.3 Área dos Imóveis(m²)

Ao comparar áreas:

- Studios de luxo e populares possuem áreas semelhantes.
- Casas e condomínios apresentam grande variação de área.
- Maior área tende a elevar o valor final.

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/area_por_tipo_por_categoria.png" width="50%"/>
</div>

---

## 5.4 Quartos e Garagem

### Luxo:
- 1 a 6 quartos
- Até 6 vagas de garagem
- Concentração em 3 quartos

### Popular:
- 1 ou 2 quartos
- 0 ou 1 vaga

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/quarto_categoria.png" width="50%"/>
</div>

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/garage_categoria.png" width="50%"/>
</div>

---

# 6. Correlação Entre Variáveis

Utilizamos as variáveis:

- `bedrooms`
- `garage`
- `rent`
- `area`
- `total`

O heatmap revelou:

- `rent` é a variável mais influente no `total`
- `area` tem forte correlação
- `garage` tem influência moderada
- `bedrooms` apresenta correlação moderada
- Área influencia indiretamente garagem

<div align='center'>
  <img src="https://github.com/WillianMonteiro23/projetos-python/blob/main/mercado-alugueis-sp/images/heatmap_corr.png" width="50%"/>
</div>

---

# Conclusão

Nossa análise expôs evidências claras sobre o mercado imobiliário paulistano e, principalmente, sobre como a **desigualdade social** se manifesta nos detalhes.

## Principais Insights

### 🏆 1. Concentração de Riqueza
- Alphaville lidera os valores mais altos.
- Zona Sul concentra a maioria dos bairros valorizados.
- Zona Norte não aparece entre os 10 mais caros.

### 🏚️ 2. Regiões Mais Baratas
- Zona Leste e Zona Sul aparecem empatadas entre as mais baratas.
- A presença da Zona Sul nos dois extremos evidencia desigualdade espacial.

### 📊 3. Limite Estrutural de Valorização
- Casas: diferença pode chegar a 1000%.
- Studios: diferença limitada a ~400%.
- A área física impõe um teto de valorização.

### 🚗 4. Estrutura Como Diferencial
- Imóveis populares raramente possuem garagem.
- Imóveis de luxo chegam a 6 vagas.
- Número de quartos e vagas são fortes indicadores de poder aquisitivo.

### 📈 5. Variáveis Preditoras
- Área, quartos e garagem possuem correlação significativa com o valor total.
- Características estruturais são bons preditores do preço.

---

# Considerações Finais

Este projeto demonstra:

- Aplicação prática de Python em análise de dados reais.
- Importância da análise exploratória antes de qualquer modelagem.
- Como dados podem revelar padrões sociais invisíveis.
- A relevância da análise imobiliária como ferramenta de leitura urbana.

Mais do que números, este estudo revela a estrutura social refletida nos preços.

---

📌 Projeto desenvolvido para portfólio com foco em Análise de Dados, exploração estatística e geração de insights estratégicos.


