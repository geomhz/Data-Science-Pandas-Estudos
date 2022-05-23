from numpy import append
import pandas as pd

## Função Built in
## Funções são unidades de código reutilizáveis que realizam tarefas específicas. Elas podem receber inputs, que são as entradas (também chamadas de parâmetros), e podem retornar resultados

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

## jeito dificil de somar

valores = []

for valor in dados.values(): 
    valores.append(valor)

print(valores) ## 1 lista

soma = 0 

for valor in dados.values():
    soma += valor

print(soma) ## 2 soma

## jeito facil de somar

print(list(dados.values())) # 1 lista

print(sum(dados.values())) # 2 soma

## funçao help para cada comando
print(help(append))

