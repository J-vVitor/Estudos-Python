import random
import sys

cpf = ''

for i in range(9):
    cpf += str(random.randint(0, 9))

print(cpf)

sys.exit()

print('teste')
