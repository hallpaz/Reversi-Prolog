from cocos.layer.base_layers import Layer
from cocos.scene import Scene
from cocos.menu import Menu, MenuItem, shake, shake_back,\
    fixedPositionMenuLayout, LEFT, BOTTOM
import pyglet
from cocos.director import director
from cocos.sprite import Sprite
from cocos.text import Label


class GameOverLayer(Layer):
    def __init__(self, vencedor):
        super(GameOverLayer, self).__init__()
        self.add(GameOverMenu())
        self.fundo = Sprite("gameover.png")
        self.fundo.opacity = 100
        self.fundo.position = (director.get_window_size()[0]/2,
                                director.get_window_size()[1]/2)
        self.add(self.fundo)
        
        if(vencedor == 1):
            self.v = Label("Voce Venceu!!!", font_name = 'Bloodsuckers', font_size = 36,
                                 x = 300, y = 200)
            self.add(self.v)
        if(vencedor == 2):
            self.v = Label("Voce Perdeu!!!", font_name = 'Bloodsuckers', font_size = 36,
                                 x = 300, y = 200)
            self.add(self.v)
        if(vencedor == 0):
            self.v = Label("Empate!!!", font_name = 'Bloodsuckers', font_size = 36,
                                 x = 300, y = 200)
            self.add(self.v)
            
            
    def criarCena(self):
        cena = Scene(self)
        return cena
    
class GameOverMenu(Menu):
    def __init__(self):
        super(GameOverMenu, self).__init__("")
        
        pyglet.font.add_directory('.')
        

        self.font_item['font_name'] = 'Bloodsuckers'
        self.font_item_selected['font_name'] = 'You Are Loved'
        self.font_item['color'] = (255, 0, 0, 255)
        
        self.menu_valign = BOTTOM
        self.menu_halign = LEFT
        
        itens = []
        itens.append(MenuItem("Menu principal", self.on_restart))
        #itens.append(MenuItem("Sair", self.on_quit))
        self.create_menu(itens, shake(), shake_back())
        
    def on_restart(self):
        director.pop()
        
    def on_quit(self):
        pass