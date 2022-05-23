import pandas as pd

dataset = pd.read_csv('Pandas/data/db.csv', sep = ';', index_col = 0) ## Importa o arquivo db.csv
#le arquivo csv     caminho do arquivo     separador     tira a contagem numerica e o indice 0 nao esta mais embutido

print(dataset) # imprime a planilha inteira

print(dataset.head()) # Mostra os 5 primeiros registros do arquivo csv

print(dataset['Valor']) #mostra o valor de todos os itens do csv

# verificar o tipo de arquivo

print(type(dataset['Valor'])) ## mostra o tipo do que ele é (no caso Series)

print(type(dataset[['Valor']])) ## com 2 [] ele vira DataFrame

## Observação: A indexação tem origem no zero e nos fatiamentos (slices) a linha com índice i é incluída e a linha com índice j não é incluída no resultado. Em nosso exemplo, pegaremos as três primeiras linhas ([0:3]) do nosso dataset.

## Selecionando linhas

print(dataset[0:3]) ## imprime as linhas do arquivo dataset do indice 0 á 3

# .loc seleciona um grupo de linahs e colunas segundo os rótulos ou uma matriz booleana

dataset.loc['Passat'] #retorna todas as informações do passat
 
dataset.loc[['Passat', 'DS5']] ## usar [] passa puxar mais de 1 key

dataset.loc[['Passat', 'DS5'], ['Motor','Valor']] #puxa informação de 2 carros e de 2 colunas apenas

dataset.loc[:, ['Motor', 'Valor']] # Mostra TODAS AS LINHAS da coluna Motor e Valor

# .iloc também nos permite fazer seleções, mas se utiliza dos índices numéricos - ou seja, na posição das informações.

dataset.iloc[1] ## MOSTRA TODAS AS INFORMAÇÕES DO INDICE 1 em series
dataset.iloc[[1]]  ## MOSTRA TODAS AS INFORMAÇÕES DO INDICE 1 em dataframe

dataset.iloc[1:4] ## retorna o indice 0 até o 3

dataset.iloc[1:4, [0, 5, 2]] ## retorna o carro do indice 1 ao 3, selecionando colunas indice 0, 5 e 2 (motor, valor e quilometragem)

dataset.iloc[[1,42,22], [0, 5, 2]] ## retorna a linha 1, 42 e 22 com as infos das colunas motor, valor e km