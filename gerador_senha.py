def gera_senha():
	from random import randint, choice
	numeros = '0123456789'
	letras = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
	simbolos = '!@#$%&*+?'
	senha = ''
	escolhas = {1: numeros, 2: letras, 3: simbolos}
	numero_digitos = int(raw_input('Quantidade de digitos: '))

	for i in range(numero_digitos):
		senha += choice(escolhas[randint(1, 3)])

	print senha

gera_senha()