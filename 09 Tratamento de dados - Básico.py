import pandas as pd

dataset = pd.read_csv('Pandas básico/data/db.csv', sep = ';')

print(dataset.info()) ## mostra todas as informaçoes do arquivo NULAS e NAO NULAS

## selecionando informações nulas

dataset.Quilometragem.isna() ## Series booleana que mostra quando o valor for nulo, retorna TRUE

nulo = dataset[dataset.Quilometragem.isna()] ## mostra todas as Series booleana que deu NULO, TRUE

print(nulo)

## mudando a informação nula

dataset.fillna(0, inplace = True) ##preencher o valor nulo (na) com o numero 0

print(dataset.query("Zero_km == True")) ## consulta se o valor 0km ta nulo ou nao

## voltar com a dataset antiga

dataset = pd.read_csv('Pandas/data/db.csv', sep = ';')

dataset.dropna(subset = ['Quilometragem']) ## se a quilometragem for nulo, ela é eliminada

