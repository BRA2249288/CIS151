""" paper air force
    top-down flying game
    fly your paper airplane with mouse
    bomb targets
    avoid rain
    
    """
    
import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((640, 480))
oceanImage = "images/ocean.gif"
spaceImage = "images/space.png"



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
        
class NPC(pygame.sprite.Sprite):   #new NPC plane class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/redplane.jpg")
        self.image = self.image.convert()
        self.image = pygame.transform.flip(self.image, False, True)
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.npc_x = random.randrange(0, screen.get_width())
        self.rect.center = (self.npc_x, 50)
        self.dx = 5
        self.dy = 5
        
    def update(self):
        self.rect.centerx += self.dx
        self.boundaryCheck()
    def boundaryCheck(self):
        if self.rect.centerx >= screen.get_width():
            self.dx *= -1
        elif self.rect.centerx <= 0:
            self.dx *= -1    
        
class Bullet(pygame.sprite.Sprite):
     def __init__ (self):
        pygame.sprite.Sprite. __init__ (self)
        self.image = pygame.Surface((15,15))
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image, (0,0,0), (7,7), 7)
        self.rect = self.image.get_rect()
     def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)

class Ocean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(oceanImage)
        self.rect = self.image.get_rect()
        self.dy = 5
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(spaceImage)
        self.rect = self.image.get_rect()
        self.dy = 5        
   
def game():
    pygame.display.set_caption("Paper Air Force")

  
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    plane = Plane()
    ocean = Ocean()
    space = Space()
    bullet = Bullet()
    npc = NPC()
    pygame.key.set_repeat(1,1)

    oceanSprites = pygame.sprite.Group(ocean)
    spaceSprites = pygame.sprite.Group(space)
    planeSprites = pygame.sprite.Group(plane, npc)
    bulletSprites = pygame.sprite.Group(bullet)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet()
                    bulletSprites.add(bullet)
                    bullet.rect.center = plane.rect.center
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
    
    
