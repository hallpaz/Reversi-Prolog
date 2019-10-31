#
# cocos2d
# http://cocos2d.org
#
# Particle Engine done by Phil Hassey
# http://www.imitationpickles.org
#

import sys
import os
from CreditsMenu import CreditsLayer
from PreGameLayer import PreGameLayer
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pyglet
from pyglet.gl import *

from cocos.director import *
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *
from cocos.actions import *
from cocos.sprite import Sprite

import random; rr = random.randrange


class Fire: 
    def __init__(self,x,y,vy,frame,size):
        self.x,self.y,self.vy,self.frame,self.size = x,y,vy,frame,size

class FireManager( Layer ):
    def __init__(self, view_width, num):
        super( FireManager, self ).__init__()

        self.view_width = view_width
        self.goodies = []
        self.batch = pyglet.graphics.Batch()
        self.fimg = pyglet.resource.image('fire.jpg')
        self.group = pyglet.sprite.SpriteGroup(self.fimg.texture,
            blend_src=GL_SRC_ALPHA, blend_dest=GL_ONE)
        self.vertex_list = self.batch.add(4*num, GL_QUADS, self.group,
            'v2i', 'c4B', ('t3f', self.fimg.texture.tex_coords*num))
        for n in xrange(0, num):
            f = Fire(0,0,0,0,0)
            self.goodies.append(f)
            self.vertex_list.vertices[n*8:(n+1)*8] = [0, 0, 0, 0, 0, 0, 0, 0]
            self.vertex_list.colors[n*16:(n+1)*16] = [0,0,0,0,] * 4

        self.schedule( self.step )

    def step(self,dt):
        w,h = self.fimg.width,self.fimg.height
        fires = self.goodies
        verts, clrs = self.vertex_list.vertices, self.vertex_list.colors
        for n,f in enumerate(fires):
            if not f.frame:
                f.x = rr(0,self.view_width)
                f.y = rr(-120,-80)
                f.vy = rr(40,70)/100.0
                f.frame = rr(50,250)
                f.size = 8+pow(rr(0.0,100)/100.0,2.0)*32;
                f.scale= f.size/32.0
            
            x = f.x = f.x+ rr(-50,50)/100.0
            y = f.y = f.y+f.vy*4
            c = 3*f.frame/255.0;
            r,g,b = (min(255,int(c*0xc2)),min(255,int(c*0x41)),min(255,int(c*0x21)))
            f.frame -= 1
            ww,hh = w*f.scale,h*f.scale
            x-=ww/2
            verts[n*8:(n+1)*8] = map(int,[x,y,x+ww,y,x+ww,y+hh,x,y+hh])
            clrs[n*16:(n+1)*16] = [r,g,b,255] * 4

    def draw( self ):
        glPushMatrix()
        self.transform()

        self.batch.draw()

        glPopMatrix()



class MenuPrincipal(Menu):
    def __init__( self ):
        
        # call superclass with the title
        super( MenuPrincipal, self ).__init__("REVERSI !" )

        pyglet.font.add_directory('.')

        # you can override the font that will be used for the title and the itens
        self.font_title['font_name'] = 'Blood Of Dracula'
        self.font_title['font_size'] = 72
        self.font_title['color'] = (255, 16, 16, 255)

        self.font_item['font_name'] = 'You Are Loved'
        self.font_item_selected['font_name'] = 'Blood Of Dracula'
        self.font_item_selected['color'] = (255, 0, 0, 255)

        # you can also override the font size and the colors. see menu.py for
        # more info

        # example: menus can be vertical aligned and horizontal aligned
        self.menu_valign = CENTER
        self.menu_halign = CENTER

        itens = []

        itens.append( MenuItem('Novo Jogo', self.on_start ) )
        itens.append( MenuItem('Opcoes', self.on_options ) )
        itens.append( MenuItem('Creditos', self.on_credits ) )
        itens.append( MenuItem('Sair', self.on_quit ) )

        self.create_menu( itens, zoom_in(), zoom_out() )


    # Callbacks
    def on_start( self ):
        preGameLayer = PreGameLayer(director, dificuldade)
        director.push(preGameLayer.criarCenar())
        print "on_start()"
           

    def on_credits( self ):
        self.parent.switch_to( 2 )

    def on_options( self ):
        self.parent.switch_to( 1 )
        #risada = Effect("risada.wav")
        #risada.play()

    def on_quit( self ):
        director.pop()
        
class OptionMenu(Menu):
    def __init__( self ):
        super( OptionMenu, self ).__init__("REVERSI !" )

        self.font_title['font_name'] = 'Blood Of Dracula'
        self.font_title['font_size'] = 72
        self.font_title['color'] = (255, 16, 16, 255)
        
        self.font_item['font_name'] = 'You Are Loved'
        self.font_item_selected['font_name'] = 'Blood Of Dracula'

        self.menu_valign = BOTTOM
        self.menu_halign = RIGHT
        
        global dificuldade
        dificuldade = "macaco"

        itens = []
        self.dificuldades = ['macaco', 'golfinho']
        self.teste = MultipleMenuItem("Dificuldade:", self.hardWay, self.dificuldades, 0)
        print self.teste.idx
        itens.append( MenuItem('Fullscreen', self.on_fullscreen) )
        itens.append(self.teste)
        itens.append( ToggleMenuItem('Show FPS: ', self.on_show_fps, True) )
        itens.append( MenuItem('OK', self.on_quit) )
        self.create_menu( itens, shake(), shake_back() )
        

    # Callbacks
    def on_fullscreen( self ):
        director.window.set_fullscreen( not director.window.fullscreen )
        
    def hardWay(self, idx):
        #print(self.teste.idx)
        balde = self.dificuldades[0]
        self.dificuldades[0] = self.dificuldades[1]
        self.dificuldades[1] = balde
        global dificuldade
        dificuldade = self.dificuldades[0]
        print dificuldade

    def on_quit( self ):
        self.parent.switch_to( 0 )

    def on_show_fps( self, value ):
        director.show_FPS = value

def init():
    director.init( resizable=True, width=800, height=450)

def start():
    director.set_depth_test()

    firelayer = FireManager(director.get_window_size()[0], 250)
    menulayer = MultiplexLayer( MenuPrincipal(), OptionMenu(), CreditsLayer() )
    
    scene =Scene( firelayer, menulayer )

    firelayer.do( Delay(4) + Repeat( RotateBy(360, 10) ) )
    
    

    return scene

def run(scene):
    director.run( scene )

if __name__ == "__main__":
    init()
    s = start()
    run(s)
