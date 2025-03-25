'''
 Faça um programa que peça ao usuário para digitar um número inteiro,
 informe se este número é par ou ímpar. Caso o usuário não digite um número
 inteiro, informe que não é um número inteiro.
 '''
''' 
capturar_numero = input('Digite um número inteiro: ');

if capturar_numero.isdigit():
    transformar_para_inteiro = int(capturar_numero);
    par_ou_impar = transformar_para_inteiro % 2 == 0;   
    
    if par_ou_impar == True:
        print('Número par!')

    else:
        print('Número impar!')
    
else:
    print('Você não digitou um número intero')
    '''
    
'''
 Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
 descrito, exiba a saudação apropriada. Ex. 
 Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
 

hora_digitada = input('Digite o horário: ');

se_hora_for_numero = hora_digitada.isdigit()

if se_hora_for_numero:
    
    hora_float = float(hora_digitada)
    
    if hora_float >= 00 and hora_float <= 4:
        print('Boa madrugada');
        
        
    elif hora_float >= 5 and hora_float <= 11:
        print('Boa dia!')
    
    elif hora_float >= 12 and hora_float <= 17:
        print('Boa tarde')
        
else:
    print('Boa noite')

'''

'''
 Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
 menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
 "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
'''

nome_usuario = input('Digite seu nome: ');

nome_usuario_contado = len(nome_usuario)

if nome_usuario_contado <= 4:
    print('Seu nome é curto')
    
elif nome_usuario_contado >= 5 and nome_usuario_contado <=6:
    print('Seu nome é normal')
    
else:
    print('Seu nome é longo')