""" asteroids.py """
from tkinter import SW
import pygame, spriteEngine, sceneEngine, uiEngine, random
# https://realpython.com/asteroids-game-python/
#setting the screen to 640 by 480
sw = 640
sh = 480
#This is the Score to keep track of how many asteroids you have destroyed. 
class Score(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0x00, 0x00, 0x00))
        self.center = (400,25)
        self.score = -10
        self.text = str(self.score)
#This Changes the Score        
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
#This changes the life
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
#The ship will start off with a shield and lose it if it crashes to many times
class ShipShield(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("shipSmall(shield).gif")
        self.w = self.image.get_width()
        self.h = self.image.get_height()      
        self.setSpeed(0)
        self.setAngle(0)
        self.position = (sw//2, sh//2)
#Keyboard Events for the ship        
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
        self.setImage("powerup.png") 
        self.setSpeed(1)
        self.setAngle(160) 
        self.x = 400 #= sh/4
        self.y = 20 #= sw/4
        tranColor = self.image.get_at((0, 0))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.imageMaster = \
          pygame.transform.scale(self.imageMaster, (30, 30))
     #Resets the Power Up Item Randomly
     def reset(self):
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y)) 
#creates bullet  
class Bullet(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("bullet.gif")
        self.imageMaster = pygame.transform.scale(self.imageMaster, (5, 5))
        self.setBoundAction(self.HIDE)
        self.reset()
#This is what happens when space is pressed        
    def fire(self):
        self.setPosition((self.scene.ship.x, self.scene.ship.y))
        self.setSpeed(12)
        self.setAngle(self.scene.ship.rotation)
#Resets the bullet        
    def reset(self):
        self.setPosition ((-100, -100))
        self.setSpeed(0)
#Creates Asteroid or rock sprite        
class Rock(spriteEngine.SuperSprite):
    def __init__(self, scene):
        #this call upon the image and sets up the asteroid image
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("asteroid_vesta.jpg")
        self.reset()
    def checkEvents(self):
        self.rotateBy(self.rotSpeed)
#Resets the Rock       
    def reset(self):
        """ change attributes randomly """
        #set random position     
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y))
        #set random size
        self.scale = random.randint(10, 40)
        #Has to define scale as self and set as an int
        self.scale = int(self.scale)
        #sets the image on the reset 
        self.setImage("asteroid_vesta.jpg")
        self.imageMaster = \
            pygame.transform.scale(self.imageMaster, (self.scale, self.scale))
        self.setSpeed(random.randint(0, 6))
        self.setAngle(random.randint(0, 360))
        self.rotSpeed = random.randint(-5, 5)
#Used to split the rock to create another rock        
    def split(self, rank=3):
        #size and rotation speed 
        self.rotSpeed = random.randint(1,1)
        self.setPosition((self.rect.center))
        #checks scale to see if it needs to create a new sprite
        if self.scale > 16:
            self.scale = int(self.scale - 10)
        else:
            self.reset()
        #Sets a random speed to create it 
        self.setSpeed(random.randint(0,1))
        self.imageMaster = \
            pygame.transform.scale(self.imageMaster, (self.scale, self.scale))
        #sets the angle of the split
        self.dir -= 90
        self.setAngle(self.dir)
##Main Game Engine code                             
class Game(sceneEngine.Scene):
    def __init__(self):
        sceneEngine.Scene.__init__(self)
        #Set's display mode here 
        self.screen = pygame.display.set_mode((sw, sh))
        #Sprites being declared here
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
#Updates the screen        
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
            self.ship.setSpeed(random.randint(-3, -1))
            self.ship.setAngle(random.randint(60, 75))
            #removes the shield after getting hit so many times
            if self.life.life < 5:       
             self.ship.setImage("shipSmall.gif")
            #if you get enough powerup you can get the shield back
            if self.life.life > 6:
             self.ship.setImage("shipSmall(shield).gif")
            #This happens if you run out of life
            if self.life.text == "Life: 0": 
               print("Ship dies")      
        #This happens if the bullet hits the asteroid 
        rockHitBullet = self.bullet.collidesGroup(self.rocks)
        if rockHitBullet:
            #checks the scale to see if it needs to split
            if rockHitBullet.scale > 14:
               splitRock = Rock(self)
               rockHitBullet.split()
               self.rocks.append(splitRock)
               splitRock.scale = rockHitBullet.scale
               splitRock.rect.center = rockHitBullet.rect.center
               splitRock.dir = rockHitBullet.dir * -1
               #has to call upon sprites and finds out the position and scale from split
               rockHitBullet.split()
               splitRock.split()
               self.bullet.reset()
               self.rockGroup = self.makeSpriteGroup(self.rocks)
               self.addGroup(self.rockGroup)               
            #add value to score
               self.score.changeScore(10)
            else:
               rockHitBullet.reset()
        #This happens if you score 100 points    
        #if self.score.text == "Score: 100" :
            #print("Win Game")    #loops 
        #This happens if ship connects with the powerup item this is how you gain life to get your shield back           
        shipHitPowerup = pygame.sprite.collide_rect(self.powerupitem, self.ship)
        if shipHitPowerup:
            #even though it's -1 it actually add 1 life back when hitting the power up
            self.life.changeLife(-1)
            self.powerupitem.reset()            
def main():
    game = Game()    
    game.start()   
if __name__ == "__main__":
    main()
