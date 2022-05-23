import pandas as pd

dataset = pd.read_csv('Pandas/data/db.csv', sep = ';')

#dataset.head() #mostrar os primeiros 5 infos


# Query são consultas que podem ser realizadas em dataframes, de modo semelhante às seleções, mas utilizando técnicas mais sofisticadas

# print(dataset.Motor) # imprime o motor de todos os carros

motor = dataset.Motor == 'Motor Diesel' # criei uma variavel motor que retorna uma Series booleana, usando true ou falso  

# print(dataset[motor]) ## imprimo todos os carros que tem Motor Diesel dentro do arquivo dataset

km = dataset.Zero_km == True # criei uma variavel km que retorna uma Series booleana, usando true ou falso  

print(dataset[(motor) & (km)]) ## pega somente MOTORES Á DIESEL COM 0KM 
# imrpimir arquivo dataset [(variavel 1) & (variavel 2)]


# metodo query 

motor_km = dataset.query('Motor ==  "Motor Diesel" and Zero_km == True') ##variavel motor_km 
                                                                         ##criei uma query para buscar a mesma informação de cima 

print(motor_km)
