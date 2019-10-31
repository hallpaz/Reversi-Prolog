from cocos.layer.base_layers import Layer
from cocos.scene import Scene
from Peca import Peca
from cocos.sprite import Sprite
from cocos.batch import BatchNode
from GameHud import GameHud


class Tabuleiro(Layer):
    is_event_handler = True
    
    def __init__( self, director ):
        super( Tabuleiro, self ).__init__()
        
        self.director = director
        self.tabuleiro = []
        self.offsetX = 100
        self.offsetY = 100
        lado = 32
        
        #montagem da matriz inicial
        self.tabMatriz = []
        for i in range(8):
            linha = []
            for j in range(8):
                linha.append(0)
            self.tabMatriz.append(linha)
        self.tabMatriz[3][3] = 1
        self.tabMatriz[3][4] = 2
        self.tabMatriz[4][3] = 2
        self.tabMatriz[4][4] = 1
        ###################################
        
        #Batch que vai segurar todos os pecas
        self.spriteBatch = BatchNode()
        self.add(self.spriteBatch)
        
        
        for i in range(8):
            l = []
            for j in range(8):
                if(self.tabMatriz[i][j] == 0):
                    peca = Peca("vazio.png", (i*lado + lado/2, j*lado + lado/2))
                elif(self.tabMatriz[i][j] == 1):
                    peca = Peca("preto.png", (i*lado + lado/2, j*lado + lado/2))
                elif(self.tabMatriz[i][j] == 2):
                    peca = Peca("branco.png", (i*lado + lado/2, j*lado + lado/2))
                l.append(peca)
                self.spriteBatch.add(peca)
            self.tabuleiro.append(l)
        
        self.spriteBatch.position = (self.offsetX, self.offsetY)
        
        self.teste = Sprite("grossini.png", (300,200))
        self.spriteBatch.add(self.teste)
        
        self.hud = GameHud()
        self.add(self.hud)
        
        for i in self.tabMatriz:
            print i
        
    #Funcao que atualiza o tabuleiro
    def atualizaTabuleiro(self, newMatrix):
        delay = 0.0
        for i in range(8):
            for j in range(8):
                if(self.tabMatriz[i][j] != newMatrix[i][j]):
                    delay += 0.02
                    self.tabuleiro[i][j].mudarCor(delay, newMatrix[i][j])
    
    def on_mouse_press (self, x, y, buttons, modifiers):
        """This function is called when any mouse button is pressed

        (x, y) are the physical coordinates of the mouse
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
           (values like 'SHIFT', 'OPTION', 'ALT')
        """
        #self.tabuleiro.mudarCor(1.0)
        print(self.director.get_virtual_coordinates(x, y))
        
        