import pygame 

running = True
hitboxes = []
hasbeenpressed = False


def main():
    while running:
        display()
        checkinputs()


def checkinputs():
    keys = pygame.key.get_pressed()
    if pygame.mouse.get_press() and not hasbeenpressed:
        hasbeenpressed = True
        pos1 = pygame.mouse.get_pos()
   else:
        hasbeenpressed = False
        pos2 = pygame.get_pos()
        hitboxes.append(pygame.Rect(pos1, pos2)


    


def display():
    for hitbox in hitboxes:
        pygam.draw.rect()  




if __name__ == "__main__":
    main()
