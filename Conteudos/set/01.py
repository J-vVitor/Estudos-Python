# SET - COLEÇÃO NÃO ENUMERADA, BASICAMENTE É UMA LISTA SEM ORDEM;

s1 = set('1' '2' '3' '5' '6' '4')

print(s1)

# Transformando-os em números inteiros
for i in s1:
    i = int(i)

    print(i, type(i))


s2 = {1, 2, 3, 5, 6, 4}
print()

# SABER SE UM INDICE ESTÁ DENTRO DO SET

if 3 in s2:
    print('Dentro do set')

print(s2)
