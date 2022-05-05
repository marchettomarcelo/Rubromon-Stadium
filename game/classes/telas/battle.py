'''
Esse módulo é responsável pela lógica de toda a batalha do jogo    
'''

import pygame
from global_vars import *
from minigames_pygame.atletica_minigame.main import *
from minigames_pygame.digitar_rapido_minigame.main import *
from minigames_pygame.memorizacao_minigame.main import *
from minigames_pygame.precisao_minigame.main import *

class Battle:
    '''
    Classe Batalha:
    - Tela de batalha de turnos dos personagens do jogo
    '''
    def __init__(self, player1, player2):
        '''
        - Inicia todas as variáveis necessárias da tela (jogadores, assets, barras de hp, etc.)

        player1 -> str de nome do personagem do jogador 1
        player2 -> str de nome do personagem do jogador 2
        '''
        self.name = BATTLE
        self.player1 = player1
        self.player2 = player2

        self.velp1 = 50
        self.velp2 = -50
        
        self.assets = {
            'font_20' : pygame.font.Font(pygame.font.get_default_font(), 20),
            'font_12' : pygame.font.Font(pygame.font.get_default_font(), 12),
            'font_30' : pygame.font.Font(pygame.font.get_default_font(), 30),
            'background' : pygame.image.load("assets/backgrounds/classroom.png"),
            'player1_skin' : characters[player1]['skins'][0],
            'player2_skin' : characters[player2]['skins'][1],
            'battle_border' : pygame.image.load("assets/sprites/Battle_BorderJPG.jpg"),
            'attack_colors' : pygame.image.load('assets/sprites/attack_colors.png'),
            'hp_bar' : pygame.image.load("assets/sprites/hp_bar.png"),
            'click_sound' : pygame.mixer.Sound('assets/sons/click_sound.mp3')
            }
        
        #Utiliza a classe de barra de vida para ambos jogadores
        self.hp_bars = {
            player2 : HpBar(characters[player1]['hp'], WIDTH/40 + 90, 48),
            player1 : HpBar(characters[player2]['hp'], 2*WIDTH/3 + 90, 2*HEIGHT/3 - 52)
        }
        self.damage = 0

        self.coords = {
            'player1_x' : 630,
            'player1_y' : 120,
            'player2_x' : -200,
            'player2_y' : 20
        }

        self.last_updated = pygame.time.get_ticks()

        #variáveis para impedir repetição de tecla e rodar animação dos jogadores 
        self.clicked_key = False
        self.out_of_position = True

        #menus de cada jogador
        self.menus_list = {
            '<- Back' : {player1 : ['Fight', 'Item', 'Run'], player2 : ['Fight', 'Item', 'Run']},
            'Fight' : {player1 : characters[player1]['attacks'], player2 : characters[player2]['attacks']},
            'Item' : {player1 : ['It was a joke', 'There are no items', 'Go KICK HIM!', '<- Back'], player2 : ['It was a joke', 'There are no items', 'Go KICK HIM!', '<- Back']},
            'Run' : {player1 : ["You can't run!", "What are you doing?", "Go fight.", '<- Back'], player2 : ["You can't run!", "What are you doing?", "Go fight.", '<- Back']}
        }
        self.player_attacking = self.player1

        self.text_index = 0
        self.current_menu = '<- Back'
        self.current_item = 0
        self.menu = self.menus_list[self.current_menu][self.player_attacking]

    def update_events(self, screens, window):
        '''
        Função atualiza eventos:
        - Trata todos os eventos de entrada do usuário e determina a próxima ação na batalha

        screens -> dicionário com todas as telas e variáveis principais (resultado da batalha, etc.)
        window -> variável que armazena a janela do jogo
        '''

        for player, bar in self.hp_bars.items():
            if bar.check_ending():
                screens['result'] = player
                return GAMEOVER

        self.menu = self.menus_list[self.current_menu][self.player_attacking]


        self.ticks = pygame.time.get_ticks()
        delta_t = (self.ticks - self.last_updated)/1000

        #se está fora de posição, move os players para o centro
        if self.out_of_position:
            self.coords['player1_x'] = self.coords['player1_x'] - 200 * delta_t
            self.coords['player2_x'] = self.coords['player2_x'] + 200 * delta_t

            if self.coords['player1_x'] <= 75 or self.coords['player2_x'] >= 390:
                self.coords['player_x'] = 75
                self.coords['player2_x'] = 390
                self.out_of_position = False

        #animação normal do jogo de movimentação natural
        else:
            self.coords['player1_x'] = self.coords['player1_x'] + self.velp1 * delta_t
            self.coords['player2_x'] = self.coords['player2_x'] + self.velp2 * delta_t

            if self.coords['player2_x'] >= 450 or self.coords['player2_x'] <= 390:
                self.coords['player1_x'] = self.coords['player1_x'] - self.velp1 * delta_t
                self.coords['player2_x'] = self.coords['player2_x'] - self.velp2 * delta_t
                self.velp1 *= -1
                self.velp2 *= -1

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT

            if ev.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            if ev.type == pygame.KEYDOWN and not self.clicked_key:
                self.clicked_key = True
                if ev.key == pygame.K_SPACE or ev.key == pygame.K_RETURN:
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    self.current_menu = self.menu[self.current_item]

                    #checa em qual menu você clicou ENTER
                    if self.current_menu in ['<- Back', "You can't run!", "What are you doing?", "Go fight.", 'It was a joke', 'There are no items', 'Go KICK HIM!']:
                        self.current_menu = '<- Back'
                        self.current_item = 0
                    elif self.current_menu in characters[self.player_attacking]['attacks'] and self.current_menu != "<- Back":
                        self.attack(window, self.current_item)
                        self.hp_bars[self.player_attacking].update_hp(self.damage)
                        self.current_menu = '<- Back'
                        self.current_item = 0
                        if self.player_attacking == self.player1:
                            self.player_attacking = self.player2
                        else:
                            self.player_attacking = self.player1

                #movimentação de menu            
                if ev.key == pygame.K_UP:
                    self.current_item -= 1
                    if self.current_item < 0:
                        self.current_item = len(self.menu) - 1
                if ev.key == pygame.K_DOWN:
                    self.current_item += 1
                    if self.current_item >= len(self.menu):
                        self.current_item = 0
                if ev.key == pygame.K_ESCAPE and self.current_menu != '<- Back':
                    self.current_menu = '<- Back'
            
            if ev.type == pygame.KEYUP:
                self.clicked_key = False


        self.last_updated = self.ticks
        return self.name

    def draw(self, window):
        '''
        Função desenha:
        - De acordo com o evento da batalha, desenha na tela os personagens, os menus, a vida, etc.
        
        window -> variável que armazena a janela do pygame
        '''
        window.fill((0, 0, 0))

        window.blit(self.assets['background'], (0, -160))
        window.blit(self.assets['battle_border'], (0, 320) )


        #desenhos os personagens em suas posições e o texto correspondente
        window.blit(self.assets['player2_skin'], (self.coords['player2_x'], self.coords['player2_y']))
        window.blit(self.assets['player1_skin'], (self.coords['player1_x'], self.coords['player1_y']))
        if self.out_of_position:
            window.blit(self.assets['font_30'].render(f"{self.player2} wants to battle!", True, (0, 0, 0)), (30, 2*HEIGHT/3 + HEIGHT/7))

        else:
            #desenha o menu de seleção
            for i in range(len(self.menu)):
                text = self.menu[i]
                if i == self.current_item:
                    text = '> ' + text
                else:
                    text = '  ' + text
                
                text_image = self.assets['font_20'].render(text, True, (0, 0, 0))
                window.blit(text_image, (30, 347 + i * 30))

            #desenha as bordas das barras de HP
            window.blit(self.assets['hp_bar'], (WIDTH/40, 40))
            window.blit(self.assets['hp_bar'], (2*WIDTH/3, 2*HEIGHT/3 - 60))

            #guia de minigames para cada ataque
            if self.current_menu == "Fight":
                window.blit(self.assets['attack_colors'], (0, 0))

            #desenha barras de vida
            for bar in self.hp_bars.values():
                bar.draw_hp(window)
            
            window.blit(self.assets['font_20'].render(f"Attacker:", True, (0, 0, 0)), (400, 347))
            window.blit(self.assets['font_20'].render(f"{self.player_attacking}", True, (0, 0, 0)), (400, 377))

        pygame.display.update()
    
    def attack(self, window, attack):
        '''
        Função de ataque:
        - De acordo com o ataque escolhido pelo jogador, roda minigame, recolhe as pontuações
          dos dois jogadores e calcula o dano com multiplicador.

        window -> variável que armazena a janela do pygame
        attack -> integer que representa o index do ataque escolhido (0, 1, 2 ou 3)
        '''
        points = [0, 0]
        attacks = [run_minigame1, run_minigame2, run_minigame3, run_minigame4]

        #roda o minigame de ataque uma vez por jogador e guarda na lista de pontuação
        for player in range(2):
            points[player] = attacks[attack](window)

        #calcula o dano de acordo com a lógica de cada minigame
        if attack == 1:
            self.damage = 200 * points[0]/points[1]
        elif attack == 4:
            self.damage = 150 * points[1]/points[0]
        else:
            self.damage = 200 * points[1]/points[0]
        
        #cap de dano máximo
        if self.damage > 300:
            self.damage = 300



