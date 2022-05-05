'''
Esse módulo é responsável pelas classes de todas as telas utilizadas no Minigame RataType
'''

import random
import pygame


class Inicialize_minigame():
    '''
    Classe Iniciar_Minigame:
    - Tela de apresentação do minigame com suas regras
    '''
    def __init__(self):
        '''
        Inicializa variáveis necessárias (no caso, apenas o nome da tela)
        '''
        self.name = "Inicialize_minigame"
        
    
    def draw(self, window, state):
        '''
        Função desenha tela de início do minigame
        '''
        window.blit(state["fundo"], (0,0))
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
                return "Minigame1"

class Finalize_minigame():
    '''
    Classe Finalizar_Minigame:
    - Tela de finalização do minigame que apresenta a pontuação do jogador
    '''
    def __init__(self):
        '''
        Inicializa variáveis necessárias para funcionamento da tela (nome da tela, assets)
        '''
        self.name = "Finalize_minigame"
        
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
        
        texto2 = self.assets["fonte_30"].render(f'{state["tempo"]}',  True, (255, 255, 255))
        
        window.blit(state["fundo2"], (0,0))

        window.blit(texto2, (390,228))

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




class Minigame1:
    '''
    Classe Minigame:
    - Tela do minigame em si, com a lógica principal da digitação das palavras aleatórias
    '''
    def __init__(self):
        '''
        Inicializa todas as variáveis necessárias (imagens, sons, lista de palavras aleatórias)
        '''
        self.correct_word_sound = pygame.mixer.Sound('assets/sons/palavra_certa.mp3')

        self.assets = {
            "fonte_24": pygame.font.Font( pygame.font.get_default_font(), 24)
        }
        
        banco_palavras = [ 'bateu',  'pouco', 'coajo', 'azedo', 'emite', 'negou', 'moera', 'anelo', 'pilar', 'abras', 'deito', 
        'regra', 'gemas', 'pomos', 'dente', 'vivem', 'orlou', 'tonto', 'dogma', 'rezes', 'canse','menta', 'domou', 'cisne'
        , 'ameno', 'surdo', 'ulula', 'fenda','bolam', 'zango', 'lerdo', 'ulula', 'rendi', 'ruela', 'caiba', 'fazem']

        sorteadas = []

        #sorteia 3 palavras do banco 
        for i in range(3):
            sorteadas.append(banco_palavras[random.randint(0,len(banco_palavras) -1)] )

        self.palavras_sorteadas = sorteadas
        self.indice_palavras_sorteadas = 0

        self.name = "Minigame1"

        #informações para tecla digitada
        self.last_click = 0
        self.last_character_id = " "
        self.palavra_sendo_escrita = ""

        self.quando_iniciou = pygame.time.get_ticks()

        self.backspace_clicked = False

        
    def draw(self, window, state):
        '''
        Desenha a tela do minigame com as palavras sorteadas de acordo com cor
           - branca: ainda a ser digitada
           - verde: já foi digitada com sucessp

        window -> armazena a tela do pygame
        state -> dicionário com todas as informações gerais do minigame
        '''

        window.fill((0, 0, 0))

        texto1 = self.assets["fonte_24"].render(f"Digite as seguintes palavras, em sequência,", True, (255, 255, 255))
        texto2 = self.assets["fonte_24"].render(f"o mais rápido possível!", True, (255,255, 255))

        #palavras sorteadas
        #de acordo com o índice da palavra que está sendo digitada, as anteriores precisam ser verdes!
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
        '''
        Função cura os eventos de entrada do jogador na tela de minigame e atualiza as palavras

        state -> variável armazena as variáveis principais do minigame
        '''

        #lista de todas as letras que o jogador pode inputar no teclado
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
                
                #usando o id do último char digitado, impede que o usuário digite o mesmo duas veze
                # seguidas
                if self.last_character_id != ev.key :
                    self.palavra_sendo_escrita += chr(ev.key)
                    self.last_character_id = ev.key

                    
            #apaga a última letra
            # tag backspace_clicked impede que o jogador segure o botão sem querer e apague tudo
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_BACKSPACE and self.backspace_clicked == False:
                self.backspace_clicked = True

                tamanho_palavra = len( self.palavra_sendo_escrita)
                if tamanho_palavra > 0:
                
                    self.palavra_sendo_escrita = self.palavra_sendo_escrita[:-1]

                    
            if ev.type == pygame.KEYUP and ev.key == pygame.K_BACKSPACE:
                self.backspace_clicked = False

            #quando o jogador termina de digitar a palavra corretamente, atualiza para a próxima
            if self.palavra_sendo_escrita == self.palavras_sorteadas[self.indice_palavras_sorteadas]:
                pygame.mixer.Channel(4).play(self.correct_word_sound)
                self.palavra_sendo_escrita = ""
                
                #finaliza se as 3 palavras forem digitadas
                if self.indice_palavras_sorteadas == 2:
                    state["tempo"] = (pygame.time.get_ticks() - self.quando_iniciou) /1000
                    return "Finalize_minigame"
                
                else:    
                    self.indice_palavras_sorteadas += 1
                
        return True