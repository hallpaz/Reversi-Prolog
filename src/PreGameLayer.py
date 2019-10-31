from cocos.menu import ImageMenuItem, Menu, MenuItem, shake_back, shake,\
    zoom_out, zoom_in, fixedPositionMenuLayout
from cocos.director import director
from GameLayer import GameLayer
from cocos.sprite import Sprite
from cocos.scene import Scene
from cocos.text import Label
from cocos.layer.util_layers import ColorLayer
from cocos.audio import effect
from cocos.audio.effect import Effect
from orca.sound import Sound


class PreGameLayer(ColorLayer):
    def __init__(self, director, dificuldade):
        super(PreGameLayer, self).__init__(180, 180, 180, 128)
        self.director = director
        
        self.dificuldade = dificuldade
        
        self.fundo = Sprite("frankstein.jpg")
        self.fundo.opacity = 50
        self.fundo.position = (director.get_window_size()[0]/2,
                                director.get_window_size()[1]/2)
        
        self.menu = PreJogoMenu()
        self.add(self.menu)
        self.add(self.fundo)
        
        #self.texto = Label("Escolha uma peca: ", 
        #                 font_name = 'Blood Of Dracula', font_size = 22,
        #                 x = 50, y = 300)
        #self.add(self.texto)
    
    def criarCenar(self):
        cena = Scene(self)
        return cena
        
class PreJogoMenu(Menu):
    def __init__(self):
        super( PreJogoMenu, self ).__init__(" 'Lasciate ogni speranza, voi che entrate.' ")
        self.font_title['font_name'] = 'Blood Of Dracula'
        self.font_title['font_size'] = 30
        self.font_title['color'] = (255, 0, 0, 255)
        
        self.font_item['font_name'] = 'Bloodsuckers'
        self.font_item_selected['font_name'] = 'Bloodsuckers'
        
        itens = []
        pumpkin = ImageMenuItem("pumpkin.png", self.on_start, 1)
        skull = ImageMenuItem("skull.gif", self.on_start, 2)
        pumpkin.scale = 2.0
        skull.scale = 2.0
        pumpkin.position = (70, 0)
        skull.position = (-70, 32)
        itens.append(pumpkin)
        itens.append(skull)
        desistir = MenuItem("Desista!!!", self.on_return)
        desistir.position = (desistir.position[0], desistir.position[1] - 50)
        itens.append(desistir)
        self.create_menu(itens, zoom_in(), zoom_out())
        
        
    def on_start(self, peca):
        gameLayer = GameLayer(self.parent.director, self.parent.dificuldade)
        self.parent.director.replace(gameLayer.criarCena())
        
    def on_return(self):
        self.parent.director.pop()
        pass