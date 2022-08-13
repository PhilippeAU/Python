x = int(input('Digite o valor da base: '))
y = int(input('Digite o valor do expoente: '))

def potencia(base, expoente):
  if expoente == 0:
    return 1
  else:
    return base * potencia(base, expoente - 1)
 

def main():
  base = x
  expoente = y
  print(f'O Resultado da potencia: {potencia(base, expoente)}.')
   
if __name__== "__main__":
  main()
