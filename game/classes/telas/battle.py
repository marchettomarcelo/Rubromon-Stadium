import pygame
from global_vars import *
from minigames_pygame.atletica_minigame.main import *
from minigames_pygame.digitar_rapido_minigame.main import *
from minigames_pygame.memorizacao_minigame.main import *
from minigames_pygame.precisao_minigame.main import *

class Battle:
    def __init__(self, player1, player2):
        self.name = BATTLE
        self.player1 = player1
        self.player2 = player2
        
        self.assets = {
            'font_20' : pygame.font.Font(pygame.font.get_default_font(), 20),
            'font_12' : pygame.font.Font(pygame.font.get_default_font(), 12),
            'font_30' : pygame.font.Font(pygame.font.get_default_font(), 30),
            'background' : pygame.image.load("assets/backgrounds/classroom.png"),
            'player1_skin' : characters[player1]['skins'][0],
            'player2_skin' : characters[player2]['skins'][1],
            'battle_border' : pygame.image.load("assets/sprites/Battle_BorderJPG.jpg"),
            'attack_colors' : pygame.image.load('assets/attack_colors.png'),
            'hp_bar' : pygame.image.load("assets/hp_bar.png"),
            'click_sound' : pygame.mixer.Sound('assets/sons/click_sound.mp3')
            }
        
        self.hp_bars = {
            player1 : HpBar(characters[player1]['hp'], WIDTH/40 + 90, 48),
            player2 : HpBar(characters[player2]['hp'], 2*WIDTH/3 + 90, 2*HEIGHT/3 - 52)
        }
        self.damage = 0

        self.coords = {
            'player1_x' : 630,
            'player1_y' : 120,
            'player2_x' : -200,
            'player2_y' : 20
        }

        self.last_updated = pygame.time.get_ticks()

        self.clicked_key = False
        self.out_of_position = True

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
        for player, bar in self.hp_bars.items():
            if bar.check_ending():
                screens['result'] = player
                return GAMEOVER

        self.menu = self.menus_list[self.current_menu][self.player_attacking]

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT
            if ev.type == pygame.KEYDOWN and not self.clicked_key:
                self.clicked_key = True
                if ev.key == pygame.K_SPACE or ev.key == pygame.K_RETURN:
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    self.current_menu = self.menu[self.current_item]
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
                if ev.key == pygame.K_UP:
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    self.current_item -= 1
                    if self.current_item < 0:
                        self.current_item = len(self.menu) - 1
                if ev.key == pygame.K_DOWN:
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    self.current_item += 1
                    if self.current_item >= len(self.menu):
                        self.current_item = 0
                if ev.key == pygame.K_ESCAPE and self.current_menu != '<- Back':
                    self.current_menu = '<- Back'
            if ev.type == pygame.KEYUP:
                self.clicked_key = False

        return self.name

    def draw(self, window):
        window.fill((0, 0, 0))

        window.blit(self.assets['background'], (0, -160))
        window.blit(self.assets['battle_border'], (0, 320) )

        ticks = pygame.time.get_ticks()
        delta_t = (ticks - self.last_updated)/1000
        
        if self.out_of_position:
            self.coords['player1_x'] = self.coords['player1_x'] - 200 * delta_t
            self.coords['player2_x'] = self.coords['player2_x'] + 200 * delta_t

            window.blit(self.assets['player2_skin'], (self.coords['player2_x'], self.coords['player2_y']))
            window.blit(self.assets['player1_skin'], (self.coords['player1_x'], self.coords['player1_y']))

            window.blit(self.assets['font_30'].render(f"{self.player2} wants to battle!", True, (0, 0, 0)), (30, 2*HEIGHT/3 + HEIGHT/7))

            if self.coords['player1_x'] <= 75 or self.coords['player2_x'] >= 390:
                self.out_of_position = False

        else:
            window.blit(self.assets['player1_skin'], (self.coords['player1_x'], self.coords['player1_y']))
            window.blit(self.assets['player2_skin'], (self.coords['player2_x'], self.coords['player2_y']))

            for i in range(len(self.menu)):
                text = self.menu[i]
                if i == self.current_item:
                    text = '> ' + text
                else:
                    text = '  ' + text
                
                text_image = self.assets['font_20'].render(text, True, (0, 0, 0))
                window.blit(text_image, (30, 347 + i * 30))
        
            window.blit(self.assets['hp_bar'], (WIDTH/40, 40))
            window.blit(self.assets['hp_bar'], (2*WIDTH/3, 2*HEIGHT/3 - 60))

            if self.current_menu == "Fight":
                window.blit(self.assets['attack_colors'], (0, 0))

            for bar in self.hp_bars.values():
                bar.draw_hp(window)
            
            window.blit(self.assets['font_20'].render(f"Attacker:", True, (0, 0, 0)), (400, 347))
            window.blit(self.assets['font_20'].render(f"{self.player_attacking}", True, (0, 0, 0)), (400, 377))

        self.last_updated = ticks
        pygame.display.update()
    
    def attack(self, window, attack):
        points = [0, 0]
        attacks = [run_minigame1, run_minigame2, run_minigame3, run_minigame4]

        for player in range(2):
            points[player] = attacks[attack](window)
    
        if attack == 1:
            self.damage = 200 * points[0]/points[1]
        elif attack == 4:
            self.damage = 150 * points[1]/points[0]
        else:
            self.damage = 200 * points[1]/points[0]
        
        if self.damage > 300:
            self.damage = 300



class HpBar():
    def __init__(self, hp, coordx, coordy):
        self.hp = hp
        self.height = 10
        self.length = self.hp/10
        self.x = coordx
        self.y = coordy

        self.font = pygame.font.Font(pygame.font.get_default_font(), 10)
    
    def update_hp(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        self.length = self.hp/10

    def draw_hp(self, window):
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(self.x-2, self.y-2, 104, self.height + 4))
        pygame.draw.rect(window, (205, 20, 50), pygame.Rect(self.x, self.y, 100, self.height))
        pygame.draw.rect(window, (0, 200, 20), pygame.Rect(self.x, self.y, self.length, self.height))
        window.blit(self.font.render(f"{int(self.hp)}", True, (0, 0, 0)), (self.x - 80, self.y))
        window.blit(self.font.render(f"1000", True, (0, 0, 0)), (self.x - 45, self.y))
    
    def check_ending(self):
        if self.length <= 0:
            return True
        return False