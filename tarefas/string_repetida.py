import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0, 8))

print(cpf)
