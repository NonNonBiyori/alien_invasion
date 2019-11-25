import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """单个外星人类"""

    def __init__(self,ai_settings,screen):
        """初始化外星人，设置起始位置"""

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """外星人图像"""
        self.image = pygame.image.load('/home/xujl/python_work/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        """在左上角"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
