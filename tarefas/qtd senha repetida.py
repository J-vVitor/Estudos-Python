senha_salva = '1234588'

qtd_vezes_senha_digitada = 0

campo_coletar_senha = input('Digite sua senha: ')

qtd_tentativas = 1

while campo_coletar_senha != senha_salva:
    
    repeticao_senha = input('Digite sua senha novamente: ')
    
    qtd_tentativas +=1
        
    print(f'Você ultilixou {qtd_tentativas} tentativas')
    
    
    break