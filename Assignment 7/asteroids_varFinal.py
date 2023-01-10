""" asteroids.py """
from tkinter import SW
import pygame, spriteEngine, sceneEngine, uiEngine, random
# https://realpython.com/asteroids-game-python/

sw = 640
sh = 480
StartGame = 1 

#This is the Score to keep track of how many asteroids you have destroyed. 
class Score(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0x00, 0x00, 0x00))
        self.center = (400,25)
        self.score = 0
        self.text = str(self.score)

    def changeScore(self, amtScore):
        self.score += amtScore 
        self.text = "Score: %s" % (self.score)

#This was created to keep track of life
class Life(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0x00, 0x00, 0x00))
        self.center = (100,25)
        self.life = 10
        self.text = str(self.life)

    def changeLife(self, amtLife):
        self.life -= amtLife 
        self.text = "Life: %s" % (self.life)        

#This is the Win Game Message
class WinGame(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0x00, 0x00, 0x00))
        self.center = (300,250)
        self.win = 100
        self.text = str(self.win)

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

    def changeLose(self):
        self.text = "You Lost"             

#The ship will start off with a shield and lose it if it crashes to many times
class ShipShield(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("shipSmall(shield).gif")
        self.w = self.image.get_width()
        self.h = self.image.get_height()      
        self.setSpeed(0)
        self.setAngle(0)
        self.x = sw//2
        self.y = sh//2
    def checkEvents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotateBy(10)
        if keys[pygame.K_RIGHT]:
            self.rotateBy(-10)
        if keys[pygame.K_UP]:
            self.addForce(.2, self.rotation)
        if keys[pygame.K_DOWN]:
            self.addForce(-.1, self.rotation)    
        if keys[pygame.K_SPACE]:
            self.scene.bullet.fire() 
#This was created to restore life             
class PowerUpItem(spriteEngine.SuperSprite):
     def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("powerup.gif") 
        self.setSpeed(1)
        self.setAngle(160) 
        self.x = sh/4
        self.y = sw/4
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
     #def reset(self):
      
  
class Bullet(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("bullet.gif")
        self.imageMaster = pygame.transform.scale(self.imageMaster, (5, 5))
        self.setBoundAction(self.HIDE)
        self.reset()       
    def fire(self):
        self.setPosition((self.scene.ship.x, self.scene.ship.y))
        self.setSpeed(16)
        self.setAngle(self.scene.ship.rotation)        
    def reset(self):
        self.setPosition ((-100, -100))
        self.setSpeed(0)          
class Rock(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("asteroid_vesta.jpg")
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.reset()  
             
    def checkEvents(self):
        self.rotateBy(self.rotSpeed)       
    def reset(self):
        """ change attributes randomly """
        #set random position     
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)  
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y))
        #set random size
        scale = random.randint(20, 50)
        size = scale 
        self.setImage("asteroid_vesta.jpg")
        self.imageMaster = \
            pygame.transform.scale(self.imageMaster, (scale, scale))
        self.setSpeed(random.randint(0, 6))
        self.setAngle(random.randint(0, 360))
        self.rotSpeed = random.randint(-5, 5)
    def spit(self):
        #size and rotation speed 
        rank = self.rect()
        print(rank)
        
     
             
class Game(sceneEngine.Scene):
    def __init__(self):
        sceneEngine.Scene.__init__(self)   
        self.screen = pygame.display.set_mode((sw, sh))    
        self.ship = ShipShield(self)
        self.bullet = Bullet(self)
        self.score = Score(self)
        self.life = Life(self)
        self.powerupitem = PowerUpItem(self)
        self.rocks = []
        #creates the amount of asteroids in this loop
        for i in range(10):
            self.rocks.append(Rock(self))
        #creates the asteroid group 
        self.rockGroup = self.makeSpriteGroup(self.rocks)
        self.addGroup(self.rockGroup)
        #This is the sprite group of what displays 
        self.sprites = [self.bullet, self.ship, self.score, self.life, self.powerupitem]
        self.setCaption("Asteroids")         
    def update(self):
        #This happens if the ship hits an asteroid
        rockHitShip = self.ship.collidesGroup(self.rocks)
        if rockHitShip:
            #if statement check for statement here up # run split method call temp rock and append it 
            #set to center where the rock was hit 
            
            rockHitShip.reset()
            #removes life when hits a rock
            self.life.changeLife(1)
            #changes the speed and angle of the ship when hit
            self.ship.setSpeed(-3)
            self.ship.setAngle(75)
                        #removes the shield after getting hit so many times
            if self.life.life < 6:       
             self.ship.setImage("shipSmall.gif")
            
            
        #This happens if the bullet hits the asteroid 
        rockHitBullet = self.bullet.collidesGroup(self.rocks)
        if rockHitBullet:
            rockHitBullet.reset()
            self.bullet.reset()
            Rock.spit(self)
            #add value to score
            self.score.changeScore(10)

        #This happens if ship connects with the powerup item this is how you gain life to get your shield back           
        rockHitPowerup = self.ship.collidesWith(self.powerupitem)
        if rockHitPowerup:
            self.life.changeLife(-1)
            self.powerupitem.remove()
           # self.powerupitem.reset()
            
            
def main():
    game = Game()    
    game.start()   
if __name__ == "__main__":
    main()
