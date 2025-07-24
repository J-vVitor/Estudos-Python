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
        'Resposta': '25',
    }
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    # Opções de resposta para o usuário
    for i, opcoes in enumerate(pergunta['Opções']):
        print(f'{i})', opcoes)
    print()

    # Resposta do usuario
    resposta_usuario = input('Digite sua resposta: ')
    print()

    # Validação se o usuário digitou um número
    if resposta_usuario.isdigit():
        transform_int = int(resposta_usuario)

        print(type(transform_int))

    if transform_int <= len(pergunta['Opções']) and transform_int == pergunta['Opções']:
        print('Você acertou')
