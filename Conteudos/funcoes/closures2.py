# CRIAR UMA FUNÇÃO QUE FAZ A SAUDAÇÃO " DENTRO DE UMA LISTA"


lista_de_nome = ['João', 'Maria', 'Luiza', 'Larrisa', 'Mikarla']


def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


s1 = saudacao('Bom dia')

for nomes in lista_de_nome:

    print(s1(nomes))
