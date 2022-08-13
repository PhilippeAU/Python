
def potencia(base, expoente):
  if expoente == 0:
    return 1
  else:
    return base * potencia(base, expoente - 1)
 

def potenciaRecursiva():
    base = int(input('Digite o valor da base: '))
    expoente = int(input('Digite o valor do expoente: '))

    potenciaRecursiva(base,expoente)

print(f'O Resultado da potencia: {potenciaRecursiva}')
   
