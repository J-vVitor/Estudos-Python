numero_um = int(input('Digite um numero: '))
num_um = numero_um * 10
resultado_num_um = num_um

numero_dois = int(input('Digite um numero: '))
num_dois = numero_dois * 9
resultado_num_dois = num_dois

numero_tres = int(input('Digite um numero: '))
num_tres = numero_tres * 8
resultado_num_tres = num_tres

numero_quatro = int(input('Digite um número: '))
num_quatro = numero_quatro * 7
resultado_num_quatro = num_quatro

numero_cinco = int(input('Digite um número: '))
num_cinco = numero_cinco * 6
resultado_num_cinco = num_cinco


numero_seis = int(input('Digite um número: '))
num_seis = numero_seis * 5
resultado_num_seis = num_seis

numero_sete = int(input('Digite um número: '))
num_sete = numero_sete * 4
resultado_num_sete = num_sete


numero_oito = int(input('Digite um número: '))
num_oito = numero_oito * 3
resultado_num_oito = num_oito

numero_nove = int(input('Digite um número: '))
num_nove = numero_nove * 2
resultado_num_nove = num_nove


# SOMA DE TODOS OS NUMEROS

soma_de_todos_os_numeros = resultado_num_um+resultado_num_dois+resultado_num_tres+resultado_num_quatro + \
    resultado_num_cinco+resultado_num_seis + \
    resultado_num_sete+resultado_num_oito+resultado_num_nove

primeiro_digito_resultado = int((soma_de_todos_os_numeros * 10) % 11)

primeiro_digito_condicao = primeiro_digito_resultado if 9 else 0

print(primeiro_digito_condicao)
