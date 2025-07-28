perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['4', '7', '8', '22'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5?',
        'Opções': ['15', '10', '25', '55'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 45x3?',
        'Opções': ['95', '120', '48', '135'],
        'Resposta': '135',
    }
]


qntd_acerto = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    qtd_opcoes = len(opcoes)

    # Opções de resposta para o usuário
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    # Resposta que usuário dá:
    resposta_usuario = input('Digite sua resposta: ')
    print()

    # Validação se o usuário digitou um número
    if resposta_usuario.isdigit():
        resposta_usu_int = int(resposta_usuario)

    if resposta_usu_int >= 0 and resposta_usuario == pergunta['Resposta']:
        print('Acertou')
