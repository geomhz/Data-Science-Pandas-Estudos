import pandas as pd

## Tipos de imóveis ##

## Relatório de analise 02 ##

dados = pd.read_csv('tratando e analisando dados/aluguel.csv', sep = ';')

dados.head(10) ## imprime os 10 primeiros

dados['Tipo'] ## aparece so a variavel que eu quero trabalhar

tipo_imovel = dados['Tipo']

tipo_imovel.drop_duplicates() ## Seleciona todos os tipos de imoveis que existe no CSV SEM REPETIÇÃO

# tipo_imovel.drop_duplicates(inplace = True) seleciona só a key selecionada sem precisar criar variavel

## Organizando a Visualização

tipo_imovel = pd.DataFrame(tipo_imovel)

tipo_imovel.index ## le todos os index (nunmero q aparece do lado)



for i in range(tipo_imovel.shape[0]):
    print(i)



tipo_imovel.index = range(tipo_imovel.shape[0])

print(tipo_imovel)

