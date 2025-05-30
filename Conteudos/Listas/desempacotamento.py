"""
    Desempacotamento de listas
"""

lista_1 = ['João','Vitor','Pereira','Lima']

nome1,nome2,nome3,nome4 = lista_1;

print(nome1,nome2,nome3,nome4)


'''
    Nesse tipo de empacotamento pega um valor e joga em uma variável 
    e acopla o restante em outra variável.

'''


lista_2 = ['João','Vitor','Pereira','Lima'];

nome1_2, *resto_da_lista = lista_2

print(f'{nome1_2}, resto da lista: {resto_da_lista}')


'''
    Se não for ultilizar a variável:
    
'''


lista_3= ['João','Vitor','Pereira','Lima'];

nome1,*_ = lista_3

print(f'Resto da variável: {_}')