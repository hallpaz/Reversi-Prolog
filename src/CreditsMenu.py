from cocos.menu import Menu, MenuItem, BOTTOM, LEFT
from cocos.layer.base_layers import Layer
from cocos.text import Label

class CreditsMenu(Menu):
    def __init__( self ):
        super( CreditsMenu, self ).__init__("Creditos")

        self.font_title['font_name'] = 'Blood Of Dracula'
        self.font_title['font_size'] = 60
        self.font_title['color'] = (255, 16, 16, 255)
        
        self.font_item['font_name'] = 'Blood Of Dracula'
        self.font_item_selected['font_name'] = 'You Are Loved'

        self.menu_valign = BOTTOM
        self.menu_halign = LEFT

        self.create_menu( [MenuItem('Voltar', self.on_quit)] )

    def on_quit( self ):
        self.parent.parent.switch_to( 0 )

class CreditsLayer(Layer):
    def __init__(self):
        super(CreditsLayer, self).__init__()
        self.menu = CreditsMenu()
        self.add(self.menu)
        
        self.motivo = Label("Jogo apresentado ao Instituto Militar de Engenharia", 
                            font_name = 'Blood Of Dracula', font_size = 16,
                            x = 310, y = 60)
        self.motivo2 = Label("como avaliacao parcial na disciplina de Logica Matematica", 
                            font_name = 'Blood Of Dracula', font_size = 16,
                            x = 300, y = 30)
        self.autores = Label("Equipe: ", font_name = 'Bloodsuckers', font_size = 28,
                            x = 30, y = 300)
        self.althoff = Label("Paulo Althoff ", font_name = 'Bloodsuckers', font_size = 25,
                            x = 80, y = 270)
        self.hallison = Label("Hallison da Paz ", font_name = 'Bloodsuckers', font_size = 25,
                            x = 80, y = 240)
        self.cadu = Label("Eduardo Rocha ", font_name = 'Bloodsuckers', font_size = 25,
                            x = 80, y = 210)
        
        self.professor = Label("Professor: ", font_name = 'Bloodsuckers', font_size = 28,
                            x = 30, y = 160)
        self.veloso = Label("Marcos Veloso", font_name = 'Bloodsuckers', font_size = 25,
                            x = 250, y = 160)
        
        self.add(self.motivo)
        self.add(self.motivo2)
        self.add(self.autores)
        self.add(self.althoff)
        self.add(self.hallison)
        self.add(self.cadu)
        self.add(self.professor)
        self.add(self.veloso)