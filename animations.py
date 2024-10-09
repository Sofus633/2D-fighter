

import pygame

def cutimg(imgpath, size):
    spritesheet = pygame.image.load(imgpath).convert_alpha()
    sheet_width, sheet_height = spritesheet.get_size()
    sprites = []
    for x in range(0, sheet_width, size):
        sprite = spritesheet.subsurface(pygame.Rect(x, 0, size, sheet_height))
        sprites.append(sprite)
    return sprites


class Attackhitbox:
    def __init__(self):
        self.hitboxes = []
    def frametodisplay(self):
        lst = []
        for hitbox in self.hitboxes:
            hitbox[1]  -= 1
            lst.append(hitbox[0])
        return lst