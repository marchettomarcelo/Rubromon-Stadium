import random
import pygame

class Inicialize_minigame():
    def __init__(self):
        self.name = "Inicialize_minigame"
        
    
    def draw(self, window, state):
        window.blit(state["fundo"], (0,0))
        pygame.display.update()
        

    def update_events(self, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "Minigame1"

class Finalize_minigame():
    def __init__(self):
        self.name = "Finalize_minigame"
        
        self.assets = {
            "fonte_30": pygame.font.Font( pygame.font.get_default_font(), 30)
        }
        
    def draw(self, window, state):
        window.fill((255,255,255))
        
        texto2 = self.assets["fonte_30"].render(f'{state["tempo"]}',  True, (255, 255, 255))
        
        window.blit(state["fundo2"], (0,0))

        window.blit(texto2, (390,228))

        pygame.display.update()
        

    def update_events(self, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return "quit"




class Minigame1:
    def __init__(self):
        self.correct_word_sound = pygame.mixer.Sound('assets/sons/palavra_certa.mp3')

        self.assets = {
            "fonte_24": pygame.font.Font( pygame.font.get_default_font(), 24)
        }
        
        banco_palavras = [ 'bateu',  'pouco', 'coajo', 'azedo', 'emite', 'negou', 'moera', 'anelo', 'pilar', 'abras', 'deito', 
        'regra', 'gemas', 'pomos', 'dente', 'vivem', 'orlou', 'tonto', 'dogma', 'rezes', 'canse','menta', 'domou', 'cisne'
        , 'ameno', 'surdo', 'ulula', 'fenda','bolam', 'zango', 'lerdo', 'ulula', 'rendi', 'ruela', 'caiba', 'fazem']

        sorteadas = []

        for i in range(3):
            sorteadas.append(banco_palavras[random.randint(0,len(banco_palavras) -1)] )

        self.palavras_sorteadas = sorteadas
        self.indice_palavras_sorteadas = 0

        self.name = "Minigame1"
        self.last_click = 0
        self.last_character_id = " "
        self.palavra_sendo_escrita = ""

        self.quando_iniciou = pygame.time.get_ticks()

        self.backspace_clicked = False

        


    def draw(self, window, state):

        window.fill((0, 0, 0))

        texto1 = self.assets["fonte_24"].render(f"Digite as seguintes palavras, em sequência,", True, (255, 255, 255))
        texto2 = self.assets["fonte_24"].render(f"o mais rápido possível!", True, (255,255, 255))

        palavra1 = self.assets["fonte_24"].render(f"{self.palavras_sorteadas[0]},", True, (50, 131, 168))
        palavra2 = self.assets["fonte_24"].render(f"{self.palavras_sorteadas[1]},", True, (50, 131, 168))
        palavra3 = self.assets["fonte_24"].render(f"{self.palavras_sorteadas[2]},", True, (50, 131, 168))

        if self.indice_palavras_sorteadas == 1:
            palavra1 = self.assets["fonte_24"].render(f"{self.palavras_sorteadas[0]},", True, (0, 131, 0))
       
        if self.indice_palavras_sorteadas == 2:
            palavra1 = self.assets["fonte_24"].render(f"{self.palavras_sorteadas[0]},", True, (0, 131, 0))
            palavra2 = self.assets["fonte_24"].render(f"{self.palavras_sorteadas[1]},", True, (0, 131, 0))
        

        
        escrevendo = self.assets["fonte_24"].render(f"{self.palavra_sendo_escrita}", True, (150, 255, 0))

        window.blit(texto1, (10,20))
        window.blit(texto2, (10,50))

        window.blit(palavra1, (10,100))
        window.blit(palavra2, (110,100))
        window.blit(palavra3, (210,100))
        
        window.blit(escrevendo, (10,200))


        pygame.display.update()


    def update_events(self, state):
        letras = [
            pygame.K_a,     
            pygame.K_b,     
            pygame.K_c,    
            pygame.K_d,    
            pygame.K_e, 
            pygame.K_f,   
            pygame.K_g,    
            pygame.K_h,    
            pygame.K_i,    
            pygame.K_j,    
            pygame.K_k,    
            pygame.K_l,    
            pygame.K_m,    
            pygame.K_n,    
            pygame.K_o,    
            pygame.K_p,    
            pygame.K_q,    
            pygame.K_r,    
            pygame.K_s,    
            pygame.K_t,    
            pygame.K_u,    
            pygame.K_v,    
            pygame.K_w,    
            pygame.K_x,    
            pygame.K_y,   
            pygame.K_z 
        ]

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                print(pygame.time.get_ticks())

                return "quit"
            
            if ev.type == pygame.KEYDOWN and ev.key in letras:
                
                if self.last_character_id != ev.key :
                    self.palavra_sendo_escrita += chr(ev.key)
                    self.last_character_id = ev.key

                    

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_BACKSPACE and self.backspace_clicked == False:
                self.backspace_clicked = True

                tamanho_palavra = len( self.palavra_sendo_escrita)
                if tamanho_palavra > 0:
                
                    self.palavra_sendo_escrita = self.palavra_sendo_escrita[:-1]

                    
            if ev.type == pygame.KEYUP and ev.key == pygame.K_BACKSPACE:
                self.backspace_clicked = False

            # if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:

            if self.palavra_sendo_escrita == self.palavras_sorteadas[self.indice_palavras_sorteadas]:
                pygame.mixer.Channel(4).play(self.correct_word_sound)
                self.palavra_sendo_escrita = ""
                
                if self.indice_palavras_sorteadas == 2:
                    
                    # print(f"Voce demorou {  (pygame.time.get_ticks() - self.quando_iniciou) /1000} segundos para teminar esse minigame!")
                    
                    state["tempo"] = (pygame.time.get_ticks() - self.quando_iniciou) /1000
                    return "Finalize_minigame"
                
                else:    
                    self.indice_palavras_sorteadas += 1
                
        return True
