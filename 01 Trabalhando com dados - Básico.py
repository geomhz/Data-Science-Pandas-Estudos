from os import sep
import pandas as pd
## pd.set_option('display.max_row', 1000) ##usado para muitas linhas
##pd.set_option: sem essa opção ele mostra somente 10 linhas
## 'display.max_row', número de linhas á ser exibido

# pd.set_option('display.max_columns', 1000) ## usado para muitas colunas

dataset = pd.read_csv('Pandas/data/db.csv', sep = ';') 
## nome da variavel = dataset
## pd.read_csv lê o arquivo CSV
## pasta/diretorio onde está o arquivo CSV
## sep= ';' = define o separador utilizado no conjunto de dados

print(dataset)

print(dataset.dtypes) ## mostra o tipo de cada coluna
# object = string

print(dataset[['Quilometragem', 'Valor']].describe()) ## seleciona as informações que quer dentro de [[para 2 informações]]

print(dataset.info)

## Tuplas são utilizada para armazenar coleçao de itens

## Tuplas não é possivel fazer modificações
## Listas é possivel fazer modificações

nome = 'Passat'
valor = 153000
print((nome, valor)) ## Tupla nome, valor

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])

print(nomes_carros)