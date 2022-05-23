import pandas as pd

dataset = pd.read_csv('Pandas/data/db.csv', sep = ';')

#for item in dataset:
#    print(item) ## imprime as colunas

#é um iterador, podemos utilizá-lo em conjunto com o for para desempacotarmos tais tuplas em dados específicos, por exemplo index e row, ou seja, os índices e informações das linhas

print(list(dataset.iterrows()))

for index, row in dataset.iterrows(): 
    if(2019 - row['Ano'] != 0): ## se 2019 - ano for diferente de 0, então
        dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano']) #dataset.loc vai criar uma index km media que vai ser a linha Quilometragem / 2019 - a linha ano
    else:
        dataset.loc[index, 'Km_media'] = 0 #se for igual a 0 = 0

print(dataset)