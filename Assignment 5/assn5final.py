import pygame
pygame.init()
class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, background):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.background = background      
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (0, 0, 255), (15, 15), 15) 
        self.rect = self.image.get_rect()      
        self.rect.center = (320, 240)      
        self.dx = -3
        self.dy = -5   
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        self.checkBounds()           
    def checkBounds(self):
        """ bounce on encountering any screen boundary; iterate as necessary """       
        if self.rect.right >= self.screen.get_width():
            self.dx *= -1
        if self.rect.left <= 0:
            self.dx *= -1
        if self.rect.bottom >= self.screen.get_height():
            self.dy *= -1
        if self.rect.top <= 0:
            self.dy *= -1
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Boundary-checking: bounce")
    
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    #create your instances here
    ball1 = Ball (screen, background)
    ball1.rect.center = (100,240)
    ball2 = Ball (screen, background)
    ball2.rect.center = (300,240)
    ball2.dx = 5
    ball2.dy = 6
    pygame.draw.circle(ball2.image, (0, 255, 0), (15, 15,), 15)
    ball3 = Ball (screen, background)
    ball3.rect.center = (500,240)
    ball3.dx = 3
    ball3.dy = -4
    pygame.draw.circle(ball3.image, (255, 0, 0), (15, 15,), 15)
    #create your group here and populate it with your instances
    ballSprites = pygame.sprite.Group(ball1, ball2, ball3)  
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        #define what happens when ball 1 collides with another ball; iterate this to cover every possible combination
        if ball1.rect.colliderect(ball2.rect):
            ball1.dx *= -1
            ball1.dy *= -1
            ball2.dx *= -1
            ball2.dy *= -1
        if ball1.rect.colliderect(ball3.rect):
            ball1.dx *= -1
            ball1.dy *= -1
            ball3.dx *= -1
            ball3.dy *= -1
        if ball2.rect.colliderect(ball3.rect):
            ball3.dx *= -1
            ball3.dy *= -1
            ball2.dx *= -1
            ball2.dy *= -1       
        ballSprites.clear(screen, background)
        ballSprites.update()
        ballSprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
