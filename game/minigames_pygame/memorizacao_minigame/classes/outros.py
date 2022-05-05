
class Bolinha:
    def __init__(self, id_bolinha, x, y, raio):
        self.id_bolinha = id_bolinha 
        self.x = x
        self.y = y
        self.cor = [251,54,64]
        self.raio = raio
        self.centro = [self.x, self.y]

    def mouse_on_top(self, x_mouse, y_mouse):

        hipo = ((x_mouse - self.x)**2 + (y_mouse - self.y)**2)**(1/2)

        if self.raio >= hipo:
            return True 
        else:
            return False