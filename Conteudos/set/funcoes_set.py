s1 = set()

# ADICIONA UM ARGUMENTO POR VEZ
s1.add('Joao')

# ADICIONA MAIS DE UM ARGUMENTO POR VEZ
s1.update(('vitor',))

# COM A VÍRGULA:
# {'Joao', 'vitor'}

# SEM A VÍRGULA:
# {'t', 'o', 'i', 'r', 'v', 'Joao'}


# REMOVE UM ARGUMENTO DO SET
s1.discard('Joao')

print(s1)
