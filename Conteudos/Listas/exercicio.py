import os

lista = []

while True:

    print('Selecione uma opção: ')
    opcoes = input('[i]nserir [a]pagar [l]istar : ')

    if opcoes == 'i':

        item_adicionado_na_lista = input('Item a ser adicionado: ')

        lista.append(item_adicionado_na_lista)

        os.system('cls')

    elif opcoes == 'a':
        print('teste')
        os.system('cls')

    elif opcoes == 'l':
        os.system('cls')
        contagem = 0

        for indice, itens in enumerate(lista):

            print(indice, itens)
            contagem += 1
        break
