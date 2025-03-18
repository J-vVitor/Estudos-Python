# CHECAR SE A LETRA QUE O USUÁRIO DESEJA ESTÁ NO NOME DIGITADO


nome_usuario = input('Digite seu nome: ');

letra_procurada = input('Digite a letra procurada: ')

if letra_procurada in nome_usuario:
    print(f'{letra_procurada} está entre {nome_usuario}');
    
else:
    print(f'{letra_procurada} não está entre {nome_usuario}')