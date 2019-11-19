import sys
import pygame

def check_events(ship):
	''' for print and mouse event '''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			    
def check_keydown_events(event,ship):
	print(event.key)
	print("\n")
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True	
	elif event.key == pygame.K_DOWN:
		ship.moving_up = True
	elif event.key == pygame.K_UP:
		ship.moving_down = True		
			
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_DOWN:
		ship.moving_up = False
	elif event.key == pygame.K_UP:
		ship.moving_down = False		
				
			
def updata_screen(ai_settings, screen, ship):
	screen.fill(ai_settings.bg_color)
	
	background = pygame.image.load("/home/xujl/python_work/alien_invasion/images/h2513.png")
	screen.blit(background,(0,0))
	ship.blitme()
	
	pygame.display.flip()
