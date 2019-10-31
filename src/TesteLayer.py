from cocos.layer.util_layers import ColorLayer
from cocos.director import director


class TesteLayer(ColorLayer):
    is_event_handler = True
    
    def on_mouse_press (self, x, y, buttons, modifiers):
        """This function is called when any mouse button is pressed

        (x, y) are the physical coordinates of the mouse
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
           (values like 'SHIFT', 'OPTION', 'ALT')
        """
        #self.tabuleiro.mudarCor(1.0)
        print(director.get_virtual_coordinates (x, y))
        
        
        #montagem da matriz inicial
#        self.tabMatrix = []
#        for i in range(8):
#            linha = []
#            for j in range(8):
#                linha.append(0)
#            self.tabMatrix.append(linha)
#        self.tabMatrix[3][3] = 1
#        self.tabMatrix[3][4] = 2
#        self.tabMatrix[4][3] = 2
#        self.tabMatrix[4][4] = 1
        ###################################