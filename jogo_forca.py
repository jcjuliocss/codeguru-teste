from os import system


class Forca:
    def __init__(self, palavra, dica):
        self.palavra = palavra
        self.dica = dica
        self.tamanho_palavra = len(palavra)
        self.palavra_oculta = ['_ '] * self.tamanho_palavra
        for i in range(len(palavra)):
            if palavra[i] == ' ':
                self.palavra_oculta[i] = '  '
        self.str_palavra = ''
        self.conta_erros = 0
        self.derrota = False
        self.letras_digitadas = []

    def desenha(self, erros):
        self.str_palavra = ''
        for i in range(self.tamanho_palavra):
            self.str_palavra += self.palavra_oculta[i] + ' '

        if erros == 0:
            print r'''
             _____
            |     |
            |
            |
            |
           _|_
               '''
        elif erros == 1:
            print r'''
             _____
            |     |
            |     O
            |
            |
           _|_
               '''
        elif erros == 2:
            print r'''
             _____
            |     |
            |     O
            |     |
            |
           _|_
               '''
        elif erros == 3:
            print r'''
             _____
            |     |
            |     O
            |    /|
            |
           _|_
               '''
        elif erros == 4:
            print r'''
             _____
            |     |
            |     O
            |    /|\
            |
           _|_
               '''
        elif erros == 5:
            print r'''
             _____
            |     |
            |     O
            |    /|\
            |    /
           _|_
               '''
        else:
            self.derrota = True
            print r'''
             _____
            |     |
            |     O
            |    /|\
            |    / \
           _|_
               '''

        print self.str_palavra
        print 'Dica: ' + self.dica

    def checa_letra(self, letra):
        if str(letra) not in self.letras_digitadas:
            self.letras_digitadas.append(letra)
        if str(letra) in self.palavra:
            for i in range(self.tamanho_palavra):
                if self.palavra[i] == str(letra):
                    self.palavra_oculta[i] = '\033[32m' + letra + '\033[0;0m'
        else:
            self.conta_erros += 1


palavra = raw_input('Digite a palavra: ')
system('clear')
dica = raw_input('Digite a dica: ')
system('clear')

jogo = Forca(palavra, dica)
jogo.desenha(jogo.conta_erros)

while '_ ' in jogo.palavra_oculta and not jogo.derrota:
    print('Letras ja escolhidas: ' + str(jogo.letras_digitadas).replace('[', '').replace(']', '').replace('\'', ''))
    letra = raw_input('Digite uma letra: ')
    system('clear')
    jogo.checa_letra(letra)
    jogo.desenha(jogo.conta_erros)

if jogo.derrota:
    print 'Voce perdeu'
else:
    print 'Acerto miseravi'
