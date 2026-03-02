# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# %%
df = pd.read_csv('data.csv')

# %%
df.head()

# %%
df.tail()

# %%
df.info()

# %%
df.columns

# %%
f'O data_set tem {df.shape[0]} linnhas e {df.shape[1]} colunas'

# %%
df.describe()

# %%
df.describe(include='object')

# %%
# A média de uma série booleana representa a proporção de valores True
# (True = 1, False = 0), ou seja, a porcentagem de apartamentos
perc_aptos_df = (df['type'].eq('Apartamento').mean()) * 100
print(f'{perc_aptos_df:.2f}% do data_set analisado é composto por apartamentos')

# %%
total_imoveis = df.groupby('type')['rent'].count().sort_values(ascending=False)
percentual = (total_imoveis / total_imoveis.sum()) * 100

plt.figure(figsize=(10, 6))
bars = plt.bar(total_imoveis.index, total_imoveis.values, color='skyblue', edgecolor='black')

# Adicionar rótulos de percentual em cima de cada barra
for bar, pct in zip(bars, percentual):
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,  # posição X central da barra
        height,                          # posição Y no topo da barra
        f'{pct:.1f}%',                   # texto do percentual
        ha='center', va='bottom'         # alinhamento horizontal/vertical
    )

plt.title('Total de Imóveis por Categoria')
plt.xlabel('Categoria')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %%
mediana = np.median(df['rent'])
plt.figure(figsize=(10, 6))          # Tamanho do gráfico
plt.boxplot(df['rent'], vert=True, medianprops=dict(color='red', linewidth=2))   # vert=True = vertical
plt.title('Distribuição dos Aluguéis')  # Título do gráfico
plt.ylabel('Valor do Aluguel')         # Label do eixo Y
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # grade horizontal
plt.text(
    1.05,                 # posição no eixo X (um pouco à direita da caixa)
    mediana,              # posição no eixo Y (valor da mediana)
    f'Mediana: {mediana:.2f}',
    color='red',
    verticalalignment='center'
)

plt.show()

# %%
plt.figure(figsize=(10, 6))

# Histograma
plt.hist(df['rent'], bins=30, color='skyblue', edgecolor='black')

# Calcular mediana
mediana = np.median(df['rent'])

# Linha vertical da mediana
plt.axvline(mediana, color='red', linestyle='--', linewidth=2, 
            label=f'Mediana: {mediana:.2f}')

# Títulos e rótulos
plt.title('Distribuição dos Valores de Aluguel')
plt.xlabel('Valor do Aluguel')
plt.ylabel('Quantidade de Imóveis')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

plt.show()

