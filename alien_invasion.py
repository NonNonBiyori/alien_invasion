import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
            
    ship = Ship(screen,ai_settings)
    bullets = Group()
    
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.updataLocation()
        gf.update_bullets(bullets)
        gf.updata_screen(ai_settings, screen, ship,bullets)


run_game()
