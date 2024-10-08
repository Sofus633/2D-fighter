import pygame 

running = True
hitboxes = []
hasbeenpressed = False
animation_frame = 0
animations = loadanimarions("file parh") # load all frame for eatch file format ["filename", [frameimage]
animation = []


def main():
    while running:
        display()
        checkinputs()
        


def checkinputs():
    keys = pygame.key.get_pressed()
    if keys[K_e]:
        
    if pygame.mouse.get_press() and not hasbeenpressed:
        hasbeenpressed = True
        pos1 = pygame.mouse.get_pos()
   else:
        hasbeenpressed = False
        pos2 = pygame.get_pos()
        hitboxes.append(pygame.Rect(pos1, pos2)
        animation_frame += 1 
        animation = animations[animation_frame]
        
        


    


def display():
    screen.blit(screen, animation
    for hitbox in hitboxes:
        pygam.draw.rect()  




if __name__ == "__main__":
    main()
