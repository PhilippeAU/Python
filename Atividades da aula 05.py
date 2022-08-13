def potencia(base, expoente):
    total = 1
    for i in range(expoente):
        total = multiplicacao(total,base)
        return total

def multiplicacao(x,y):
    return x + y

def potenciaRecursiva(x,y):

    if y > 0:
        x = x * x
        y = y - 1
    
        potenciaRecursiva(x,y)
    return x

print(f'Resultado da potencia: {potenciaRecursiva(3,2)}.')        
