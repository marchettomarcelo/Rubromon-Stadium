'''
Esse módulo é responsável pelas classe das bolinhas utilizadas na lógica do
minigame 1 (Dory Decore)
'''

class Bolinha:
    '''
    Classe Bolinha:
    - Cria os objetos a serem clicados pelo jogador em ordem
    '''
    def __init__(self, id_bolinha, x, y, raio):
        '''
        Inicializa todas as variáveis necessárias para o objeto (n° da ordem, coordenadas, cor, raio, centro)
        '''
        self.id_bolinha = id_bolinha 
        self.x = x
        self.y = y
        self.cor = [251,54,64]
        self.raio = raio
        self.centro = [self.x, self.y]

    def mouse_on_top(self, x_mouse, y_mouse):
        '''
        Função checa se o mouse do jogador está dentro do círculo, usando o raio como referência
        '''

        hipo = ((x_mouse - self.x)**2 + (y_mouse - self.y)**2)**(1/2)

        if self.raio >= hipo:
            return True 
        else:
            return False