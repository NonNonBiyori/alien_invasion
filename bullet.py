import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""子弹管理类"""
	
	def __init__(self,ai_settings,screen,ship):
		super().__init__()
		self.screen = screen
		
		#在（0，0）处设置子弹然后移到正确位置
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
		           ai_settings_bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.init_speed = ai.settings.bullet_init_speed
		
	def update(self):
		""""移动子弹"""
		self.y -= self.init_speed
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)
