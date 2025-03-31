''' 
    JOGO DA PALAVRA SECRETA 
'''

palavra_secreta = 'comi'
palavra_concatenada = ''

while True:
    letra_digitada = input('Digite uma letra: ')
    
    # "LER" O TAMANHO DA VARIÁVEL "LETRA DIGITADA" E VER SE ELA FOR MAIOR QUE 1 
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!!!')
        continue
    
    # SE A LETRA DIGITA ESTIVER ENTRE A PALAVRA SECRETA, EXIBA A LETRA DIGITADA         
    if letra_digitada in palavra_secreta:
        palavra_concatenada += letra_digitada 
        
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavra_concatenada:
            print(letra_secreta)
            
        else:
            print('*')
            
            
        if letra_secreta == palavra_secreta:
            print('Finalizados')