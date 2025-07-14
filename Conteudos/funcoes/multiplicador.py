# CRIAR UMA FUNÇÃO QUE MULTIPLICA, TRIPLICA E QUADRUPLICA O
# PARÂMETRO RECEBIDO

def multiplicacao(numero):

    def multiplicar(multiplicador):
        return numero * multiplicador

    return multiplicacao()


print(multiplicacao(4))
