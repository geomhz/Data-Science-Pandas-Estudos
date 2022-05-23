import pandas as pd

# Series = arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado
# Index = Os rótulos das linhas de uma series são conhecidos como index
## exemplo: s = pd.Series(dados, index = index)

# Dataframe = uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. Assim como as series, os dataframes são capazes de armazenar qualquer tipo de dado
## exemplo: df = pd.DataFrame(dados, index = index, columns = columns)


# Series
carros = ['Jetta Variant', 'Passat', 'Crossfox']

car = pd.Series(carros)

print(car)

# DataFrame a partir de uma lista de dicionarios

dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

dataset = pd.DataFrame(dados)

print(dataset)

# dataset[['Nome', 'Motor', 'Ano', 'Quilometragem', 'Zero_Km', 'Valor']] # Para mudar a Ordem de algum dos items

## ou 

dados1 = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}

dataset1 = pd.DataFrame(dados1)

print(dataset1)

