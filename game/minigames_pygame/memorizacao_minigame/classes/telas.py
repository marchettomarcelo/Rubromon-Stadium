'''
Esse módulo é responsável pelas classes de todas as telas utilizadas no Minigame1 (Dory Decore)
'''

from minigames_pygame.memorizacao_minigame.classes.outros import*
import random
import pygame

            
class Iniciar_minigame():
    '''
    Classe Iniciar_Minigame:
    - Tela de apresentação do minigame com suas regras
    '''
    def __init__(self):
        '''
        Inicializa variáveis necessárias (nome da tela, assets)
        '''
        self.name = "Iniciar_minigame"
        self.assets = {
            "fonte_24": pygame.font.Font( pygame.font.get_default_font(), 24)
        }
        

    def draw(self, window, state):
        '''
        Função desenha tela de início do minigame

        window -> variável que armazena tela do pygame
        state -> dicionário com todas as variáveis principais do minigame
        '''
        window.fill((50,50,50))

        window.blit(state["tela_inicial"], (0,0))

        pygame.display.update()
        

    def update_events(self, state):
        '''
        Função cura os eventos de entrada do jogador na tela inicial e a atualiza

        state -> variável armazena as variáveis principais do minigame
        '''
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "Random_sequence"

class Random_sequence:
    '''
    Classe Sequência Aleatória:
    - classe da tela que apresenta ao jogador a sua sequência aleatória, junto com um timer para ele
      decorá-la e se preparar
    '''

    def __init__(self):
        '''
        Inicializa todas as variáveis necessárias para a tela (nome, assets, tempo)
        '''
        self.name = "Random_sequence"
        self.assets = {
            "fonte_70": pygame.font.Font( pygame.font.get_default_font(), 70),
            "fonte_24": pygame.font.Font( pygame.font.get_default_font(), 24)
        }
        self.quando_iniciou = pygame.time.get_ticks()
        self.time_to_memorize = 0
            
    def draw(self, window, state):
        '''
        Função desenha tela de preparo do minigame
        '''

        window.blit(state["tela_sequencia"], (0,0))

        texto1 = self.assets["fonte_70"].render(f'{ str(state["correct_sequence"])}', True, (255, 255, 255))

        self.time_to_memorize = (self.quando_iniciou + 5000 - pygame.time.get_ticks())/1000
        
        #para caso o tempo diminua abaixo de 0 acidentalmente
        if self.time_to_memorize < 0:
            self.time_to_memorize = 0

        texto2 = self.assets["fonte_24"].render( f'O jogo começará em: { self.time_to_memorize  } segundo.', True, (255, 255, 255))
        
        window.blit(texto1, (120,200))
        window.blit(texto2, (120,400))
        

        pygame.display.update()


    def update_events(self, state):
        '''
        Função cura os eventos de entrada do jogador na tela intermediária e a atualiza

        state -> variável armazena as variáveis principais do minigame
        '''
    
        for ev in pygame.event.get():
    
            if ev.type == pygame.QUIT:
                return "quit"
            
            #quando o tempo de memorização acaba
            if self.time_to_memorize == 0:
                return "Minigame3"

class Minigame3:
    '''
    Classe Minigame:
    - Tela do minigame em si, com a lógica principal das bolinhas em locais aleatórios
    '''
    def __init__(self, state):
        '''
        Inicializa todas as variáveis necessárias para a tela (nome, som, assets, tempo)
        '''
        self.name = "Minigame3"
        self.correct_click_sound = pygame.mixer.Sound('assets/sons/click_no_numero.mp3')

        self.assets = {
            "fonte_24": pygame.font.Font( pygame.font.get_default_font(), 24)
        }
            
        self.quando_iniciou = pygame.time.get_ticks()


        self.conjunto_bolinhas = []
        #cria lista com cinco bolinhas em lugares aleatórios
        for num in state["correct_sequence"]:

            x_aleatorio = random.randint(0, 640)
            y_aleatorio = random.randint(0, 480)

            self.conjunto_bolinhas.append( Bolinha(num, x_aleatorio, y_aleatorio, 20) )


    def draw(self, window, state):
        '''
        Desenha a tela do minigame com as bolinhas sorteadas e sua respectiva cor
           - vermelho: ainda não foi clicada
           - verde: já foi clicada com sucesso

        window -> armazena a tela do pygame
        state -> dicionário com todas as informações gerais do minigame
        '''

        window.fill((95, 95, 95))        

        #desenha cada bolinha
        for bola in self.conjunto_bolinhas:

            pygame.draw.circle(window, bola.cor, bola.centro, bola.raio)

            id_bolinha = self.assets["fonte_24"].render( str(bola.id_bolinha) , True, (0, 0, 0))

            window.blit(id_bolinha, (bola.x -7, bola.y -10 ))

        pygame.display.update()


    def update_events(self, state):
        '''
        Função cura os eventos de entrada do jogador na tela de minigame e atualiza as bolinhas

        state -> variável armazena as variáveis principais do minigame
        '''
    
        for ev in pygame.event.get():
    
            if ev.type == pygame.QUIT:
                return "quit"
            
            #para cada bolinha, checa se clicou na bola e se clicou na sequência correta
            for bola in self.conjunto_bolinhas:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                if bola.mouse_on_top(x_mouse, y_mouse): 
                    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                
                        if bola.id_bolinha == state["correct_sequence"][0] and len(state["correct_sequence"]) == 1:
                            pygame.mixer.Channel(4).play(self.correct_click_sound)
                            bola.cor = [0,250,0]
                            state["tempo"] = (pygame.time.get_ticks() - self.quando_iniciou) /1000
                            return "Finalizar_minigame"
                        
                        if bola.id_bolinha == state["correct_sequence"][0]: 
                            pygame.mixer.Channel(4).play(self.correct_click_sound)
                            bola.cor = [0,220,0]
                            del state["correct_sequence"][0]

        
        return True


class Finalizar_minigame():
    '''
    Classe Finalizar_Minigame:
    - Tela de finalização do minigame que apresenta a pontuação do jogador
    '''
    def __init__(self):
        '''
        Inicizaliza todas as variáveis necessárias para a tela (nome, assets)
        '''
        self.name = "Finalizar_minigame"
        
        self.assets = {
            "fonte_30": pygame.font.Font( pygame.font.get_default_font(), 30)
        }
        
    def draw(self, window, state):
        '''
        Desenha a tela de finalização do minigame com as atualizações

        window -> armazena a tela do pygame
        state -> dicionário com todas as informações gerais do minigame
        '''
        window.fill((255,255,255))
        
        window.blit(state["tela_final"], (0,0))
        
        texto1 = self.assets["fonte_30"].render(f'{state["tempo"]}',  True, (255, 255, 255))
        
        window.blit(state["tela_final"], (0,0))

        window.blit(texto1, (390,228))
    
        
        pygame.display.update()
        

    def update_events(self, state):
        '''
        Função cura os eventos de entrada do jogador na tela final e a atualiza

        state -> variável armazena as variáveis principais do minigame
        '''
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                
                return "quit"