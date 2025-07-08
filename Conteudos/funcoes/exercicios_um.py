# crie um funçãp que multiplica todos os argumento não nomeados recebidos
# Retorne o total oara uma variavel e mostre o valor da variavel

def multiplicar(*args):
    resultado = 1

    for numeros in args:
        resultado *= numeros

    return resultado


multilplicacao = multiplicar(4, 5)

print(multilplicacao)

# PAR OU ÍMPAR
valor = int(input('Digite um número: '))

if valor % 10 == 0:
    print('Número par!')


else:
    print('Número ímpar')
