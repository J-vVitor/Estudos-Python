receber_cpf = input('Digite o CPF: ')
contador = 10

primeiro_digito = 0

for numeros in receber_cpf:

    primeiro_digito += int(numeros) * contador

    contador -= 1


# VALOR DOS NÚMEROS DO CPF MULTIPLICADO POR 10 E DIVIDIDO POR 11, COM O RESTO DA DIVISÃO
valor_primeiro_digito = ((primeiro_digito * 10) % 11)


# VALOR DO CPF COM O PRIMEIRO DIGITO INCLUSO.
concatecao_com_primero_digito = (receber_cpf + str(valor_primeiro_digito))
