import sys
import pygame
import time
import random
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


# from alien import Alien


def run_game():
    pygame.init()

    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    bg_color = (230, 230, 230)

    # alien = Alien(ai_settings,screen)

    while True:
        gf.check_events(ai_settings, screen, stats,
                        play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # bullets.update()

        # for bullet in bullets.copy():
        # 	if bullet.rect.bottom <= 0:
        # 		bullets.remove(bullet)
        # if len(bullets) > 0:
        # 	print("bullets counts = ",len(bullets))

        gf.update_screen(ai_settings, screen, stats, sb,
                         ship, aliens, bullets, play_button)
    # for event in pygame.event.get():
    # 	if event.type == pygame.QUIT:
    # 		sys.exit()
    # else:
    # bg_color = (random.random()*100,random.random()*200,random.random()*150)
    # bg_color = (255, 0, 0)
    # screen.fill(bg_color)
    # screen.fill(ai_settings.bg_color)
    # ship.blitme()
    # pygame.display.flip()
    # time.sleep(2)


run_game()
