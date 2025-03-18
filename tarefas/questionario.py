nome_usuario = input('Digite o seu nome: ');
idade_usuario = input('Digite sua idade: ');
leitura_do_nome = len(nome_usuario);

if nome_usuario and idade_usuario != '':
    
    print(f'Seu nome é: {nome_usuario}');
    
    print(f'Seu nome invertido é: {nome_usuario[::-1]}')
    
    if '' in nome_usuario:
        print('O seu nome contém espaços')
        
    else:
        print('Seu nome não contém espaços')
    
    print(f'O seu nome tem: {len(nome_usuario)} letras');
    
    print(f'A primeira letra do seu nome é: {nome_usuario[0]}')
    
    print(f'A última letra do seu nome é: {nome_usuario[-1]}')
    
else:
    print('Desculpe, você deixou campos vazios.')