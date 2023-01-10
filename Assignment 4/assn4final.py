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
background.fill(white)                          #makes a white background
ball = pygame.image.load("ballimage.gif")       #returns a new surface with the image loaded onto it
ball.convert()                                  #converts the native pixel format of the image to SDL's format
ballrect = ball.get_rect()
clock = pygame.time.Clock()                     #set clock for pi speed 
adj_speed = 2
tickSpeed = 60
doNotMove = 0

def Speed():
    print(speed) #Outputs speed of movement of object
while 1:
    clock.tick(tickSpeed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Does Keydown event
            if event.key == pygame.K_UP: #if keyboard up is pressed do this
                speed[1] = -adj_speed #moves up on the on the y access
                speed[0] = doNotMove #does not move on the x access
                Speed()
            elif event.key == pygame.K_DOWN: #if keyboard down is pressed do this
               speed[1] = +adj_speed #moves down on the y access
               speed[0] = doNotMove  #does not move on the x access
               Speed()
            elif event.key == pygame.K_LEFT: #if keyboard left is pressed do this
                speed[1] = doNotMove #does not move on the y access
                speed[0] = -adj_speed
                Speed()
            elif event.key == pygame.K_RIGHT: #if keyboard right is pressed do this
                speed[1] = doNotMove #does not move on the y access
                speed[0] = +adj_speed
                Speed()
            elif event.key == pygame.K_q: #quit pygame on escape
                pygame.display.quit() #stops display
                pygame.quit() #stops sdl
                sys.exit() #exits application
            else:
                speed = defaultSpeed  #Stops movement by setting both speed for x and y to zero when no key is pressed
            ballrect = ballrect.move(speed) #Sets that speed to stop
    if ballrect.centerx > width: #If the ball x field is greater than the display width - represents the screens width, so this would be the right side.
        ballrect.centerx = 0  #Reset to Zero - this would reset the object's position to the left side of the screen.
    elif ballrect.centerx < 0: #If the ball x field is less than the dislpay width
        ballrect.centerx = width #Rest the ball x center to the width
    elif ballrect.centery > height:
        ballrect.centery = 0
    elif ballrect.centery < 0:
        ballrect.centery = height
    screen.blit(background, (backgroundcolor))  #draw the background
    screen.blit(ball, ballrect)                 #draw the player
    pygame.display.flip()                       #


    
