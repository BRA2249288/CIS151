""" lander.py 
    lunar lander program using gameEngine
"""
import pygame
import sceneEngine
import spriteEngine
import uiEngine
import random 

#set the first level 
level = 1
#This was created to keep track of life
class Life(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0x00, 0x00, 0x00))
        self.center = (100,25)
        #starts with 10 units of health
        self.life = 10
        self.text = str(self.life)
#This changes the life
    def changeLife(self, amtLife):
        self.life -= amtLife #this will subtract the number given
        self.text = "Life: %s" % (self.life) #this updates the life  
#invisible sprite for collision detection
        
class ProxyObjectOne(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("blank.png")#created a blank image
        #attempted 25, 1 but 25,25 gave a better more realistic result
        self.imageMaster = pygame.transform.scale(self.imageMaster, (25, 25))
        #self.imageMaster = pygame.transform.scale(self.imageMaster, (25, 1))
        self.platform = Platform(self)
        #sets to position so it can check the x and y from the lander to the platform
        self.setPosition((self.scene.platform.x -30, self.scene.platform.y -15))
        #starts the NPC to shoot felt this was the easiest way to put it
        self.scene.platform.bulletShoot()
        #sets transparency even though this is a jpg
        tranColor = self.image.get_at((0, 0))
        self.image.set_colorkey(tranColor)
        
class ProxyObjectTwo(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("blank.png")#created a blank image 
        #attempted 25, 1 but 25,25 gave a better more realistic result
        self.imageMaster = pygame.transform.scale(self.imageMaster, (25, 25))
        #self.imageMaster = pygame.transform.scale(self.imageMaster, (25, 1))
        self.platform = Platform(self)
        #sets to position so it can check the x and y from the lander to the platform
        self.setPosition((self.scene.platform.x +30, self.scene.platform.y -15))
        #sets transparency even though this is a jpg
        tranColor = self.image.get_at((0, 0))
        self.image.set_colorkey(tranColor)
        
    
#creates the 1st barrier
class BarrierOne(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        #no transparent layer in .jpg files 
        self.setImage("asteroid_vesta.jpg")
        #sets position
        self.x = 400
        self.y = 160
        #Sets angle and speed
        self.setSpeed(1)
        self.setAngle(160)
        #creates at a random position off the width and height
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y))
        #scales the image
        self.imageMaster = pygame.transform.scale(self.imageMaster, (25, 25))
        #sets transparency even though this is a jpg
        tranColor = self.image.get_at((0, 0))
        self.image.set_colorkey(tranColor)
        
#creates the 2nd barrier
class BarrierTwo(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        #no transparent layer in .jpg files 
        self.setImage("asteroid_vesta.jpg")
        #sets position
        self.x = 400
        self.y = 360
        #Sets angle and speed
        self.setSpeed(1)
        self.setAngle(110)
        #creates at a random position off the width and height
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y))
        #scales the image
        self.imageMaster = pygame.transform.scale(self.imageMaster, (25, 25))
        #sets transparency even though this is a jpg
        tranColor = self.image.get_at((0, 0))
        self.image.set_colorkey(tranColor)
        
#creates the 3rd barrier
class BarrierThree(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        #same settings as above just different position and angle and speed increase for difficulty for level 2
        self.setImage("asteroid_vesta.jpg")
        self.x = 300
        self.y = 310
        self.setSpeed(2)
        self.setAngle(65) 
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y))
        self.imageMaster = pygame.transform.scale(self.imageMaster, (25, 25))
        
