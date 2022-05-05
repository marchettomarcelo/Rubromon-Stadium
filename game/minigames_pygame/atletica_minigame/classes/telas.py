import pygame
import random
from minigames_pygame.atletica_minigame.classes.outros import *

class Iniciar_minigame():
    def __init__(self):
        self.name = "Iniciar_minigame"
        
    
    def draw(self, window, state):
        window.blit(state["tela_inicial"], (0,0))  
        pygame.display.update()
        

    def update_events(self, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "Minigame2"

class Finalizar_minigame():
    def __init__(self):
        self.name = "Finalizar_minigame"
        
        self.assets = {
            "fonte_30": pygame.font.Font( pygame.font.get_default_font(), 30)
        }
        
    def draw(self, window, state):
        window.blit(state["tela_final"], (0,0))  
        
    
        texto1 = self.assets["fonte_30"].render(f'{state["tempo"]} ',  True, (255, 255, 255))

        window.blit(texto1, (390,228))

        pygame.display.update()
        

    def update_events(self, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "quit"


class Minigame2():
    def __init__(self):

        fgv_meteoro = pygame.image.load("assets/atleticas/fgv.png")
        espm_meteoro = pygame.image.load("assets/atleticas/espm.png")
        puc_meteoro = pygame.image.load("assets/atleticas/puc.png")
        fea_meteoro = pygame.image.load("assets/atleticas/fea.png")
        mack_meteoro = pygame.image.load("assets/atleticas/mack.png")
        fecap_meteoro = pygame.image.load("assets/atleticas/fecap.png")
        
        n_meteoros = []

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


    def draw(self, window, state):

        window.blit(state["game_screen"], (0,0))  

       
        window.blit(self.nave.image, self.nave.posicao)
        
        for meteoro in self.n_meteoros:
            window.blit(meteoro.image, (meteoro.x, meteoro.y))

        pygame.display.update()


    def update_events(self, state):

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
        
            if ev.type == pygame.MOUSEMOTION:
                x, y = ev.pos
                self.nave.atualiza_posicao((x-50, y-50)) 
        

        ultimo_update = self.last_updated
        self.last_updated = pygame.time.get_ticks()
        
        delta_t = self.last_updated - ultimo_update
        
        for meteoro in self.n_meteoros:
            novo_y = meteoro.y + delta_t * (meteoro.vy/1000)
            meteoro.atualiza_posicao(novo_y)
            
            if meteoro.confere_se_colidiu(self.nave.posicao):
                
                state["tempo"] = (pygame.time.get_ticks() - self.quando_iniciou)/1000
                return "Finalizar_minigame"
                
        return True