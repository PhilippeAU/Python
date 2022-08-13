#Programa para fazer um desconto de 5% do produto

v = float(input('Digite o valor do produto: '))

d = ((v * 5)/100)

print('O valor do produto com desconto: R${:.2f}' .format(v-d)) 