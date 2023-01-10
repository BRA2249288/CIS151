""" paper air force
    top-down flying game
    fly your paper airplane with mouse
    bomb targets
    avoid rain
    
    """
    
import pygame, sys
pygame.init()

screen = pygame.display.set_mode((640, 480))



class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/pa_fold0009.jpg")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
class NPC(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
          
        self.image = pygame.image.load("images/redplane.jpg")
        NPC_WIDTH, NPC_HEIGHT = 55, 40
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.dx = -3    
        self.dy = -5
        #self.rect = self.rect(700, 300, NPC_WIDTH, NPC_HEIGHT)
 



class Ocean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/ocean.gif")
        self.rect = self.image.get_rect()
        self.dy = 5

    
def game():
    pygame.display.set_caption("Paper Air Force")

  
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    plane = Plane()
    ocean = Ocean()
    npc = NPC()
    pygame.key.set_repeat(1,1)

    oceanSprites = pygame.sprite.Group(ocean)
    planeSprites = pygame.sprite.Group(plane, npc)
    npcSprites = pygame.sprite.Group(npc)
  


    clock = pygame.time.Clock()
    
    cntdwn = pygame.USEREVENT + 1 #Create a custom user event that will create a simple countdown timer and print to the shell window
    pygame.time.set_timer(cntdwn, 1000) #uses milliseconds
    cntdwn_sec = 10 #in seconds
    
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == cntdwn:
                if cntdwn_sec > 0:
                    cntdwn_sec -= 1
                    print("Countdown:",cntdwn_sec)
                else:
                    print("times up!")
                    keepGoing = False
        
        oceanSprites.update()
        planeSprites.update()
        
        oceanSprites.draw(screen)
        planeSprites.draw(screen)
        
        pygame.display.flip()

    pygame.mouse.set_visible(True) 
    




if __name__ == "__main__":
    game()
    
    
