import random
import pygame

from minigames_pygame.precisao_minigame.classes.outros import*


def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )   

class Inicialize_minigame():
    def __init__(self):
        self.name = "Inicialize_minigame"
        self.assets = {
            "fonte_24": pygame.font.Font( pygame.font.get_default_font(), 24)
        }
        

    def draw(self, window, state):
        window.fill((50,50,50))
        
        window.blit(state["tela_inicial"], (0,0))

        pygame.display.update()
        

    def update_events(self, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "Minigame4"


class Minigame4:
    def __init__(self, state):
        self.name = "Minigame4"
        self.precision_sound = pygame.mixer.Sound('assets/sons/precisao.mp3')

        self.assets = {
            "fonte_30": pygame.font.Font( pygame.font.get_default_font(), 30)
        }
            
        self.last_updated = 0
        
        self.barra = Barra()



    def draw(self, window, state):

        window.blit(state["game_screen"], (0,0))    

        gradientRect( window, (0, 220, 0), (255, 255, 0), pygame.Rect( 320,240, 50, 240 ) )
        gradientRect( window, (255, 255, 0), (0, 220, 0), pygame.Rect( 270,240, 50, 240 ) )
        
        gradientRect( window, (255, 255, 0), (255, 0, 0) , pygame.Rect( 370,240, 150, 240 ) )
        gradientRect( window,  (255, 0, 0), (255, 255, 0), pygame.Rect( 120,240, 150, 240 ) )
        
        gradientRect( window, (50,0, 50), (255, 0, 0), pygame.Rect( 0,240, 120, 240 ) )
        gradientRect( window, (255, 0, 0), (50,0,50),  pygame.Rect( 520,240, 120, 240 ) )

        
        pygame.draw.rect(window, self.barra.cor, pygame.Rect([self.barra.x, self.barra.y], [self.barra.w, self.barra.h]))
        
        
        pygame.display.update()


    def update_events(self, state):
    
        for ev in pygame.event.get():
    
            if ev.type == pygame.QUIT:
                return "quit"

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                pygame.mixer.Channel(4).play(self.precision_sound)
                
                self.barra.vx = 0
                state["distance_from_green"] = float(f"{abs((self.barra.x + self.barra.w/2) - 320):.3f}")
                
                return "Finalize_minigame"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                self.barra.vx = 400
                
        ticks = pygame.time.get_ticks()

        self.barra.mover(self.last_updated, ticks)
        self.last_updated = ticks


        
        return True


            


class Finalize_minigame():
    def __init__(self):
        self.name = "Finalize_minigame"
        
        self.assets = {
            "fonte_30": pygame.font.Font( pygame.font.get_default_font(), 30)
        }
        
    def draw(self, window, state):
        window.fill((255,255,255))
        
        texto1 = self.assets["fonte_30"].render(f'{state["distance_from_green"]}',  True, (0, 0, 0))

        window.blit(state["tela_final"], (0,0))
        window.blit(texto1, (390,228))

        pygame.display.update()
        

    def update_events(self, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "quit"
            