contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 10:
        print('Não vou exibir o número 10')
        continue
        #CONTIUE SERVE PARA SEGUIR COM FLUXO
    
    print(contador)
       
    if contador == 30:
        break
    