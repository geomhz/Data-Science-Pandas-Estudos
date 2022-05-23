import pandas as pd

## Listas: São coleções sequenciais, isto é, os itens destas sequências estão ordenados e utilizam índices (números inteiros) para acessar os valores.

## Dicionários:São estruturas de dados que representam um tipo de mapeamento. Mapeamentos são 
 #             coleções de associações entre pares de valores onde o primeiro elemento do par 
 #             é conhecido como chave (key) e o segundo como valor (value).


carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

carros.index('Passat') ## mostra o indice que ta o Passat

#dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16} ## dicionario

#type(dados) == dict 

list(zip(carros, valores))

dados1 = dict(zip(carros, valores)) ##transforma carros e valores em 1 dicionario 

print(dados1)

## Operações com dicionários

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}


## dict['key']

print(dados['Passat']) ## Imprime o valor correspondente á (key) referente ao passay (key)

# 'Passat' in dados  TRUE ou FALSE, caso tem ou nao tem

# 'Fusca' not in dados -- True pois nao esta em dados

print(len(dados)) ## Retorna 3 pois tem 3 keys no dicionário

# dict[key] = value
dados['DS5'] = 124549.07 ## adicionei o carro DS5 com o valor de 124549.07 no dicionario

print(dados)

#del dict[key]

del dados['Passat'] ## deleta a key Passat e o valor do dicionario

dados.update({'Passat': 106161.95, 'Fusca': 150000}) 

print(dados)

dados2 = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    }, 
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

print('acessorios' in dados2['Crossfox']) ## imprimir TRUE ou FALSE se tem acessorios em Crossfox
print('acessorios' in dados2['Passat']) ## imprimir TRUE ou FALSE se tem acessorios em Passat
print(dados2['Crossfox']['valor']) ## Imprimir o valor do Crossfox
print(dados2['Passat']['acessorios'][-1]) ## Imrpimir o ultimo acessório do Passat


#del dict['key'] # Deleta a key Passat

del dados['Passat']

#dict.update() # Adiciona alguma key de volta

dados.update({'Passat': 106161.95, 'Fusca': 150000}) 

#dict.copy() ##cria outra variavel com a mesma informaçao do dict
 
dados3 = dados.copy()

print(dados3)

del dados3['Fusca']

print(dados3)

## dict.pop(key[default])
    #elimina o key selecionado

dados3.pop('Passat') ## retorna quem ele eliminou

print(dados3.pop('Passat', 'Chave não encontrada'))
 
## dict.clear() limpa o dict inteiro

dados3.clear()

print(dados3)

## dict.keys() retorna uma lista contendo as chaves do dicionario

print(dados.keys())

for key in dados.keys():
    print(dados[key]) ## retorna o valor de cada key

## dict.values() #retorna todos os valores também

print(dados.values())

## dict.items() ##faz tuplas com key+valor

print(dados.items())

for item in dados.items():
    print(item)

for key,value in dados.items():
    print(key,value)

for key,value in dados.items():
    if (value > 100000):
        print(key)