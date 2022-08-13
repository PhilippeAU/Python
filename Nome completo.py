nome = str(input('Digite seu nome: ')).strip()

print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome em minúsculo é {}' .format(nome.lower()))
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