class HpBar():
    '''
    Classe HP:
    - Barra de HP de cada jogador durante a batalha
    '''
    def __init__(self, hp, coordx, coordy):
        '''
        - Inicializa a barra de vida com o seu comprimento relacionado com a quantidade de vida

        hp --> quantidade de pontos de vida do jogador
        coordx --> coordenada x de onde a barra tem que estar localizada
        coordy --> coordenada y de onde a barra tem que estar localizada
        '''
        self.hp = hp
        self.height = 10
        self.length = self.hp/10
        self.x = coordx
        self.y = coordy

        self.font = pygame.font.Font(pygame.font.get_default_font(), 10)
    
    def update_hp(self, damage):
        '''
        Função atualiza:
        - Atualiza o tamanho da barra de acordo com o dano recebido

        damage -> integer da qtd de dano recebido pelo jogador
        '''
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        self.length = self.hp/10

    def draw_hp(self, window):
        '''
        Função desenha:
        - Desenha barra de vida do jogador na sua respectiva posição

        window -> variável que segura a janela do pygame
        '''
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(self.x-2, self.y-2, 104, self.height + 4))
        pygame.draw.rect(window, (205, 20, 50), pygame.Rect(self.x, self.y, 100, self.height))
        pygame.draw.rect(window, (0, 200, 20), pygame.Rect(self.x, self.y, self.length, self.height))
        window.blit(self.font.render(f"{int(self.hp)}", True, (0, 0, 0)), (self.x - 80, self.y))
        window.blit(self.font.render(f"1000", True, (0, 0, 0)), (self.x - 45, self.y))
    
    def check_ending(self):
        '''
        Função checa final:
        - De acordo com o comprimento da barra de vida, retorna se o jogo deve acabar ou não
        '''
        if self.length <= 0:
            return True
        return False