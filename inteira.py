#Com módulo
from math import trunc
n = float(input('Digite um número real: '))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(n,trunc(n)))

#Sem módulo
n = float(input('Digite um número real: '))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(n,int(n)))