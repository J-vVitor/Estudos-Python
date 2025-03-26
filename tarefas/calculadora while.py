'''
 Criar calculadora e fazer as operações de acordo com o operador que o usuário digitou.

'''
while True:
    
    # CAMPO PARA RECEBER INFORMAÇÕES DO USUÁRIO
    num_um = input('Digite um número: ');
    num_dois = input('Digite outro número: ');
    operador = input('Digite o operador ( + - * / ) ');
    
    # CAMPO PARA CONVERSÃO DE STRING PARA INTEIRO
    num_um_conversao = int(num_um)
    num_dois_conversao = int(num_dois)
    
    # CAMPO QUE VERIFICA SE FORAM DIGITADOS NÚMEROS
    if num_um.isdigit() and num_dois.isdigit():
    
        if operador == '+':
            print(num_um_conversao + num_dois_conversao);
            
        elif operador == '-':
            print(num_um_conversao - num_dois_conversao);   
            
        elif operador == '*':
            print(num_um_conversao * num_um_conversao);
            
        elif operador == '/':
            print(num_um_conversao // num_dois_conversao);
            
        else:
            print('Você não digitou um operador')
             
    continuacao = input('Deseja continuar? [s]im [n]ão ')
    
    if continuacao == 's' or continuacao == 'S':
        continue
    else:
        break
            
        