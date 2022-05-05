import random
import pygame
def colisao_rect(vermelho, azul):
    
    l_vermelho = vermelho[0]
    t_vermelho = vermelho[1]
    r_vermelho = vermelho[0] + vermelho[2]
    b_vermelho = vermelho[1] + vermelho[3]

    l_azul = azul[0]
    t_azul = azul[1]
    r_azul = azul[0] + azul[2]
    b_azul = azul[1] + azul[3]
    
    if r_vermelho >= l_azul and r_azul >= l_vermelho and  b_vermelho >= t_azul  and b_azul >= t_vermelho :
        return True
    else:
        return False


class Meteoro:
    def __init__(self, image ):
        self.x = random.randint(-10,540 )
        self.y = -500
        
        self.vy = random.randint(300, 500)

        img = pygame.transform.smoothscale(image, (100, 100)) 
        
        self.image = img


    def atualiza_posicao(self, novo_y):
        
        if novo_y > 480:
            self.y = -500
            self.x = random.randint(-10,540 )
            self.vy = random.randint(300, 500)

        else:
            self.y = novo_y
    
    def confere_se_colidiu(self, nave_pos):

        infos_meteoro = [self.x + 49, self.y + 49, 2, 2]

        x_nave, y_nave = nave_pos
        infos_nave = [x_nave + 30, y_nave+ 30 , 40, 40]
        
        return colisao_rect(infos_meteoro, infos_nave)
        
    

class Nave:
    def __init__(self, posicao, image):
        
        self.posicao = posicao
        img = pygame.transform.smoothscale(image, (100, 100)) 
        self.image = img
    
    def atualiza_posicao(self, nova_posicao):
        self.posicao = nova_posicao