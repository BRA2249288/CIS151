""" paper air force
    top-down flying game
    fly your paper airplane with mouse
    bomb targets
    avoid rain
    
    """
    
import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((640, 480))
#background image locations
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
    #plane follows the mouse    
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
#enemy Non-playable character         
class NPC(pygame.sprite.Sprite):   #new NPC plane class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #new custom image
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
    #Updates and checks the boundary   
    def update(self):
        self.rect.centerx += self.dx
        self.boundaryCheck()
    #if reaches boundary it resets the image   
    def boundaryCheck(self):
        if self.rect.centerx >= screen.get_width():
            self.dx *= -1
        elif self.rect.centerx <= 0:
            self.dx *= -1
    #resets the plane if hit        
    def reset(self):
        self.rect.center = (self.npc_x, 50)
        self.dx *= -1
        self.boundaryCheck()        

#This is used to go from the character to the NPC to simulate shooting        
class Bullet(pygame.sprite.Sprite):
     def __init__ (self):
        pygame.sprite.Sprite. __init__ (self)
        self.image = pygame.Surface((15,15))
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image, (0,0,0), (7,7), 7)
        self.rect = self.image.get_rect()
     #uses the mouse position   
     def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
#default background
class Ocean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(oceanImage)
        self.rect = self.image.get_rect()
        self.dy = 5
#new space background        
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(spaceImage)
        self.rect = self.image.get_rect()
        self.dy = 5        
   
def game():
    pygame.display.set_caption("Airplane fun")

  
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    plane = Plane()
    ocean = Ocean()
    #space is the added background
    space = Space()
    bullet = Bullet()
    npc = NPC()
    pygame.key.set_repeat(1,1)
    #sets the sprites
    #different sprit groups
    oceanSprites = pygame.sprite.Group(ocean) #creates the ocean background
    spaceSprites = pygame.sprite.Group(space) #creats space background
    planeSprites = pygame.sprite.Group(plane) #creates the character
    npcSprites = pygame.sprite.Group(npc) #Enemy NPC
    bulletSprites = pygame.sprite.Group(bullet) #Creates the bullet to be used to shoot from the plane
    clock = pygame.time.Clock()
    
    cntdwn = pygame.USEREVENT + 1 #Create a custom user event that will create a simple countdown timer and print to the shell window
    pygame.time.set_timer(cntdwn, 1000) #uses milliseconds
    cntdwn_sec = 10 #in seconds
    levelOne = 0 
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
            elif event.type == pygame.KEYDOWN: #checks for keydown
                if event.key == pygame.K_SPACE: #If space is pressed 
                    bullet = Bullet() #adds the bullet class
                    bulletSprites.add(bullet) #adds in bullet
                    bullet.rect.center = plane.rect.center #creates bullet
            if event.type == cntdwn:
                if cntdwn_sec > 0:
                    cntdwn_sec -= 1
                    print("Countdown:",cntdwn_sec)
                    shootNpcs = pygame.sprite.groupcollide(bulletSprites, npcSprites, True, False)
                    #checks to see if enemy is shot
                    if shootNpcs:
                     print("Enemy Hit")
                     npc.reset()
                     #changes background if hit
                     levelOne = 1
                else:
                    #changes background color back once time is up
                    levelOne = 0 
                    print("times up!")
                    keepGoing = False
            #checks to see if it needs to change the background       
            if levelOne == 0:
             oceanSprites.update()
            elif levelOne == 1:
             spaceSprites.update()
            #updates character and npc
            planeSprites.update()
            npcSprites.update()
            #this actually draws the background depending on if character was hit
            if levelOne == 0: 
             oceanSprites.draw(screen)
            elif levelOne == 1:
             spaceSprites.draw(screen)
            #draws characters
            planeSprites.draw(screen)
            npcSprites.draw(screen)
            pygame.display.flip()

    pygame.mouse.set_visible(True) 
    



if __name__ == "__main__":
    game()
    
    
