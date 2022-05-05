import pygame

WIDTH = 640
HEIGHT = 480
FPS = 60

TITLE = "title"
QUIT = "quit"
RULES = "rules"
SELECT_CHARACTER = 'select_character'
BATTLE = "battle"
GAMEOVER = "game_over"

characters = {
            'Diabo Loiro' : {
                'hp': 1000,
                'skins' : [pygame.transform.scale(pygame.image.load("assets/sprites/marcos_perto.png"), (200, 200)), pygame.transform.scale(pygame.image.load("assets/sprites/marcos_longe.png"), (200, 200))], 
                'attacks' : ['Reforma Tributária', 'Bolsa de Estudos', 'Bomba de Descolorante', 'Menos Marx, Mais Marcos']
                }, 
            'Toshi Coxinha' : {
                'hp': 1000, 
                'skins' : [pygame.transform.scale(pygame.image.load("assets/sprites/toshi_perto.png"), (200, 200)), pygame.transform.scale(pygame.image.load("assets/sprites/toshi_longe.png"), (200, 200))], 
                'attacks' : ['Míssil de Coxinha', 'For Infinito', 'CSSoco', 'Heurística']
                }, 
            'Insper Boy' : {
                'hp': 1000, 
                'skins' : [pygame.transform.scale(pygame.image.load("assets/sprites/insperboy_perto.png"), (200, 200)), pygame.transform.scale(pygame.image.load("assets/sprites/insperboy_longe.png"), (200, 200))], 
                'attacks' : ['Névoa Mística', 'Trancrazy', 'Cascalho do Papi', 'Meinzinho']
                }, 
            'Raposa Loka' : {
                'hp': 1000, 
                'skins' : [pygame.transform.scale(pygame.image.load("assets/sprites/raposa_perto.png"), (300, 200)), pygame.transform.scale(pygame.image.load("assets/sprites/raposa_longe.png"), (200, 200))], 
                'attacks' : ['Nuvem Rubra', 'Soco 300', 'Rasteira Quatá', 'Terror do Alojas']
                }
        }