import pandas as pd

dados = pd.read_csv('tratando e analisando dados/aluguel_residencial2.csv', sep = ';')



## Relatório de analise 04 ##
## ANALISE DE DADOS seleções e frequencias ##

#Selecione somente os imóveis classificados com tipo 'Apartamento'.

selecao = dados['Tipo'] == 'Apartamento' ## mostra em true ou false a selecao dos aptos
n1 = dados[selecao].shape[0] ## mostra o total de dados do tipo apartamentos que existem na planilha

print(n1)

#Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.

selecao1 = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila') ## | = or
n2 = dados[selecao1].shape[0]

print(n2)

#Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
#60 <= área <= 100

selecao2 = (dados['Area'] >= 60) & (dados['Area'] <= 100) ## & = and
n3 = dados[selecao2].shape[0]

print(n3)

#Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.

selecao3 = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000.0)
n4 = dados[selecao3].shape[0]
print(n4)

## Resultado

print("Nº de imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'-> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))




