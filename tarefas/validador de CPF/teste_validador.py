
# REPLACE PARA SUBSTITUIR ALGO
receber_cpf = input('Digite o CPF: ').replace('.', '').replace('-', '')
contador = 10

primeiro_digito = 0

for numeros in receber_cpf:

    primeiro_digito += int(numeros) * contador

    contador -= 1


# VALOR DOS NÚMEROS DO CPF MULTIPLICADO POR 10 E DIVIDIDO POR 11, COM O RESTO DA DIVISÃO
valor_primeiro_digito = ((primeiro_digito * 10) % 11)
valor_primeiro_digito if valor_primeiro_digito <= 9 else 0


# TRANFORMANDO O VALOR DO PRIMEIRO DIGITO PARA STRING, FAZENDO A CONCATENAÇÃO COM O CPF DIGITADO
valor = receber_cpf + str(valor_primeiro_digito)

contador_2 = 11
segundo_digito = 0

for digitos in valor:

    segundo_digito += int(digitos) * contador_2

    contador_2 -= 1

# O VALOR DO SEGUNDO DIGITO MULTIPLICADO POR 10 E DIVIDIDO POR 11, COM RESTO DA DIVISÃO
valor_segundo_digito = ((segundo_digito * 10) % 11)

# CONDIÇÃO SE O NÚMERO FOR MAIOR QUE NOVE (FICA ZERO), SE NÃO CONTINUA O MESMO NÚMERO
valor_segundo_digito if valor_segundo_digito <= 9 else 0


# CONCATENANDO O VALOR (CPF JÁ COM O PRIMEIRO DIGITO + O SEGUNDO DIGITO )
resultado_final = valor + str(valor_segundo_digito)

print(resultado_final)
