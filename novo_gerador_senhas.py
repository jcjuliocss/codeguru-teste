from random import choice

def gera_senha(n):
    alfabeto = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    alfabeto += '!@#$%&*+?0123456789'
    senha = ''

    for i in range(n):
        senha += choice(alfabeto)

    return senha

n = int(raw_input('Quantidade de digitos: '))

print gera_senha(n)
