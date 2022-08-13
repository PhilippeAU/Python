d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))

D = (d * 60)
K = (k * 0.15)

print('O total a pagar é de R${:.2f}' .format(D+K))