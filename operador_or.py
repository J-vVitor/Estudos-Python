# SE QUALQUER CONDIÇÃO FOR VERDADEIRA O CÓDIGO SEGUE COM "TRUE", OU UMA CONDIÇÃO OU OUTRA.

entrada = input('[E]ntrar [S]air: ');

senha_permitida = '12345';

senha_do_usuario = input('Digite sua senha: ')

if entrada == 'E' or senha_do_usuario == senha_permitida:
    print('Você entrou no sistema!');
    
else:
    print('Você saiu do sistema!');
    
