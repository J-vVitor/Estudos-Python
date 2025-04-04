"""
    ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
    SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MUTADO.
    A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.
"""

limite_de_velocidade = 80;
valor_da_multa = 7;

velocidade_recebida = input('Qual a velocidade do carro(km):');

velocidade_convertida = int(velocidade_recebida)

if velocidade_convertida > 80:
    print('Você foi multado!')
    print(f'Você terá que pagar um multa de R${valor_da_multa *(velocidade_convertida - limite_de_velocidade)}')
    
else:
    print('Você está no limite de velocidade')

print(4/2)


