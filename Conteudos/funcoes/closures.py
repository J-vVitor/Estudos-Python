# Método antigo

'''''
def saudacao(saudacao, nome_pessoa):
    return f'{saudacao},{nome_pessoa}!'


saudacao_de_bom_dia = saudacao('Bom dia', 'João')

saudacao_de_boa_noite = saudacao('Boa noite', 'João')

print(saudacao_de_bom_dia)
print(saudacao_de_boa_noite)

'''

# Novo método


def saudacao(saudacao, nome_da_pessoa):
    def saudar():
        return f'{saudacao},{nome_da_pessoa}!'

    return saudar


s1 = saudacao('Boa noite', 'João')

print(s1())


def saudacao(saudacao):
    def saudar(nome_da_pessoa):
        return f'{saudacao},{nome_da_pessoa}!'

    return saudar


s1 = saudacao('Boa noite')

print(s1('João'))
