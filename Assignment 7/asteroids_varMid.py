""" asteroids.py """
import pygame, spriteEngine, sceneEngine, uiEngine, random
# https://realpython.com/asteroids-game-python/
##class Ship2(pygame.spirt.Sprite):


class Score(uiEngine.Label):
    def __init__(self, scene):
        uiEngine.Label.__init__(self)
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0xFF, 0xFF, 0xFF))
        self.center = (400,25)
        self.score = 0
        self.text = str(self.score)

    def changeScore(self, amtScore):
        self.score += amtScore 
        self.text = "score: %s" % (self.score)

class Lives(uiEngine.Label):
    def __int__(self, scene):
        self.fgColor = ((0xFF, 0xAA, 0x00))
        self.bgColor = self.bgColor = ((0xFF, 0xFF, 0xFF))
        self.center = (200,2)
        self.lives = 3
        self.text = str(self.lives)

    def changeLives(self, amtLives):
        self.lives -=  amtLives
        self.text = "lives: %s" % (self.lives)   



class ShipShield(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("shipSmall(shield).gif")
        self.setSpeed(2)
        self.setAngle(-60)
        self.x = 400
        self.y = 400
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
class Ship(spriteEngine.SuperSprite):
    def __init__(self, scene):
        spriteEngine.SuperSprite.__init__(self, scene)
        self.setImage("shipSmall.gif")
        self.setSpeed(2)
        self.setAngle(-60)
        self.x = 400
        self.y = 400
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
        self.reset()        
    def checkEvents(self):
        self.rotateBy(self.rotSpeed)       
    def reset(self):
        """ change attributes randomly """
        #set random position
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.setPosition((x, y))
        #set random size
        scale = random.randint(10, 50)
        self.setImage("asteroid_vesta.jpg")
        self.imageMaster = \
            pygame.transform.scale(self.imageMaster, (scale, scale))
        self.setSpeed(random.randint(0, 6))
        self.setAngle(random.randint(0, 360))
        self.rotSpeed = random.randint(-5, 5)
class Game(sceneEngine.Scene):
    def __init__(self):
        sceneEngine.Scene.__init__(self)
       
        self.ship = ShipShield(self)

        self.bullet = Bullet(self)
        self.score = Score(self)
        self.lives = Lives(self)
        
        self.rocks = []
        for i in range(10):
            self.rocks.append(Rock(self))
        self.rockGroup = self.makeSpriteGroup(self.rocks)
        self.addGroup(self.rockGroup)
        self.sprites = [self.bullet, self.ship, self.score]
        self.setCaption("Asteroids")         
    def update(self):
        rockHitShip = self.ship.collidesGroup(self.rocks)
        if rockHitShip:
            rockHitShip.reset()
            #self.lives.changeLives(1)
            #moves ship if hit
            
            
        rockHitBullet = self.bullet.collidesGroup(self.rocks)
        if rockHitBullet:
            rockHitBullet.reset()
            self.bullet.reset()
            self.score.changeScore(10)
            #add value to score
            
            
def main():
    game = Game()    
    game.start()   
if __name__ == "__main__":
    main()
