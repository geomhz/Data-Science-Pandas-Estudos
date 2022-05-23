import pandas as pd

## Relatorio de analises 5 ##
## Tratamento de dados faltantes (null) 'Valor' ##

dados = pd.read_csv('tratando e analisando dados/aluguel_residencial2.csv', sep = ';')

dados.isnull() ## se valor for nulo =  true, se não false
dados.notnull() ## se valor nao for nulo = true, se não false

# dados.info() ##mostra a qtidade dos valores nao nulos da planilha inteira

## Puxando valores nulos do 'Valor'

dados['Valor'].isnull() # true ou false

dados[dados['Valor'].isnull()] # aparece todos os itens sem true ou false, com o valor nulo


## Tratando valores NULOS e removendo as linhas com o 'Valor' Nulo

A = dados.shape[0] ## puxa o valor de imoveis com os valores nulos
print(A) 

dados.dropna(subset = ['Valor'], inplace =  True) # retira os itens com valores NA da coluna VALOR, no total 9 
B = dados.shape[0]
print(B)


## Tratamento de dados faltantes (null) pt 2 ##

dados[dados['Condominio'].isnull()].shape[0] ## mostra a quantidade de valores NULL de 'Condominios'

selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull()) ## Quero remover eles

C = dados.shape[0] ## puxa o valor de imoveis com os valores nulos
dados1 = dados[~selecao] ## inverte o true e false vira false e true

D = dados1.shape[0]

print(C - D)

dados = dados.fillna({'Condominio': 0, 'IPTU': 0}) ## preenche todos os valores nulos

dados.info() 

dados.to_csv('tratando e analisando dados/aluguel_residencial3.csv', sep = ';', index = False)

