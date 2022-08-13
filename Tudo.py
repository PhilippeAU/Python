frase = 'Curso em Vídeo Python'
print(frase[3:14])

print('Curso' in frase)

print(len(frase)) #Mostra o comprimento da frase

print(frase.count('o')) #Conta quantas vezes algo especifico aparece ('o',0,13)

print(frase.find('deo')) #Acha a palavra que vc quer na frase ('deo')

print(frase.replace('Python','Android')) #Troca uma palavra por outra

print(frase.upper()) #Deixa todas as letras da frase em maiscula

print(frase.lower()) #Deixa todas as letras da frase em minuscula

print(frase.capitalize()) #Deixa a primeira letra da frase em maiuscula

print(frase.title()) #Deixa a primeira letra das palavras em maiuscula

print(frase.strip()) #Elimina espaços no inicio e no fim das frases 

print(frase.rstrip()) #Elimina espaços do lado direito da frase

print(frase.lstrip()) #Elimina espaços do lado esquerdo da frase

print(frase.split()) #Divide os  strings

print('-'.join(frase)) #Ajunta todos os elementos da frase com algo que vc escolhe ('>'.join(frase))