""" lander.py 
    lunar lander program using gameEngine
"""
import random

##Lander will rotate or slide off the platform if < 50% of Lander's bottom boundary is touching the top boundary of the platform. (15 points) This may be accomplished two ways:
##By using of a proxy object for collision detection (layered on top of the platform)
##By comparing the x/y position of the lander to the x/y position of the platform
##Add an additional force beside gravity (i.e. wind); have an on-screen button or keyboard input to do this (10 points)
##Add moving barriers or constraints that may disrupt a good landing (5 points per item, 2 max)
##Add a NPC to shoot at the lander. It doesn't have to continuously fire at the lander, but the NPC should be able to aim and shoot autonomously. (10 points)
##Extra Credit: Incrementally increase the difficulty after each successful landing. (5 points)
##import pygame, sceneEngine, spriteEngine, uiEngine, random
import pygame

import sceneEngine
import spriteEngine
import uiEngine

level = 1


#invisible sprite for collision detection
class ProxyObject(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.imageMaster = pygame.transform.scale(self.imageMaster, (5, 5))
        self.platform = Platform(self)
        self.y = platform.y
        self.x = platform.x
        

#creates the 1st barrier
class BarrierOne(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("asteroid_vesta.jpg")
        self.x = 400
        self.y = 160
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y))
        self.imageMaster = pygame.transform.scale(self.imageMaster, (25, 25))

#creates the 2nd barrier
class BarrierTwo(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("asteroid_vesta.jpg")
        self.x = 400
        self.y = 360
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y)) 

#creates the enemy that will fire 
class EnemyNPC(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        #self.thrust = .2
        #self.sideThrust = .08
        self.setImage("enemynpc.gif")
        self.setAngle(180)
        self.x = 10
        self.y = 160 

#creates bullet  
class Bullet(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("bullet.gif")
        self.imageMaster = pygame.transform.scale(self.imageMaster, (5, 5))
        self.reset()
#This starts the movement of the bullet       
    def fire(self):
        self.setPosition((self.scene.enemynpc.x, self.scene.enemynpc.y))
        self.setSpeed(12)
        #self.setAngle(self.scene.enemynpc.rotation)
#Resets the bullet        
    def reset(self):
        self.setPosition ((-100, -100))        
#creates moonlander
class Lander(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.thrust = .1
        self.sideThrust = .05
        self.setImage("lander.gif")
        self.setAngle(90)
        self.inFlight = True
        self.inWind = False

    def checkEvents(self):
        self.checkKeys()
        
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        #if you press up you do reverse thrust
        if keys[pygame.K_UP]:
            self.dy -= self.thrust
            self.inFlight = True
        #sets the left trust     
        if keys[pygame.K_LEFT]:
            self.dx += self.sideThrust
            self.inFlight = True
        #sets the right thrust          
        if keys[pygame.K_RIGHT]:
            self.dx -= self.sideThrust
            self.inFlight = True

        #turns on wind 
        if keys[pygame.K_SPACE]:
            self.inWind = True
        self.updateVector()
        
class Platform(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("platform.gif")
        self.imageMaster = \
            pygame.transform.scale(self.imageMaster, (50,20))
        self.reset()
        #starts the enemy NPC fire
        self.scene.bullet.fire()   
        
    def reset(self):
        #pick random position on screen
        self.x = random.randint(0, self.screen.get_width())
        
        #make sure it's in bottom half of screen
        screenHeight = self.screen.get_height()
        self.y = random.randint(screenHeight/2, screenHeight)

        #How you might change the angle  
    def changeAngle(self):
        for i in range(50):
            self.setAngle(i)

class Game(sceneEngine.Scene):
    def __init__(self):
        sceneEngine.Scene.__init__(self)
        self.setCaption("Lunar Lander - arrow key to begin")
        self.lander = Lander(self)
        #create instance of enemy NPC
        self.enemynpc = EnemyNPC(self)
        #create a bullet for the enemy npc to shoot
        self.bullet = Bullet(self)
        #sets platform to land on
        self.platform = Platform(self)
        #creates first barrier
        self.barrierone = BarrierOne(self)
        #create 2nd barrier
        self.barriertwo = BarrierTwo(self)

        #info label created here. 
        self.lblInfo = uiEngine.Label()
        self.lblInfo.center = (320, 20)
        self.lblInfo.size = (300, 30)

        self.sprites = [self.lander, self.bullet, self.barrierone, self.enemynpc, self.platform, self.lblInfo]
        self.gravity = .02
        self.wind = .05
    
    def update(self):
        #add force of gravity
        if self.lander.inFlight == True:
            self.lander.addDY(self.gravity)
        #add wind whne pressing space     
        if self.lander.inWind == True:
            self.lander.addDX(self.wind)
        self.checkLanding()
        
        self.updateInfo()
        
    def checkLanding(self):
        #check collisions
        if self.lander.collidesWith(self.platform):
            #check for good landing
            if self.lander.dx < 10.5:
                if self.lander.dx > -10.5:
                    if self.lander.dy >= 0:
                        if self.lander.dy < 1:
                            print ("nice landing")
                            print(self.lander.dy)
                            print(self.lander.dx)
                        else:
                            print ("too much vertical velocity")
                            print(self.lander.dy)
                            print(self.lander.dx)
                    else:
                        badDY = self.lander.dy
                        print ("must approach from top %.2f" % badDY)
                else:
                    print ("going too fast to left")
            else:
                print ("going too fast to right")
            
            self.lander.dx = 0
            self.lander.dy = 0
            self.lander.updateVector()
            self.lander.inFlight = False

    def updateInfo(self):
        info = "dx: %.2f, dy: %.2f" % (self.lander.dx, self.lander.dy)
        self.lblInfo.text = info


#This is the Win Game Message
class WinGame(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0x00, 0x00, 0x00))
        self.center = (300,250)
        self.win = 100
        self.text = str(self.win)
#This is the Win status Message
    def changeWin(self):
        self.text = "You WIN!"      
#This is the Lose Game Message
class LoseGame(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0x00, 0x00, 0x00))
        self.center = (300,250)
        self.lose = 100
        self.text = str(self.lose)
#This is the Lose message
    def changeLose(self):
        self.text = "You Lost"      
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
