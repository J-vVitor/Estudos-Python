# OPERADOR "AND" - SE UM OPERAÇÃO FOR CONSIDERADA "FALSA", O CÓDIGO COMPLETO É CONSIDERADO "FALSO".

entrada = input('[E]ntrar [S]air: ');

senha_permitida = '12345';

senha_do_usuario = input('Digite sua senha: ')

if entrada == 'E' and senha_do_usuario == senha_permitida:
    print('Você entrou no sistema!');
    
else:
    print('Você saiu do sistema!');
    
