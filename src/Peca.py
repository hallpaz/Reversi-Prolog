import pyglet

from cocos.sprite import Sprite
from cocos.actions.interval_actions import Delay, Rotate


class Peca(Sprite):
    preto = pyglet.image.load("preto.png")
    branco = pyglet.image.load("branco.png")
    vazio = pyglet.image.load("vazio.png")
    pumpkin = pyglet.image.load("pumpkin.png")
    skull = pyglet.image.load("skull.gif")
    def __init__(self, tipo, position=(0,0)):
        super(Peca, self).__init__("vazio.png", position, 0, 1, 0)
        
        self.image = Peca.vazio
        self.tipo = tipo
        if(self.tipo == 1):
            self.image = Peca.pumpkin
            self.opacity = 255
        elif(self.tipo == 2):
            self.image = Peca.skull
            self.opacity = 255

    
    def mudarCor(self, delay, tipo):
        espera = Delay(delay)
        rotacao = Rotate(360, 0.5)
        self.do(espera + rotacao)
        self.tipo = tipo
        if(self.tipo == 1):
            self.image = Peca.pumpkin
        elif(self.tipo == 2):
            self.image = Peca.skull
        self.opacity = 255
    