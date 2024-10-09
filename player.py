import pygame
from vector import Vector2

MAXVELO = 5


class Player:
    def __init__(self, position, color):
        self.color = color
        self.life =  100
        self.spawnpoint = position
        self.position = position
        self.velocity = Vector2(0, 1)
        self.apparence = pygame.Rect(list(self.position), [50, 100]) #hitbox
        self.friction = Vector2(.5, .5)
        self.onground = False
        self.dirrection = "left"
        self.punchcooldown = pygame.time.get_ticks()
        self.ground = None
        
    def update(self):
        self.position = self.velocity + self.position
        
        self.apparence = pygame.Rect(list(self.position), [50, 100])
    
        self.updatevelo()
        
    def updatevelo(self):
        if self.velocity[0] > 0:
            self.velocity[0] = self.velocity[0] - self.friction[0]
        if self.velocity[0] < 0:
            self.velocity[0] = self.velocity[0] + self.friction[0]
        if self.velocity[1] > 0:
            self.velocity[1] = self.velocity[1] - self.friction[1]
        if self.velocity[1] < 0:
            self.velocity[1] = self.velocity[1] + self.friction[1]
        
        if self.velocity[0] > MAXVELO:
            self.velocity[0] = MAXVELO
        if self.velocity[0] < -MAXVELO:
            self.velocity[0] = -MAXVELO

        if self.onground == False:
            self.velocity = self.velocity + [0, 1]
            
    def toutchground(self, obj):
        self.onground = True
        self.velocity[1] = 0

        self.position[1] = obj.position[1] - 99
        self.ground = obj.position[1] - 100
        
    def endground(self):
        self.onground = False   
        self.ground = None
    
    def respawn(self):
        self.position = self.spawnpoint
        self.life = 100
        
    def attack(self, name, attackhitbox):
        time = pygame.time.get_ticks()
        print(self.punchcooldown, time)
        if time > self.punchcooldown:
            self.punchcooldown = time + 1000
            if name == "punch":
                rect =  pygame.Rect([list(self.position)[0] + (50 if self.dirrection == "right" else -70), list(self.position)[1]], [70, 50])
                attackhitbox.append([rect , self, 10])
