class Settings():
    """ save setting """

    def __init__(self):
        """init"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        self.ship_speed_init = 7.5
        
        #子弹设置
        self.bullet_speed_init = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 100
        
