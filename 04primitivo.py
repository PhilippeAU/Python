algo = input('Digite algo? ')

print('O tipo primivivo desse valor é: {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}' .format(algo.isnumeric()))
print('É alfabetico? {}' .format(algo.isalpha()))
print('É alfanúmerico? {}' .format(algo.isalnum()))
print('Está em maiúscula? {}' .format(algo.isupper()))
print('Está em minúscula? {}' .format(algo.islower()))
print('Está capitalizada? {}' .format(algo.istitle())) # Quando a palavra é maiúscula e menúscula!
