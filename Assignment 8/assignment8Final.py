""" assignment8.py 
    illustrates a multi-frame animation
"""

import pygame
pygame.init()

#creates the animation class for Paper Plane 
class Plane(pygame.sprite.Sprite):


    def __init__(self, screen):

        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        #Sets standing or if it's going to fold
        self.STANDING = 0
        self.FOLDING = 1

        #creates the image object to display
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        #These are variables used for the animation
        self.frame = 0
        self.delay = 3
        self.pause = 0
        self.state = self.STANDING

        self.dx = 2

    def update(self):
        if self.state == self.STANDING:
            self.image = self.imageStand
        elif self.state == self.FOLDING:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                #Sets the image stand still
                if self.frame >= len(self.planeImagesFold):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                #Starts the fold plane animation     
                else:
                    self.image = self.planeImagesFold[self.frame]
                
                

    #load the images 
    def loadImages(self):
        self.imageStand = pygame.image.load("images/pa_fold0000.jpg")
        self.imageStand = self.imageStand.convert()
        transColor = self.imageStand.get_at((1, 1))
        self.imageStand.set_colorkey(transColor)
        #loops paperplane fold images 
        self.planeImagesFold = []
        #does a loop of the images to create the animation up to image 9 
        for i in range(9):
            imgName = "images/pa_fold000%d.jpg" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.planeImagesFold.append(tmpImage)


#sets the screen variable for the size
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Press Space to make plane fold")
#sets the background and call upon the screen variable
background = pygame.Surface(screen.get_size())
background.fill((0, 0x99, 0))
screen.blit(background, (0, 0))

#calls upon the plane class/ instance
plane = Plane(screen)
allSprites = pygame.sprite.Group(plane)

clock = pygame.time.Clock()
keepGoing = True
#Maps buttons for actions
while keepGoing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        #if key is pressed    
        elif event.type == pygame.KEYDOWN:
            #if key is space
            if event.key == pygame.K_SPACE:
                #if space is priced fold animatiion starts
                plane.state = plane.FOLDING
    #Clear screen then update then draw 
    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)
    
    pygame.display.flip()                    
