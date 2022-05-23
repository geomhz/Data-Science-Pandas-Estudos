import pandas as pd

## Tuplas são utilizada para armazenar coleçao de itens

## Tuplas não é possivel fazer modificações
## Listas é possivel fazer modificações

nome = 'Passat'
valor = 153000
print((nome, valor)) ## Tupla nome, valor

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
 #                     0                1         2 ou -2     3 ou -1
print(nomes_carros)

print(nomes_carros[0]) ## Imprime o nome_carros indice 0

print(nomes_carros[1:3])

nomes_carros1 = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))

print(nomes_carros1[-1][0])   #-1 = acessando a ultima tupla entre parenteses e selecionando algum carro com o indice dentro da tupla

## iterando em tuplas

for item in nomes_carros:
    print(item)


carro_1, carro_2, carro_3, carro_4 = nomes_carros
#carro_1 = indice 0


print(carro_4)

_, A, _, B = nomes_carros
#_underscore ignora o indice que está _


print(A)

print(B)

_, C, *_ = nomes_carros 

#_ ignora o indice que eu quero
# *_ ignora todo os restantes 


# usando ZIP 

# carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
# valores = [88078.64, 106161.94, 72832.16, 124549.07]

# print(zip(carros,valores)) ## zipa o carros + valores

# lista = list(zip(carros,valores)) ## criei variavel lista para criar tabela do carro e valor

# print(lista)

# for item in zip(carros, valores):
#     print(item) ## cria uma lista com zip valores e nomes


# for carro, valor in zip(carros, valores):
#     if(valor > 100000):
#         print(carro, valor) #se o valor do carro for maior que cem mil, imprime o nome + valor do carro
     
## Operações com dicionários

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}


## dict['key']

print(dados['Passat'])
