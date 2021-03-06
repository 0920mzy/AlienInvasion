import sys

import pygame

import game_function as gf

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
       
def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("alien invasion")

	play_button = Button(ai_settings, screen, "Play")

	ship = Ship(ai_settings, screen) 
	#alien = Alien(ai_settings, screen)
	aliens = Group()
	bullets = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens) 
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)


	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()