N = int(input("Digite o valor: "))
C = N
F = 1
print('Calculando {}! = '.format(N), end='')
while C > 0:
    print('{}'.format(C), end='')
    print(' → ' if C > 1 else ' = ', end='')
    F = F * C
    C -= 1

print('{}'.format(F))

