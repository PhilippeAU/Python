import math
AN = float(input('Digite o ângulo: '))
SEN = math.sin(math.radians(AN))
COS = math.cos(math.radians(AN))
TAN = math.tan(math.radians(AN))

print('O ângulo de {} tem o SENO de {:.2f} e tem o COSSENO de {:.2f} e tem a TANGENTE de {:.2f}' .format(AN,SEN,COS,TAN) )
