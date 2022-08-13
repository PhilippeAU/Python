PI = float(input('Digite o comprimento da pista: '))
VO = int(input('Digite quantas voltas seram dadas: '))
AB = int(input('Digite quantas vezes será reabastecida: '))
CO = float(input('Digite a quantidade de combustível: '))

PETO = ((PI/1000)*VO) #PErcurso TOtal
DIRE = (PETO / (AB + 1)) #DIstância de REabastecimento
LITROS = (DIRE / CO)

print('O Valor mínimo de litros até o primeiro reabastecimento é {:.3f}'.format(LITROS))