
class Barra:
    def __init__(self):
        self.x = 0
        self.y = 240

        self.w = 10
        self.h = 240

        self.vx = 400
        self.cor = [0,0,0]
    
    def mover(self, last_updated, ticks):

    
        delta_t = ticks - last_updated

        novo_x = self.x + delta_t * (self.vx/1000)
        
        if novo_x > 640:
            self.x = 0
        else:
            self.x = novo_x
