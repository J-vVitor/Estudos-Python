nome = 'João Vitor'

i = 0

while i < len(nome):
    letras_do_nome = nome[i]
    print(letras_do_nome)
    
    if letras_do_nome == ' ':
        break
    i+=1