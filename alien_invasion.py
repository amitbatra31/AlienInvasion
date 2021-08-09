import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard
def run_game():
    #Initialize game and create a screen object
    pygame.init()
    xyz = Settings()
    screen = pygame.display.set_mode((xyz.screen_width,xyz.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ai_settings = Settings()

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")


    # Create an instance to store game statistics and create scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship.
    ship = Ship(ai_settings, screen) 
    # Make a group to store bullets in.
    bullets = Group()
    # Make an alien.
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Start the main loop of the game
    while True:
        #Watch for keyboard and mouse input
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship,aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen,sb, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
       
        #Redraw the screen during each pass through the loop
        screen.fill(xyz.bg_color)
        ship.blitme()
        
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            # print(len(bullets))
        #Make the most recently drawn screen visible.
        pygame.display.flip()



    
run_game()
