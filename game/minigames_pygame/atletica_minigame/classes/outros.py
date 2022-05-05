'''
Esse módulo é responsável pelas funções e classes restantes que são utilizadas na lógica do
minigame 2 (Atléticas)
'''


import random
import pygame


class Meteoro:
    '''
    Classe Metoro:
    - Objetos que tentam atingir o jogador durante o minigame
    - Representados pelas imagens das atléticas de outras faculdades
    '''
    def __init__(self, image):
        '''
        Inicializa todas as variáveis necessárias

        image --> imagem png da atlética que será usada no objeto
        '''
        self.x = random.randint(-10,540 )
        self.y = -500
        
        self.vy = random.randint(300, 500)

        img = pygame.transform.smoothscale(image, (100, 100)) 
        
        self.image = img


    def atualiza_posicao(self, novo_y):
        '''
        Função atualiza a posição do objeto pela tela
        '''
        
        if novo_y > 480:
            #se saiu da tela, o coloca no topo em uma coordenada aleatória
            self.y = -500
            self.x = random.randint(-10,540 )
            self.vy = random.randint(300, 500)

        else:
            self.y = novo_y
    
    def confere_se_colidiu(self, nave_pos):
        '''
        Função cofere se o objeto colidiu com o jogador

        nave_pos -> tupla com par de coordenadas do jogador na tela
        '''

        infos_meteoro = pygame.rect.Rect(self.x + 49, self.y + 49, 2, 2)

        x_nave, y_nave = nave_pos
        infos_nave = pygame.rect.Rect(x_nave + 30, y_nave+ 30 , 40, 40)
        
        return pygame.Rect.colliderect(infos_meteoro, infos_nave)
        
    

class Nave:
    '''
    Classe Nave:
    - Objeto que representa o jogador no minigame
    '''
    def __init__(self, posicao, image):
        '''
        Inicializa todas as variáveis necessárias (posição e sprite utilizado)

        posicao -> tupla com par de coordenadas de onde o jogador estará
        image -> sprite utilizado para o jogador
        '''
        
        self.posicao = posicao
        img = pygame.transform.smoothscale(image, (100, 100)) 
        self.image = img
    
    def atualiza_posicao(self, nova_posicao):
        '''
        Método atualiza a posição do jogador

        nova_posicao -> tupla com par de novas coordenadas do jogador na tela
        '''

        #previne exploit de ficar no cantinho para desviar de todos as atléticas
        if nova_posicao[0] > 630 - 100:
            self.posicao = (630 - 100, nova_posicao[1])
        elif nova_posicao[0] < 10:
            self.posicao = (10, nova_posicao[1])
        else:
            self.posicao = nova_posicao