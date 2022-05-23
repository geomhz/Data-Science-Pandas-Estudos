import os
import pandas as pd

## funções sem e com parametros


#   sem parametro

# def <nome>():
#   <instrução>

def media(): ## usar comando media() para executar a funçao
    valor = (1 + 2 + 3) / 3
    print(valor) ## printa o valor ao ser executado

media() ## defino valores fixos na funçao sem parametro

#  com parametro

def media1(number_1, number_2, number_3):
    valor = (number_1 + number_2 + number_3) / 3
    print(valor)

media1(10, 8, 7) ## posso usar a função para valores nao fixos
                 ## limitado em 3 numeros (number1 number2 number3)
# com lista

def media2(lista):
    valor = sum(lista) / len(lista) # soma da lista / qtidade de numeros definidos da lista
    print(valor)                    # na hr da execução da função

media2([1, 3, 5, 7, 10, 9, 5, 6]) ## posso fazer com a quantidade de numero que eu quiser

#aqui ele não encontra valor para retornar

## função que retorna resultado

#def <nome>(<param_1>, <param_2>, ..., <param_n>):
#    <instruções>
#    return <resultado>

def media3(lista):
    valor = sum(lista) / len(lista)
    return valor
    
print(media3([1, 2, 3, 4, 5, 6, 7, 8]))

resultado = media3([1, 2, 3, 4, 5, 6, 7, 8]) 

print(resultado) ## agora retorna o valor media 3

## retornando mais de um valor

def media4(lista):
    valor = sum(lista) / len(lista)
    return(valor, len(lista)) ## retorna valor da media (soma da lista / qtidade da lista) + a qtidade de elemento na lista (len)

print(media4([1, 2, 3, 4, 5, 6, 7, 8]))

resultado, n =  media4([1, 2, 3, 4, 5, 6, 7, 8])

print(n)
print(resultado)
