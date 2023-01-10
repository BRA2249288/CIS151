import sys, pygame
pygame.init()
 
size = width, height = 320, 240             
speed = [0, 0]
black = 0, 0, 0
white = 255, 255, 255
backgroundcolor = [0,0]
defaultSpeed = [0,0]
screen = pygame.display.set_mode(size)          #sets the screen(window) size    
pygame.display.set_caption("Bouncing Ball")     #sets the caption in the title bar
background = pygame.Surface(screen.get_size())  #sets the background surface to the size of the screen
background = background.convert()               #converts the native pixel format of the image to SDL's format
background.fill(white)
ball = pygame.image.load("ballimage.gif")       #returns a new surface with the image loaded onto it
ball.convert()                                  #converts the native pixel format of the image to SDL's format
ballrect = ball.get_rect()
clock = pygame.time.Clock()
adj_speed = 2
tickSpeed = 60
doNotMove = 0
while 1:
    clock.tick(tickSpeed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed[1] = -adj_speed
                speed[0] = doNotMove
            else:
                speed = defaultSpeed
            ballrect = ballrect.move(speed)   
            if event.key == pygame.K_DOWN:
               speed[1] = +adj_speed
               speed[0] = doNotMove
            else:
               speed = defaultSpeed    
            ballrect = ballrect.move(speed)
            if event.key == pygame.K_LEFT:
                speed[1] = doNotMove
                speed[0] = -adj_speed
            else:
                speed = defaultSpeed
            ballrect = ballrect.move(speed)
            if event.key == pygame.K_RIGHT:
                speed[1] = doNotMove
                speed[0] = +adj_speed
            else:
                speed = defaultSpeed
            ballrect = ballrect.move(speed)
    screen.blit(background, (backgroundcolor))              #draw the background
    screen.blit(ball, ballrect)                 #draw the player
    pygame.display.flip()                       #


    
