import pygame
import decors
import player
import time 
from vector import Vector2
from animations import Attackhitbox

def display(screen, objects, hitboxes):
    for object in objects:
        if type(object) == player.Player:
            pygame.draw.rect(screen, object.color, object.apparence)
            text_surface = my_font.render(str(object.life), False, (255, 255, 255))
            screen.blit(text_surface, (list(object.position)[0], list(object.position)[1] - 100))
        elif type(object.apparence) == pygame.Rect:
            pygame.draw.rect(screen, (255, 0, 0), object.apparence)
        else:
            pygame.Surface.blit(screen ,object.apparence)
    for hitbox in hitboxes:
        pygame.draw.rect(screen, (0, 0, 255), hitbox[0])
        hitbox[2] -= 1
        if hitbox[2] < 0:
            hitboxes.remove(hitbox)


def checkcollitions(objects):
    for object in objects:
        if player1.apparence.colliderect(object.apparence):
            player1.toutchground(object)
        else:
            player1.endground() 
            
        if player2.apparence.colliderect(object.apparence):
            player2.toutchground(object)
        else:
            player2.endground() 

def checkifhit(hitboxes,hitablethings):
    for hitbox in hitboxes:
        for object in hitablethings:
            if hitbox[0].colliderect(object.apparence) and object is not hitbox[1]:
                object.life -= 10
                hitboxes.remove(hitbox)
    

if __name__ == "__main__":
    pygame.init()
    pygame.font.init() 
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    SCREENSIZE = [1000, 800]
    screen = pygame.display.set_mode((1000, 800))
    bloc1 = decors.Bloc((100, 800-10), (1000-200, 10))
    player1 =  player.Player(Vector2(300, 0), (0, 255, 0))
    player2 = player.Player(Vector2(800, 0), (255, 255, 255))
    
    
    todisplay = [bloc1, player1, player2]
    tocollide = [bloc1]
    running = True
    hitablethings = [player1, player2]
    attackhitbox = []
    
    punchclock = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    animation = Attackhitbox()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        keys = pygame.key.get_pressed()
        # ------------------------------------------------- player1
        if keys[pygame.K_s]:
            if not player1.onground:
                player1.velocity[1] += 1
        if keys[pygame.K_z]:
            if player1.onground:
                player1.velocity[1] -= 20
                         
        if keys[pygame.K_d]:
            player1.velocity[0] += 1
            player1.dirrection = "right"
                
        if keys[pygame.K_q]:
            player1.velocity[0] -= 1
            player1.dirrection = "left"
            
        if keys[pygame.K_e]:       
            player1.attack("punch", attackhitbox)
            checkifhit(attackhitbox, hitablethings)
        # ------------------------------------------------- player2
        if keys[pygame.K_k]:
            if not player2.onground:
                player2.velocity[1] += 1
                
                
        if keys[pygame.K_i]:
            if player2.onground:
                player2.velocity[1] -= 20    
                     
        if keys[pygame.K_l]:
            player2.velocity[0] += 1
            player2.dirrection = "right"
            
        if keys[pygame.K_j]:
            player2.velocity[0] -= 1
            player2.dirrection = "left"
            
        if keys[pygame.K_o]:

            player2.attack("punch", attackhitbox)
            checkifhit(attackhitbox, hitablethings)
        
            
        if player1.position[1] > SCREENSIZE[1] or player2.position[1] > SCREENSIZE[1] or player1.life <= 0 or player2.life <= 0:
            player1.respawn() 
            player2.respawn() 
            
        player1.update()
        player2.update()
        checkcollitions(tocollide)
        display(screen, todisplay, attackhitbox)
        pygame.display.flip()
        screen.fill(0)
        clock.tick(60)
                    
