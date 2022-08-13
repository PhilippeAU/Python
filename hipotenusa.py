CO = float(input("Comprimento do cateto oposto: "))
CA = float(input('Comprimento do catero adjacente: '))
HI = (((CO ** 2) + (CA ** 2)) ** (1/2))
print('A Hipotenusa vai medir: {:.2f}'.format(HI))


#Com importação
import math
CO2 = float(input("Comprimento do cateto oposto: "))
CA2 = float(input('Comprimento do catero adjacente: '))
HI2 = math.hypot(CO2,CA2)
print('A Hipotenusa vai medir: {:.2f}'.format(HI2))