import pygame
from pygame.locals import *
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define game variables
tile_size = 50
game_over = 0
main_menu = True
level = 0
max_levels = 2


#load images
sun_img = pygame.image.load('img/star.png')
bg_img = pygame.image.load('img/night.png')
restart_img = pygame.image.load('img/restart_btn.png')
start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')


def reset_level(level):
    playerone.reset(100, screen_height - 130)
    playertwo.reset(60, screen_height - 130)
    badguy_group.empty()
    badground_group.empty()
    exit_group.empty()
    
    #load in level data and create world
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data)

    return world 
    

class Button():
   def __init__(self, x, y, image):
       self.image = image
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.clicked = False

   def draw(self):
       action = False    
       screen.blit(self.image, self.rect)

       #get mouse
       pos = pygame.mouse.get_pos()

       #check mouseover and click conditions

       if self.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
               action = True
               self.clicked = True

       if pygame.mouse.get_pressed()[0]:
           self.clicked = False

       return action    

           
                   
                   


class PlayerOne():
        def __init__(self, x, y):
            self.reset(x, y)

        def update(self, game_over):
                dx = 0
                dy = 0
                walk_cooldown = 5

                if game_over == 0:

                        #get keypresses
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                                self.vel_y = -15
                                self.jumped = True
                        if key[pygame.K_SPACE] == False:
                                self.jumped = False
                        if key[pygame.K_LEFT]:
                                dx -= 5
                                self.counter += 1
                                self.direction = -1
                        if key[pygame.K_RIGHT]:
                                dx += 5
                                self.counter += 1
                                self.direction = 1
                        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                                self.counter = 0
                                self.index = 0
                                if self.direction == 1:
                                        self.image = self.images_playeroneright[self.index]
                                if self.direction == -1:
                                        self.image = self.images_playeroneleft[self.index]


                        #handle animation
                        if self.counter > walk_cooldown:
                                self.counter = 0        
                                self.index += 1
                                if self.index >= len(self.images_playeroneright):
                                        self.index = 0
                                if self.direction == 1:
                                        self.image = self.images_playeroneright[self.index]
                                if self.direction == -1:
                                        self.image = self.images_playeroneleft[self.index]


                        #add gravity
                        self.vel_y += 1
                        if self.vel_y > 10:
                                self.vel_y = 10
                        dy += self.vel_y

                        #check for collision
                        self.in_air = True 
                        for tile in world.tile_list:
                                #check for collision in x direction
                                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                        dx = 0
                                #check for collision in y direction
                                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        #check if below the ground i.e. jumping
                                        if self.vel_y < 0:
                                                dy = tile[1].bottom - self.rect.top
                                                self.vel_y = 0
                                        #check if above the ground i.e. falling
                                        elif self.vel_y >= 0:
                                                dy = tile[1].top - self.rect.bottom
                                                self.vel_y = 0
                                                self.in_air = False 

                        #check for collision with enemies
                        if pygame.sprite.spritecollide(self, badguy_group, False):
                            game_over = -1

                        #check for collision with bad ground  
                        if pygame.sprite.spritecollide(self, badground_group, False):
                            game_over = -1

                        #check for collision with exit
                        if pygame.sprite.spritecollide(self, exit_group, False):
                                game_over = 1    
                            

           


                        #update player coordinates
                        self.rect.x += dx
                        self.rect.y += dy
                elif game_over == -1:
                    self.image = self.dead_image
                    if self.rect.y > 200:
                        self.rect.y -= 5 
                        

                #draw player onto screen
                screen.blit(self.image, self.rect)
                pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

                return game_over 



        def reset(self, x, y):
               self.images_playeroneright = []
               self.images_playeroneleft = []
               self.index = 0
               self.counter = 0
               for num in range(1, 5):
                   img_playeroneright = pygame.image.load(f'img/guy{num}.png')
                   img_playeroneright = pygame.transform.scale(img_playeroneright, (40, 80))
                   img_playeroneleft = pygame.transform.flip(img_playeroneright, True, False)
                   self.images_playeroneright.append(img_playeroneright)
                   self.images_playeroneleft.append(img_playeroneleft)
               self.dead_image = pygame.image.load('img/ghost.png')        
               self.image = self.images_playeroneright[self.index]
               self.rect = self.image.get_rect()
               self.rect.x = x
               self.rect.y = y
               self.width = self.image.get_width()
               self.height = self.image.get_height()
               self.vel_y = 0
               self.jumped = False
               self.direction = 0
               self.in_air = True 
               
