class Settings:
    #A class to store all settings for Alien Invasion


    def __init__(self):
        #Initialize the game's settings
        #Screen settings
        self.screenResolution = (600, 400)
        self.backgroundColor = (230,230,230)
        #Ship Settings
        self.ship_speed = 0.65
        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3