# %%
total_quartos = df['bedrooms'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(total_quartos.index, total_quartos.values, color='skyblue', edgecolor='black')
plt.title('Distribuição da Quantidade de Quartos')
plt.xlabel('Quantidade de Quartos')
plt.ylabel('Quantidade de Imóveis')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %%
total_garagens = df['garage'].value_counts().sort_index()

plt.figure(figsize=(10,6))
plt.bar(total_garagens.index, total_garagens.values, color='skyblue', edgecolor='black')
plt.title('Distribuição da Quantidade de Garagens')
plt.xlabel('Quantidade de Garagens')
plt.ylabel('Quantidade de Imóveis')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# %%
df['area'].describe()

# %%
# É possivel ver que tem imoveis com 0m quadrados
# isso nao existe, poderiamos tratar isso
df = df.loc[df['area'] > 10]

# %%
top50_districts = (
    df.groupby('district', as_index=False)
        .agg(preco_medio=('rent', 'mean'))
        .sort_values(by='preco_medio', ascending=False)
        .head(50)
)


# Alphaville contem 3 dos 5 mais caros na media de valor de aluguel mensal, é nitido que é um lugar com custo elevado
# vamos excluir da analise para observar outros locais
top50_districts = (
    df[~df['district'].str.contains('Alphaville', case=False, na=False)]
        .groupby('district', as_index=False)
        .agg(preco_medio=('rent', 'mean'))
        .sort_values(by='preco_medio', ascending=False)
        .head(50)
)
top50_districts[:10]

# %%
top50_districts.describe()

# %%
bottom50_districts = df.groupby('district', as_index=False) \
    .agg(preco_medio= ('rent', 'mean')) \
    .sort_values(by='preco_medio') \
    .head(50)

bottom50_districts

# %%
bottom50_districts.describe()

# %%
top_imoveis = df[df['district'].isin(top50_districts['district'])]
bottom_imoveis = df[df['district'].isin(bottom50_districts['district'])]

# %%
top_imoveis['categoria_imovel'] = 'Luxo'
bottom_imoveis['categoria_imovel'] = 'Popular'

# %%
fig = go.Figure()

fig.add_trace(go.Box(
    x=top_imoveis["categoria_imovel"],
    y=top_imoveis["rent"],
    name="Luxo",
    boxpoints="outliers",
    marker_color='lightblue'
))

fig.add_trace(go.Box(
    x=bottom_imoveis["categoria_imovel"],
    y=bottom_imoveis["rent"],
    name="Popular",
    boxpoints="outliers",
    marker_color='thistle'
))

fig.update_layout(
    xaxis=dict(title='Categoria Imovel'),
    yaxis=dict(title='Aluguel'),
    title='Aluguel dos Imóveis por Categoria',
    showlegend=True
)

fig.show()

# %%
rent_by_type_top = top_imoveis.groupby("type")["rent"].mean().reset_index()
rent_by_type_bottom = bottom_imoveis.groupby("type")["rent"].mean().reset_index()

fig = go.Figure()

fig.add_trace(go.Bar(
    x=rent_by_type_top["type"],
    y=rent_by_type_top["rent"],
    name="Top Aptos"
))

fig.add_trace(go.Bar(
    x=rent_by_type_bottom["type"],
    y=rent_by_type_bottom["rent"],
    name="Bottom Aptos"
))

# %%
area_by_type_top = top_imoveis.groupby("type")["area"].mean().reset_index()
area_by_type_bottom = bottom_imoveis.groupby("type")["area"].mean().reset_index()

fig = go.Figure()

fig.add_trace(go.Bar(
    x=area_by_type_top["type"],
    y=area_by_type_top["area"],
    name="Top Aptos"
))

fig.add_trace(go.Bar(
    x=area_by_type_bottom["type"],
    y=area_by_type_bottom["area"],
    name="Bottom Aptos"
))

# %%
top_bedrooms = top_imoveis['bedrooms'].value_counts().reset_index()
top_bedrooms.columns = ['Nº de Quartos', 'Quantidade']
top_bedrooms = top_bedrooms.sort_values(by='Nº de Quartos')

bottom_bedrooms = bottom_imoveis['bedrooms'].value_counts().reset_index()
bottom_bedrooms.columns = ['Nº de Quartos', 'Quantidade']
bottom_bedrooms = bottom_bedrooms.sort_values(by='Nº de Quartos')

fig = go.Figure()

fig.add_trace(go.Bar(
    x=top_bedrooms['Nº de Quartos'].astype(str),
    y=top_bedrooms['Quantidade'],
    name="Top Aptos"
))

fig.add_trace(go.Bar(
    x=bottom_bedrooms['Nº de Quartos'].astype(str),
    y=bottom_bedrooms['Quantidade'],
    name="Bottom Aptos"
))

# %%
top_garages = top_imoveis['garage'].value_counts().reset_index()
top_garages.columns = ['Nº de Garagens', 'Quantidade']
top_garages = top_garages.sort_values(by='Nº de Garagens')

bottom_garages = bottom_imoveis['garage'].value_counts().reset_index()
bottom_garages.columns = ['Nº de Garagens', 'Quantidade']
bottom_garages = bottom_garages.sort_values(by='Nº de Garagens')

fig = go.Figure()

fig.add_trace(go.Bar(
    x=top_garages['Nº de Garagens'].astype(str),
    y=top_garages['Quantidade'],
    name="Top Aptos"
))

fig.add_trace(go.Bar(
    x=bottom_garages['Nº de Garagens'].astype(str),
    y=bottom_garages['Quantidade'],
    name="Bottom Aptos"
))

# %%
subset_imoveis = df[['bedrooms', 'garage', 'rent', 'area', 'total']]

correlation_matrix = subset_imoveis.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

plt.show()

# %%