class PlayerTwo():
        def __init__(self, x, y):
             self.reset(x, y)

        def update(self, game_over):
                dx = 0
                dy = 0
                walk_cooldown = 5

                if game_over == 0:

                        #get keypresses
                        key = pygame.key.get_pressed()
                        if key[pygame.K_w] and self.jumped == False and self.in_air == False:
                                self.vel_y = -15
                                self.jumped = True
                        if key[pygame.K_w] == False:
                                self.jumped = False
                        if key[pygame.K_a]:
                                dx -= 5
                                self.counter += 1
                                self.direction = -1
                        if key[pygame.K_s]:
                                dx += 5
                                self.counter += 1
                                self.direction = 1
                        if key[pygame.K_a] == False and key[pygame.K_RIGHT] == False:
                                self.counter = 0
                                self.index = 0
                                if self.direction == 1:
                                        self.image = self.images_playertworight[self.index]
                                if self.direction == -1:
                                        self.image = self.images_playertwoleft[self.index]


                        #handle animation
                        if self.counter > walk_cooldown:
                                self.counter = 0        
                                self.index += 1
                                if self.index >= len(self.images_playertworight):
                                        self.index = 0
                                if self.direction == 1:
                                        self.image = self.images_playertworight[self.index]
                                if self.direction == -1:
                                        self.image = self.images_playertwoleft[self.index]


                        #add gravity
                        self.vel_y += 1
                        if self.vel_y > 10:
                                self.vel_y = 10
                        dy += self.vel_y

                        #check for collision
                        self.in_air = True 
                        for tile in world.tile_list:
                                #check for collision in x direction
                                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                        dx = 0
                                #check for collision in y direction
                                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        #check if below the ground i.e. jumping
                                        if self.vel_y < 0:
                                                dy = tile[1].bottom - self.rect.top
                                                self.vel_y = 0
                                        #check if above the ground i.e. falling
                                        elif self.vel_y >= 0:
                                                dy = tile[1].top - self.rect.bottom
                                                self.vel_y = 0
                                                self.in_air = False 

                        #check for collision with enemies
                        if pygame.sprite.spritecollide(self, badguy_group, False):
                            game_over = -1

                        if pygame.sprite.spritecollide(self, badground_group, False):
                            game_over = -1

                         #check for collision with exit
                        if pygame.sprite.spritecollide(self, exit_group, False):
                                game_over = 1    
                              
                            

           


                        #update player coordinates
                        self.rect.x += dx
                        self.rect.y += dy
                elif game_over == -1:
                    self.image = self.dead_image
                    if self.rect.y > 200:
                        self.rect.y -= 5 
                        

                #draw player onto screen
                screen.blit(self.image, self.rect)
                pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

                return game_over 



        def reset(self, x, y):
                self.images_playertworight = []
                self.images_playertwoleft = []
                self.index = 0
                self.counter = 0
                for num in range(1, 5):
                        img_playertworight = pygame.image.load(f'img/buy{num}.png')
                        img_playertworight = pygame.transform.scale(img_playertworight, (40, 80))
                        img_playertwoleft = pygame.transform.flip(img_playertworight, True, False)
                        self.images_playertworight.append(img_playertworight)
                        self.images_playertwoleft.append(img_playertwoleft)
                self.dead_image = pygame.image.load('img/ghost.png')        
                self.image = self.images_playertworight[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0
                self.in_air = True 

class World():
        def __init__(self, data):
                self.tile_list = []

                #load images
                dirt_img = pygame.image.load('img/dirt.png')
                grass_img = pygame.image.load('img/grass.png')

                row_count = 0
                for row in data:
                        col_count = 0
                        for tile in row:
                                if tile == 1:
                                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                                        img_rect = img.get_rect()
                                        img_rect.x = col_count * tile_size
                                        img_rect.y = row_count * tile_size
                                        tile = (img, img_rect)
                                        self.tile_list.append(tile)
                                if tile == 2:
                                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                                        img_rect = img.get_rect()
                                        img_rect.x = col_count * tile_size
                                        img_rect.y = row_count * tile_size
                                        tile = (img, img_rect)
                                        self.tile_list.append(tile)
                                if tile == 3:
                                        badguy = EnemeyNPC(col_count * tile_size, row_count * tile_size + 15)
                                        badguy_group.add(badguy)
                                if tile == 6:
                                        badground = BadGround(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                                        badground_group.add(badground)
                                if tile == 8:
                                        exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                                        exit_group.add(exit)                                    
                                col_count += 1
                        row_count += 1

        def draw(self):
                for tile in self.tile_list:
                        screen.blit(tile[0], tile[1])
                        pygame.draw.rect(screen, (255, 255, 255), tile[1], 1)



class EnemeyNPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/badguy.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0 

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 50:
            self.move_direction *= -1
            self.move_counter *= -1
        

class BadGround(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/badground.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y    


playerone = PlayerOne(100, screen_height - 130)
playertwo = PlayerTwo(60, screen_height - 130)

badguy_group = pygame.sprite.Group()
badground_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

#FindWorld()
#load in level data and create world
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
world = World(world_data)


#create buttons
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

run = True
while run:

        clock.tick(fps)

        screen.blit(bg_img, (0, 0))
        screen.blit(sun_img, (100, 100))


        if main_menu == True:   
                if exit_button.draw():
                        run = False
                if start_button.draw():
                        main_menu = False
        else:
                world.draw()

                if game_over == 0:                
                    badguy_group.update()
                    
                badguy_group.draw(screen)
                badground_group.draw(screen)
                exit_group.draw(screen)

                game_over = playerone.update(game_over)
                game_over = playertwo.update(game_over)
                #if player has died
                if game_over == -1:
                    if restart_button.draw():
                        world_data = []
                        world = reset_level(level)
                        game_over = 0
                #if player has completed the level
                if game_over == 1:
                #reset game and go to next level
                    level += 1
                    if level <= max_levels:                           
                            world_data = []
                            world = reset_level(level)
                            game_over = 0
                    else:
                            if restart_button.draw():
                                    level = 1
                                    #reset level
                                    world_data = []
                                    world = reset_level(level)
                                    game_over = 0 
                
                
       
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()

pygame.quit()
