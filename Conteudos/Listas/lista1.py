
"""
(CRUD) - CREATE READ UPDATE DELETE

"""

"""

---- APAGAR UM ITEM ESPECÍFICO DA LISTA: ---
    
    DEL.LISTA_EXMEPLO[-1] - APAGA O ÚLTIMO INDÍCE DA LISTA;
    
    
                     0 1 2 3
    LISTA_EXEMPLO = [0,1,2,3];
    
    DEL.LISTA_EXEMPLO[2];
    
    SAIDA: LISTA_EXEMPLO = [0,1,3]
    
"""

"""

---- ADICIONAR UM INDÍCE AO FINAL DA LISTA ----

                     0 1 2 3
    LISTA_EXEMPLO = [0,1,2,3];

    LISTA_EXEMPLO.APPEND(4)
    
    SAIDA: LISTA_EXEMPLO = [0,1,2,3,4]
    
"""

"""

---- REMOVER O ÚLTIMO ELEMENTO DA LISTA ----

                     0 1 2 3
    LISTA_EXEMPLO = [0,1,2,3];

    LISTA_EXEMPLO.POP()
    
    SAIDA: LISTA_EXEMPLO = [0,1,2]

"""

'''

---- LIMPAR A LISTA ----

                    0 1 2 3
    LISTA_EXEMPLO = [0,1,2,3];

    SAIDA: LISTA_EXEMPLO = []

'''


"""

---- INSERIR UM ITEM NA LISTA EM UM INDÍCE ESPECÍFICO ----

                    0  1 2 3
    LISTA_EXEMPLO = [0,1,2,3];

    LISTA_EXEMPLO.INSERT(0 - INDICE, 4 - NÚMERO INSERIDO)
    
    SAIDA: LISTA_EXEMPLO = [4,0,1,2,3]

"""


'''

--- CONCATENAÇÃO DE LISTAS ----

    LISTA_1 = [0,1]
    LISTA_2 = [2,3]
    
    LISTA_3 = LISTA_1 + LISTA_2
    
    SAIDA: LISTA_3 = [0,1,2,3]


'''



listas_de_compras = ['Feijão','Arroz','Carne']

print(listas_de_compras[0])