#creates the enemy that will fire 
class EnemyNPC(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        #sets image
        self.setImage("enemynpc.gif")
        #sets the angle to fire upon lander
        self.setAngle(180)
        #sets position
        self.x = 10
        self.y = 160 

#creates bullet to be fire upon
class Bullet(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("bullet.gif")
        #sets the scale size 
        self.imageMaster = pygame.transform.scale(self.imageMaster, (5, 5))
        self.reset()
#This starts the movement of the bullet       
    def fire(self):
        self.setPosition((self.scene.enemynpc.x, self.scene.enemynpc.y))
        self.setSpeed(12)
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
        #starts off in flight
        self.inFlight = True
        #starts off with no Wind you press space to start the Wind
        self.inWind = False
    def checkEvents(self):
        self.checkKeys()        
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        #if you press up key you do reverse thrust
        if keys[pygame.K_UP]:
            self.dy -= self.thrust
            self.inFlight = True
        #sets the left trust for left key    
        if keys[pygame.K_LEFT]:
            self.dx += self.sideThrust
            self.inFlight = True
        #sets the right thrust  for right key         
        if keys[pygame.K_RIGHT]:
            self.dx -= self.sideThrust
            self.inFlight = True
        #added the down for fun 
        if keys[pygame.K_DOWN]:
            self.dy += self.thrust
            self.inFlight = True    
        #turns on wind by pressing space 
        if keys[pygame.K_SPACE]:
            self.inWind = True
        self.updateVector()
        
class Platform(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("platform.gif")
        self.imageMaster = \
            pygame.transform.scale(self.imageMaster, (60,20))
        self.reset()       
    #starts the enemy NPC fire
    def bulletShoot(self):    
        self.scene.bullet.fire()        
    def reset(self):
        #pick random position on screen
        self.x = random.randint(0, self.screen.get_width())        
        #make sure it's in bottom half of screen
        screenHeight = self.screen.get_height()
        self.y = random.randint(screenHeight/2, screenHeight)

class Game(sceneEngine.Scene):
    def __init__(self):
        sceneEngine.Scene.__init__(self)
        self.setCaption("Lunar Lander - arrow key to begin")
        #This has been broken up into Levels and Level 2 right now has an additional barrier
        if level == 1:            
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
            #create proxy object one
            self.proxyobjectone = ProxyObjectOne(self)
            #create proxy object two
            self.proxyobjecttwo = ProxyObjectTwo(self)
            #info label stored here
            self.lblInfo = uiEngine.Label()
            self.lblInfo.center = (320, 20)
            self.lblInfo.size = (300, 30)
            #Life bar to keep track
            self.life = Life(self)
            #Sprites to use
            self.sprites = [self.lander, self.bullet, self.life, self.barrierone, self.barriertwo, self.proxyobjectone,  self.proxyobjecttwo, self.enemynpc, self.platform, self.lblInfo]
            #sets the default gravity variable
            self.gravity = .02
            #sets the default Wind variable
            self.wind = .02
        if level == 2:         
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
            #create 3rd barrier for level 2 to make it harder
            self.barrierthree = BarrierThree(self)
            #create proxy object one
            self.proxyobjectone = ProxyObjectOne(self)
            #create proxy object two
            self.proxyobjecttwo = ProxyObjectTwo(self)
            #info label stored here
            self.lblInfo = uiEngine.Label()
            self.lblInfo.center = (320, 20)
            self.lblInfo.size = (300, 30)
            self.life = Life(self)
            self.sprites = [self.lander, self.bullet, self.life, self.barrierone, self.barriertwo, self.barrierthree, self.proxyobjectone,  self.proxyobjecttwo, self.enemynpc, self.platform, self.lblInfo]
            #sets the default gravity variable
            self.gravity = .02
            #sets the default Wind variable
            self.wind = .02
#This checks the proxy and if it's 50% off it will fall off the platform. Attempted to get it to 50% as possible give or take.
    def checkProxy(self):       
        landerHitProxyOne = self.lander.collidesWith(self.proxyobjectone)
        if landerHitProxyOne:
            print("hit proxy one") 
            self.lander.dx = self.lander.dx - .1
            #rotates off the edge
            #for i in range(50):
                #self.lander.setAngle(i)
        landerHitProxyTwo = self.lander.collidesWith(self.proxyobjecttwo)
        if landerHitProxyTwo:
            print("hit proxy two")
            self.lander.dx = self.lander.dx + .1
              #rotates off the edge
              #for i in range(50):
              #self.lander.setAngle(i)
#This checks the different barriers to see if they hit the lander for level 2 it checks for the additional barrier            
    def checkRockHit(self):
        landerHitRockOne = self.lander.collidesWith(self.barrierone)
        if landerHitRockOne:
            self.life.changeLife(1)#substracts one life
            self.lander.dx = self.lander.dy + .3#Moves the lander away from the platform to disrupt a good landing
        landerHitRockTwo = self.lander.collidesWith(self.barriertwo)
        if landerHitRockTwo:
            self.life.changeLife(1)#substracts one life
            self.lander.dx = self.lander.dy + .3#Moves the lander away from the platform
        if level == 2 : #If level 2 check for third barrier    
           landerHitRockThree = self.lander.collidesWith(self.barrierthree)
           if landerHitRockThree:
               self.life.changeLife(1)#substracts one life
               self.lander.dx = self.lander.dx + .5#Moves the lander away from the platform
               self.lander.dx = self.lander.dy + .5#Moves the lander away from the platform
    #Check to see if the NPC            
    def checkBulletHit(self):
        landerHitBullet = self.lander.collidesWith(self.bullet)
        if landerHitBullet:
            self.life.changeLife(1) #substracts one life      
    def update(self):
        #add force of gravity
        if self.lander.inFlight == True:
            self.lander.addDY(self.gravity)
        #add wind whne pressing space     
        if self.lander.inWind == True:
            #additional force beside gravity
            self.lander.addDX(self.wind)
        #runs the checkProxy function    
        self.checkProxy()
        #runs the checkLanding function
        self.checkLanding()
        #runs the checkRockHit function
        self.checkRockHit()
        #Updates the Information 
        self.updateInfo()       
    def checkLanding(self):
        #check collisions
        if self.lander.collidesWith(self.platform):
            #check for good landing
            if self.lander.dx < 10.5:
                if self.lander.dx > -10.5:
                    if self.lander.dy >= 0:
                        if self.lander.dy < 1:
                            if self.lander.dy == self.platform.dy:
                                #will print and go to level 2 if you land
                                print("you landed")
                                level = 2
                            else:
                                #this happens if you don't land yet if you are close to the edge you will fall off
                                print ("did not land yet")
                                print(self.lander.dy)
                                print(self.lander.dx)
                        else:
                            #have to watch your speed
                            print ("too much vertical velocity")
                            print(self.lander.dy)
                            print(self.lander.dx)
                    else:
                        #checks to see if you tried to weird angle
                        badDY = self.lander.dy
                        print ("must approach from top %.2f" % badDY)
                else:
                    #have to make sure your not going to fast to the left
                    print("going too fast to left")
                    #slows down the speed if going to fast
                    self.lander.dx = self.lander.dx + 5
            else:
                #have to make sure your not going to fast to the right
                print("going too fast to right")
                #slows down the speed if going to fast
                self.lander.dx = self.lander.dx - 5                     
            self.lander.dx = 0
            self.lander.dy = 0
            self.lander.updateVector()
            #disabled this for landing purposes
            #self.lander.inFlight = False

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
#This main starts the game        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
