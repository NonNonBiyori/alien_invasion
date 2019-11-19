import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
            

    bg_color = (230,0,230)
    ship = Ship(screen,ai_settings)
    
    while True:
        gf.check_events(ship)
        ship.updataLocation()
        gf.updata_screen(ai_settings, screen, ship)


run_game()
