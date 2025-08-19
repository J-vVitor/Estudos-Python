s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

numero_digitado_pelo_usuario = input('Digite um número: ')
numero_digitado_pelo_usuario = int(numero_digitado_pelo_usuario)

if numero_digitado_pelo_usuario in s1:
    print()
    print(f'O número {numero_digitado_pelo_usuario} está entre o set')

else:

    print('Deu errado')
