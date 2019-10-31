from cocos.menu import BOTTOM, LEFT, MenuItem, Menu



class GameHud(Menu):
    def __init__( self ):
        super( GameHud, self ).__init__()

        self.font_item['font_name'] = 'Bloodsuckers'
        self.font_item_selected['font_name'] = 'Bloodsuckers'
        self.font_item['font_size'] = 30

        self.menu_valign = BOTTOM
        self.menu_halign = LEFT

        self.create_menu( [MenuItem('Arregar', self.on_quit)] )

    def on_quit( self ):
        self.parent.director.pop()
