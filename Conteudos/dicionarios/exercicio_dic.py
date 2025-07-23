perguntas = [
    {
        'Pergunta': 'Quanto é 4+4:',
        'Opções': ['4', '8', '16', '44'],
        'Resposta': '8'
    }
]

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])

    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)

    print()

    valor_resposta = input('Escolha uma opção: ')
