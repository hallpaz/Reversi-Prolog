from cocos.layer.base_layers import Layer
from cocos.sprite import Sprite

class Background(Layer):
    def __init__(self, imagem):
        super(Background, self).__init__()
        self.fundo = Sprite(imagem)
        self.add(self.fundo)