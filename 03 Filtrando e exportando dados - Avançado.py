import pandas as pd



## Relatório de analise 03 ##

dados = pd.read_csv('tratando e analisando dados/aluguel.csv', sep = ';')

dados.head(10)

list(dados['Tipo'].drop_duplicates()) ## pega os tipos de imovel 

residencial = ['Quitinete',             ## separamos quais são residenciais
'Casa',
'Apartamento',
'Casa de Condomínio',
'Casa de Vila']


selecao = dados['Tipo'].isin(residencial) ## Caso tenha algum item que está no residencial dentro do dado 'Tipo' retorna true

# selecao = dados['Tipo'].isin(residencial) ## Caso tenha algum item que está no residencial dentro do dado 'Tipo' retorna true os 10 primeiros apenas

dados_residencial = dados[selecao] ## dados residencial = apenas dados da selecao isin residencial

print(dados_residencial)

# print(list(dados_residencial['Tipo'].drop_duplicates())) ## checa os tipos de imoveis novamente (apenas residencial)


# print(dados.shape[0]) ## tem 32 mil elementos

# print(dados_residencial.shape[0]) ## tem 22 mil elementos

dados_residencial.index = range(dados_residencial.shape[0]) ## reconstroi os dados residenciais colocando todas as qtidades de imoveis residenciais na ordem correta

print(dados_residencial)

## Exportando a base de dados

dados_residencial.to_csv('tratando e analisando dados/aluguel_residencial.csv', sep = ';') ## exporta o db  importnado o index com o banco de dados

dados_residencial.to_csv('tratando e analisando dados/aluguel_residencial2.csv', sep = ';', index = False) ## exporta o db sem o index 