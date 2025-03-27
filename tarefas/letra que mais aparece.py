frase = 'A letraaaa que mais aparece'
i = 0

qtd_letra_apreceu = 0

letras_que_mais_apareceu = ''

while i < len(frase):
    qtd_letras = frase[i]
    
    qtd_letra_apareceu_atual = frase.count(qtd_letras)
    
    if qtd_letra_apreceu < qtd_letra_apareceu_atual:
        qtd_letra_apreceu = qtd_letra_apareceu_atual
        letras_que_mais_apareceu = qtd_letras

    i+=1
    
    print(letras_que_mais_apareceu)
    
    
    
