'''
Esse módulo é responsável pelas classe da barra que se movimenta utilizada na lógica do
minigame 4 (Precisão / Desvio Padrão)
'''


class Barra:
    '''
    Classe Barra:
    - Cria a barra que fica rodando pela tela
    '''
    def __init__(self):
        '''
        Inicializa todas as variáveis necessárias para o objeto (coordenadas, comprimento, velocidade de movimento, cor)
        '''
        self.x = 0
        self.y = 240

        self.w = 10
        self.h = 240

        self.vx = 400
        self.cor = [0,0,0]
    
    def mover(self, last_updated, ticks):
        '''
        Função atualiza a posição da barra ao redor da tela
        '''
        delta_t = ticks - last_updated

        novo_x = self.x + delta_t * (self.vx/1000)
        
        if novo_x > 640:
            self.x = 0
        else:
            self.x = novo_x
