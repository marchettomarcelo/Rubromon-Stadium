'''
Esse módulo é responsável pelas classes de todas as telas utilizadas no Minigame2 (Atléticas)
'''

import pygame
import random
from minigames_pygame.atletica_minigame.classes.outros import *


class Iniciar_minigame():
    '''
    Classe Iniciar_Minigame:
    - Tela de apresentação do minigame com suas regras
    '''
    def __init__(self):
        '''
        Inicializa todas as variáveis necessárias
        '''
        self.name = "Iniciar_minigame"
        
    
    def draw(self, window, screens):
        '''
        Função desenha tela de início do minigame
        '''
        window.blit(screens["tela_inicial"], (0,0))  
        pygame.display.update()
        

    def update_events(self, screens):
        '''
        Função cura os eventos de entrada do jogador na tela inicial e a atualiza

        screens -> variável armazena as variáveis principais do minigame
        '''
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "Minigame2"

class Finalizar_minigame():
    '''
    Classe Finalizar_Minigame:
    - Tela de finalização do minigame que apresenta a pontuação do jogador
    '''
    def __init__(self):
        '''
        Inicializa todas as variáveis necessárias (nome da tela, assets)
        '''
        self.name = "Finalizar_minigame"
        
        self.assets = {
            "fonte_30": pygame.font.Font( pygame.font.get_default_font(), 30)
        }
        
    def draw(self, window, screens):
        '''
        Desenha a tela de finalização do minigame com as atualizações

        window -> armazena a tela do pygame
        screens -> dicionário com todas as informações gerais do minigame
        '''
        window.blit(screens["tela_final"], (0,0))  
        
    
        texto1 = self.assets["fonte_30"].render(f'{screens["time"]} ',  True, (255, 255, 255))

        window.blit(texto1, (390,228))

        pygame.display.update()
        

    def update_events(self, screens):
        '''
        Função cura os eventos de entrada do jogador na tela final e a atualiza

        screens -> variável armazena as variáveis principais do minigame
        '''
        for ev in pygame.event.get():
            #fecha o minigame
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "quit"


class Minigame2():
    '''
    Classe Minigame:
    - Tela do minigame em si, com a lógica principal dos "meteoros" e do jogador
    '''
    def __init__(self):
        '''
        Inicializa todas as variáveis necessárias (imagens, "meteoros", "nave")

        meteoros -> ícones das atléticas que o jogador precisa desviar
        nave -> ícone do jogador
        '''
        fgv_meteoro = pygame.image.load("assets/atleticas/fgv.png")
        espm_meteoro = pygame.image.load("assets/atleticas/espm.png")
        puc_meteoro = pygame.image.load("assets/atleticas/puc.png")
        fea_meteoro = pygame.image.load("assets/atleticas/fea.png")
        mack_meteoro = pygame.image.load("assets/atleticas/mack.png")
        fecap_meteoro = pygame.image.load("assets/atleticas/fecap.png")
        
        n_meteoros = []

        #inicializa os obstáculos
        for atletica in [fgv_meteoro, espm_meteoro, puc_meteoro, fea_meteoro, mack_meteoro, fecap_meteoro] :

            for n in range(3):
                
                n_meteoros.append( Meteoro( atletica) )
            

        self.n_meteoros = n_meteoros

        self.nave = Nave((200, 400), pygame.image.load("assets/atleticas/raposa.png"))

        self.assets = {
            "fonte_24": pygame.font.Font( pygame.font.get_default_font(), 24)
        }
        self.name = "Minigame2"
        self.quando_iniciou = pygame.time.get_ticks()
        self.last_updated = 0


    def draw(self, window, screens):
        '''
        Desenha a tela do minigame com jogador e inimigos

        window -> armazena a tela do pygame
        screens -> dicionário com todas as informações gerais do minigame
        '''

        window.blit(screens["game_screen"], (0,0))  

       
        window.blit(self.nave.image, self.nave.posicao)
        
        for meteoro in self.n_meteoros:
            window.blit(meteoro.image, (meteoro.x, meteoro.y))

        pygame.display.update()


    def update_events(self, screens):
        '''
        Função cura os eventos de entrada do jogador na tela de minigame e a atualiza

        screens -> variável armazena as variáveis principais do minigame
        '''

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
        
            if ev.type == pygame.MOUSEMOTION:
                x, y = ev.pos
                self.nave.atualiza_posicao((x-50, y-50)) 
        

        ultimo_update = self.last_updated
        self.last_updated = pygame.time.get_ticks()
        
        delta_t = self.last_updated - ultimo_update
        
        #checa se jogador foi atingido por algum dos obstáculos
        for meteoro in self.n_meteoros:
            novo_y = meteoro.y + delta_t * (meteoro.vy/1000)
            meteoro.atualiza_posicao(novo_y)
            
            if meteoro.confere_se_colidiu(self.nave.posicao):
                
                screens["time"] = (pygame.time.get_ticks() - self.quando_iniciou)/1000
                return "Finalizar_minigame"
                
        return True