import pygame 
from animations import cutimg
import json
running = True
hitboxes = []
hasbeenpressed = False
screen = pygame.display.set_mode((1000, 800))

NAME = "atk1.png"


animations = cutimg(NAME, 100) # load all frame for eatch file format ["filename", [frameimage]
animation = [[] for i in range(len(animations))]
animation_frame = 0
clock = pygame.time.Clock()
time = pygame.time.get_ticks()
timerE = pygame.time.get_ticks()
pos1 = None
pos2 = None
displaysize = 10
pygame.font.init()
my_font = pygame.font.SysFont('Lucida Console', 30)

def main(screen):
    
    while running:
        time = pygame.time.get_ticks()
        display(screen)
        checkinputs(time)
        pygame.display.flip()
        screen.fill(0)
        clock.tick(60)


def checkinputs(time):
    global animation_frame
    global timerE
    global pos1
    global pos2
    global hasbeenpressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                if len(animation[animation_frame]) > 0:
                    animation[animation_frame].remove(animation[animation_frame][0])
        if event.type == pygame.MOUSEWHEEL:
            print(event.y)
            if event.y > 0:
                print("Scrolled up")
            elif event.y < 0:
                print("Scrolled DOWN")
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if  event.button == 1 : 
                hasbeenpressed = True
                pos1 = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            if  event.button == 1  : 
                hasbeenpressed = False
                print("realease")
                pos2 = pygame.mouse.get_pos()
                print(pos1, pos2)
                #animation[animation_frame].append(pygame.Rect((pos1[0]/ 100, pos1[1]/ 100), ((pos2[0] - pos1[0] )/ 100, (pos2[1] - pos1[1])/ 100 )))
                animation[animation_frame].append([(pos1[0]/ 100, pos1[1]/ 100), ((pos2[0] - pos1[0] )/ 100, (pos2[1] - pos1[1])/ 100 )])

                
                
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e] and timerE < time:
        if animation_frame + 1 < len(animations):
            animation_frame += 1 
        else:
            animation_frame = 0
        timerE = time + 500
    if keys[pygame.K_a] and timerE < time:
        createjson(animation)
        timerE = time + 500
        

        
        

def createjson(animation):
    with open("hitboxes.json", "r") as json_file:
        loaded_data = json.load(json_file)
    print("Original Data:")
    print(loaded_data)

    loaded_data["characteran"][NAME] = animation


    with open("hitboxes.json", "w") as json_file:
        json.dump(loaded_data, json_file, indent=4)
    print("\nUpdated Data:")
    print(loaded_data)
        
    


def display(screen):
    global animation_frame
    global hasbeenpressed
    global pos1
    global displaysize
    global my_font
    screen.blit(pygame.transform.scale(animations[animation_frame], (100 * displaysize, 100 * displaysize)))
    text_surface = my_font.render(NAME, False, (255, 255, 255))
    screen.blit(text_surface, (10, 10))
    text_surface2 = my_font.render(str(animation_frame), False, (255, 255, 255))
    screen.blit(text_surface2, (500, 10))
    #screen.blit(animations[animation_frame], (100 , 100 ))
    for hitbox in animation[animation_frame]:
        
        resized_rect = pygame.Rect(hitbox[0][0] * 100, hitbox[0][1] * 100 , hitbox[1][0] *  100, hitbox[1][1] *  100)
        pygame.draw.rect(screen, (0, 0, 255), resized_rect)
        
    if hasbeenpressed:
        pos2 = pygame.mouse.get_pos()    
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((pos1[0], pos1[1]), ((pos2[0] - pos1[0]) , (pos2[1] - pos1[1]) )))




if __name__ == "__main__":
    main(screen)
