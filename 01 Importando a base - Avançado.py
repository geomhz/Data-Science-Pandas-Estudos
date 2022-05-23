import pandas as pd


## Relatório de analise 01 ##

dados = pd.read_csv('Pandas tratando e analisando dados/aluguel.csv', sep = ';')

dados.dtypes #mostra o tipo que cada key é

tipo = pd.DataFrame(dados.dtypes, columns = ['Tipos de dados']) ## cria o nome tipo de dados para a coluna dtypes

tipo.columns.name = 'Variáveis' ## cria o nome variáveis para a key

print(tipo)

dados.shape ## retorna uma tupla com número de linhas e 9 variáveis (key)

dados.shape[0] ## mostra o numero de linhas
dados.shape[1] ## mostra o numero de key

print('A base de dados aprensenta {} registros (imóveis) e {} váriaveis'.format(dados.shape[0], dados.shape[1])) ## na primeira chave vai o dados.shape[0] e na segunda dados.shape[1]


