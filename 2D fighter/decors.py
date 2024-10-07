import pygame


class Bloc:
    def __init__(self, position, size) :
        self.position = position
        self.size = size
        self.apparence = pygame.Rect(self.position, self.size) #hitbox