lista = [
    {'nome': 'João', 'sobrenome': 'Vitor'},
    {'nome': 'Thiago', 'sobrenome': 'Bruno'},
    {'nome': 'Bruno', 'sobrenome': 'Da silva'},
    {'nome': 'Cesar ', 'sobrenome': 'Luiz'},
    {'nome': 'Felipe', 'sobrenome': 'Tavares'},
]


# PRIMEIRO TENHO QUE ORDENAR TODA A LISTA JÁ COM A FUNÇÃO 'LAMBDA'


# FEITO COM SORT:

lista.sort(key = lambda item : item['nome'])

print('Ordenando pelo primeiro nome com sort:')
print()
for i in lista:
    print(i)

# COM SORTED:


def exibir(lista):
    for nome in lista:
        print(nome)

l1 = sorted(lista, key = lambda item: item['nome'])
l2 = sorted(lista, key = lambda item: item['sobrenome'])

print()
print('Ordenados pelo primeiro nome:')
print()

exibir(l1)

print()
print('Ordenados pelo sobrenome:')
print()

exibir(l2)

