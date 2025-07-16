# CRIAR UMA FUNÇÃO QUE MULTIPLICA, TRIPLICA E QUADRUPLICA O PARÂMETRO RECEBIDO

'''''

def multiplicacao(numero):
    def multiplicador():
        return f'{numero} x 2 = {numero * 2} ,\
    {numero} x 3 = {numero * 3} , {numero} x 4 = {numero * 4}'
    return multiplicador


numero_recebido = multiplicacao(4)

print(numero_recebido())

'''


def multiplicacao(numero):
    def multiplicar(multiplicador):
        return numero * multiplicador

    return multiplicar


n1 = multiplicacao(4)

print(n1(2))
print(n1(3))
print(n1(4))
