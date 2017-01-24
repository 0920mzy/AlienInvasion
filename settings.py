class Settings():
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (230,230,230)

		self.ship_speed_factor = 5

		self.bullet_speed_factor = 10
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 10

		self.alien_speed_factor = 300
		self.fleet_drop_speed = 10
		self.fleet_direction = 1

		self.ship_limit = 3

		self.speedup_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 5
		self.bullet_speed_factor = 10
		self.alien_speed_factor = 300

		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale