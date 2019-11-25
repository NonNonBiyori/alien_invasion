import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
	''' for print and mouse event '''
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			    
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True	
	elif event.key == pygame.K_DOWN:
		ship.moving_up = True
	elif event.key == pygame.K_UP:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_the_hore(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_ESCAPE:
		sys.exit()		
			
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_DOWN:
		ship.moving_up = False
	elif event.key == pygame.K_UP:
		ship.moving_down = False		
				
			
def updata_screen(ai_settings, screen, ship, bullets, alien):
	screen.fill(ai_settings.bg_color)
	
	background = pygame.image.load("/home/xujl/python_work/alien_invasion/images/h2513--.png")
	screen.blit(background,(0,0))
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	alien.blitme()
	
	pygame.display.flip()
	
	
def fire_the_hore(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullet_allowed:
	    new_bullet = Bullet(ai_settings,screen,ship)
	    bullets.add(new_bullet)
	
	
def update_bullets(bullets):
	bullets.update()
	
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print(len(bullets))
