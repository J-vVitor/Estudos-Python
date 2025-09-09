lista = [
    {'nome': 'João', 'sobrenome': 'Vitor'},
    {'nome': 'Thiago', 'sobrenome': 'Bruno'},
    {'nome': 'Bruno', 'sobrenome': 'Da silva'},
    {'nome': 'Cesar ', 'sobrenome': 'Luiz'},
    {'nome': 'Felipe', 'sobrenome': 'Tavares'},
]


# PRIMEIRO TENHO QUE ORDENAR TODA A LISTA JÁ COM A FUNÇÃO 'LAMBDA'


# FEITO COM SORT:

lista.sort(key=lambda item: item['nome'])

for i in lista:
    print(i)
    
print()

# COM SORTED:

ord_first_name = sorted(lista,key=lambda item: item['nome'])
ord_last_name = sorted(lista,key=lambda item: item['sobrenome'])

def ordem(lista):
    for nomes in lista:
        print(nomes)

print('Ordenado pelo primeiro nome:')
ordem(ord_first_name)
print()
print('Ordenado pelo segundo nome:')
ordem(ord_last_name)


