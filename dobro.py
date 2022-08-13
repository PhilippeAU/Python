#Programa para mostrar o dobro o triplo e a raiz quadrada de um número

n = float(input('Digite um número: '))

print('O número que digitado foi: {} dobro: {} triplo: {} raiz quadrada: {:.2f}'. format(n,(n*2),(n*3),(n**(1/2))))