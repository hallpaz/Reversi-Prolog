from cocos.layer.base_layers import Layer
from cocos.scene import Scene
from Peca import Peca
from cocos.sprite import Sprite
from cocos.batch import BatchNode
from GameHud import GameHud
from pyswip.prolog import Prolog
from copy import deepcopy
from pyglet.window.mouse import LEFT, RIGHT
from Background import Background
from cocos.text import Label
import pyglet
from GameOverLayer import GameOverLayer


class GameLayer(Layer):
    is_event_handler = True
    
    def __init__( self, director, dificuldade ):
        super( GameLayer, self ).__init__()
        
        self.director = director
        self.tabuleiro = []
        self.offsetX = director.get_window_size()[0]/3
        self.offsetY = director.get_window_size()[1]/8
        lado = 45
        self.lado = lado
        self.dificuldade = dificuldade
        
        self.cpu = False
        
        self.prolog = Prolog()
        self.prolog.consult("reversi.pl")
        self.tabMatriz = list(self.prolog.query("novotab(X)"))[0]['X']
        self.matriz = deepcopy(self.tabMatriz)
        
        pyglet.font.add_directory('.')
        self.jogadorAtivo = Label("Jogador: Player1", font_name = 'Blood Of Dracula', font_size = 22,
                                 x = 20, y = 350)
        self.add(self.jogadorAtivo)
        self.dif = Label("Dificuldade: " + self.dificuldade, font_name = 'Blood Of Dracula', font_size = 16,
                                 x = 20, y = 300)
        self.add(self.dif)
        self.p = list(self.prolog.query("winner(" + str(self.tabMatriz) + ", P0, P1, P2)"))[0]
        self.p1 = Label("P1: " + str(self.p['P1']) + self.dificuldade, font_name = 'Bloodsuckers', font_size = 26,
                                 x = 20, y = 200)
        self.p2 = Label("P1: " + str(self.p['P2']) + self.dificuldade, font_name = 'Bloodsuckers', font_size = 26,
                                 x = 20, y = 150)
        self.add(self.p1)
        self.add(self.p2)
        
        #Batch que vai segurar todos os pecas
        self.spriteBatch = BatchNode()
        self.add(self.spriteBatch)
        
        size = 8*self.lado
        for i in range(8):
            l = []
            for j in range(8):
                peca = Peca(self.tabMatriz[i][j], (j*lado + lado/2, size - (i*lado + lado/2)))
                l.append(peca)
                self.spriteBatch.add(peca)
            self.tabuleiro.append(l)
            
        self.spriteBatch.add(Sprite("tabuleiro.png", 
                                    (self.tabuleiro[4][4].position[0] - lado/2, self.tabuleiro[4][4].position[1] + lado/2) 
                                    , 0, 1, 32), 0)
        
        self.spriteBatch.position = (self.offsetX, self.offsetY)
        self.spriteBatch.scale = 1.0        
        
        self.hud = GameHud()
        self.add(self.hud)
        
        self.schedule(self.gameLoop)
        
        
    def criarCena(self):
        background = Background("caldron.jpg")
        background.position = (self.director.get_window_size()[0]/2,
                                self.director.get_window_size()[1]/2)
        background.fundo.opacity = 100
        cena = Scene(background, self )
        return cena
        
    #Funcao que atualiza o tabuleiro
    def atualizaTabuleiro(self, newMatrix):
        delay = 0.0
        for i in range(8):
            for j in range(8):
                if(self.tabMatriz[i][j] != newMatrix[i][j]):
                    delay += 0.04
                    self.tabuleiro[i][j].mudarCor(delay, newMatrix[i][j])
    
    def gameLoop(self, dt):
        #Implementar o loop do game
        self.atualizarJogador()
        retorno = list(self.prolog.query("dont_game_over(" + str(self.tabMatriz) + ")"))
        self.p = list(self.prolog.query("winner(" + str(self.tabMatriz) + ", P0, P1, P2)"))[0]
        
        self.p1.element.text = "P1: " + str(self.p['P1'])
        self.p2.element.text = "P2: " + str(self.p['P2'])
        
        if(not retorno):
            self.schedule_interval(self.gameOver, 3.0)
        pass
    
    def gameOver(self, dt):
        v = list(self.prolog.query("winner("+ str(self.tabMatriz) + ", V)"))[0]['V']
        print(v)
        self.director.replace(GameOverLayer(v).criarCena())
    
    def atualizarJogador(self):
        if(self.cpu):
            self.jogadorAtivo.element.text = "CPU"
            self.jogadorAtivo.element.font_size = 26
        else:
            self.jogadorAtivo.element.font_size = 22
            self.jogadorAtivo.element.text = "Jogador: Player1"
            
    
    def turnoCPU(self, dt):
        if(self.cpu):
            consulta = self.dificuldade +"_play("+ str(self.tabMatriz) + ", Novo)"
            retorno = list(self.prolog.query(consulta))
            if(retorno): #se for possivel jogar
                self.matriz = retorno[0]['Novo']
                self.atualizaTabuleiro(self.matriz)
                self.tabMatriz = deepcopy(self.matriz)
            self.cpu = False
            self.unschedule(self.turnoCPU)
        
    def on_mouse_press (self, x, y, buttons, modifiers):           
        if(not self.cpu):
            posx, posy = self.director.get_virtual_coordinates (x, y)
            posx = posx - self.offsetX
            posy = posy - self.offsetY
            j = int(posx / self.lado)
            i = 7 - int(posy / self.lado)
        
            if((i > 7) | (j > 7) | (i < 0) | (j < 0)):
                return
            
            if(not list(self.prolog.query("macaco(" + str(self.tabMatriz) + ", 0, I, J, 1)"))[0]):
                self.cpu = True
                return
        
            if(buttons == LEFT):
                consulta = "play(" + str(self.tabMatriz) + ", " + str(i) + ", " + str(j) + ", 1, Novo)"
            if(buttons == RIGHT):
                consulta = "play(" + str(self.tabMatriz) + ", " + str(i) + ", " + str(j) + ", 2, Novo)"
            retorno = list(self.prolog.query(consulta))
            if(retorno):  # se for possivel jogar            
                self.matriz = retorno[0]['Novo']
                self.atualizaTabuleiro(self.matriz)
                self.tabMatriz = deepcopy(self.matriz)
                self.cpu = True
                self.schedule_interval(self.turnoCPU, 2.0)
            
