lista_a = [0,1,2,3,4,5,6]

lista_b = lista_a ;

"""
 A LISTA_A E A LISTA_B APONTAM PARA O MESMO " ARQUIVO " NA MEMÓRIA 

"""
lista_a = [0,1,2,3,4,5,6]

lista_b = lista_a.copy()

lista_a[0] = 'Indicie zero'

print(lista_a);
print(lista_b)

"""
 MESMO QUE A LISTA_B ESTEJA PUXANDO A LISTA_A, AS DUAS APONTAM PARA " ARQUIVOS " 
 DIFERENTES NA MEMÓRIA

"""

