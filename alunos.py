import random
AL1 = str(input('Primeiro aluno: '))
AL2 = str(input('Segundo aluno: '))
AL3 = str(input('Terceiro aluno: '))
AL4 = str(input('Quarto aluno: '))
lista = [AL1 ,AL2, AL3, AL4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}' .format(escolhido))
