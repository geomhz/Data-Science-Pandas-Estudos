import pandas as pd

dados = pd.read_csv('tratando e analisando dados/aluguel_residencial3.csv', sep = ';')

## Relatório de analise 6 ##
## Criando novas variáveis ##

# criando valor bruto do aluguel mensal #
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados ['IPTU']

# criando o valor do m2 do imovel #
dados['Valor m2'] = dados['Valor'] / dados['Area']

# colocando limite de 3 digitos no valor do m2
dados['Valor m2'] = dados['Valor m2'].round(3)

# Colocando o valor bruto do m2 #
dados['Valor Bruto m2'] = dados['Valor Bruto'] / dados['Area'].round(3)

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')

print(dados)

## Excluindo variáveis do dataframe ##

dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])

print(dados_aux.head(10))

## Jeito 1 de deletar

del dados_aux['Valor Bruto'] 

print(dados_aux.head(10))

## Jeito 2 de deletar

dados_aux.pop('Valor Bruto m2')

print(dados_aux.head(10))

## Jeito 3 de deletar

dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis= 1) ## Axis =  1 coluna, 0 linha

## tirar da planilha dados