import pygments
import pygame
import os
import time  # Getting the game time imported
import math
from handle_enemy import enemy,  enemy_collision, Node

pygame.init()
# WINDOW_WIDTH = 704
# WINDOW_HEIGHT = 320
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
#16:9^
WINDOW=pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
BLACK=(0,0,0)
WIN_EDGE = pygame.Rect(WINDOW_WIDTH//2 - 5, 0, 10, WINDOW_HEIGHT)
pygame.display.set_caption("TCA2")

TRAP_IMAGE = pygame.image.load(os.path.join('Assets', 'pngwing.com.png'))



COIN_IMAGE = pygame.image.load(os.path.join('Assets', 'coin_clear_background.png')).convert_alpha()# linking coin images with a asset
COIN_WIDTH = 20
COINT_HEIGHT = 20
COIN_COMP=pygame.transform.rotate(pygame.transform.scale(COIN_IMAGE, (COIN_WIDTH, COINT_HEIGHT)), 0)



BACKGROUND_TEST = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Grass_Sample.png')), (WINDOW_WIDTH, WINDOW_HEIGHT))

PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'test_sprite.png'))
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 30
PLAYER_COMP = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)#rotate redundant for now

COIN_IMAGE = pygame.image.load(os.path.join('Assets', 'pngtree-glossy-golden-coin-icon-png-image_2898883.jpg'))# linking coin images with a asset
player_score = 0  #Start of the game the player will have 0 ponits
MAZE_WALL=pygame.image.load(os.path.join('Assets', 'maze_wall_test.png'))

ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'monster2_test.png'))
ENEMY_WIDTH = 15
ENEMY_HEIGHT = 30
ENEMY_COMP = pygame.transform.rotate(pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT)), 0)

#Creating a class for player the main character
class Player(pygame.sprite.Sprite):
  
  def __init__(self,width, height, speed, max_health,player_image,x,y,health,score):
    #self.rect = pygame.Rect(2, 2, width, height) # linking pygame
    self.image=player_image
    self.speed = speed # Creating the variable 
    self.max_health = max_health
    self.health=health
    self.score=score

    self.rect=self.image.get_rect()
    self.rect.width = width
    self.rect.height = height
    self.rect.x=x
    self.rect.y=y

    pygame.sprite.Sprite.__init__(self)
    WINDOW = pygame.display.get_surface()

#Updating moveing block to block
def movement(entity,key_press):
    player=entity
    if move[pygame.K_a]:
        player.move_ip(-1,0) 
    elif move[pygame.K_d]:
        player.move_ip(1,0) 
    elif move[pygame.K_w]:
        player.move_ip(0,-1)
    elif move[pygame.K_s]:
        player.move_ip(0,1)


def draw_maze(level):
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == "x":
                WALL_X = x * TILE_SIZE
                WALL_Y = y * TILE_SIZE
                WINDOW.blit(MAZE_WALL, (WALL_X, WALL_Y))




#Loading level
def load_level():
    pass

#for enemy collision and for trap collision
def check_collision():
    pass

#For player animation
def player_animation():
    pass

#For enemy animation
def enemy_animation():
    pass

def draw_lives(entity):
    #display_surface = pygame.display.set_mode((X, Y))#
    health=str(entity.health)
    #print(health)
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render(health, True, black)
    textRect = text.get_rect()
    textRect.center = (100,500)
    WINDOW.blit(text, textRect)

def draw_coins(coins_list):
    for coin in coins_list:
        WINDOW.blit(COIN_COMP, (coin.rect.x, coin.rect.y))


# Making Class for the trap 
class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, TRAP_IMAGE):
        super().__init__()
        self.image = pygame.transform.scale(TRAP_IMAGE, (TILE_SIZE, TILE_SIZE)) # Getting the trap images from assets
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def draw_traps(traps_group):
    for trap in traps_group:
        WINDOW.blit(trap.image, trap.rect.topleft)


# Could be done in check_collision and creating a coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, COIN_IMAGE): 
        super().__init__()
        self.image = pygame.transform.scale(COIN_IMAGE, (TILE_SIZE, TILE_SIZE))  # Getting the image to the coin
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y    # 
# # Function to check for collisions with the player and coin
def coin_collision(player_init, coins_group):
    collected_coins=pygame.sprite.spritecollide(player_init, coins_group, True)       
    player_init.score +=len(collected_coins)





   #LOAD IMAGES

start_image=pygame.image.load(os.path.join('Assets', 'test_sprite.png'))

#start_image('6orceshd.png')


#botton class

class Button():
    def __init__(self, x, y, image):
        self.image= image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        WINDOW.blit (self.image,(self.rect.x, self.rect.y))


start_button = Button(100, 200, start_image)





black = (0, 0, 0)
white = (255, 255, 255)


   
# On the screen it will show the score 
font = pygame.font.Font(None, 36)
score_text = font.render(f"score: {player_score}", True, (255,255,255)) #Putting score in a dict and changing font to white
WINDOW.blit(score_text, (10,10)) # Size of text

pygame.display.update()

# Creating the time for the maze
pygame.init()
start_time = time.time() # The time the player starting and with the current time
time_limit = 3 * 60 # 60 seconds times 3 equals 3 mintues 

loop =True

while loop:

    elapsed_time = time.time() - start_time # The elapsed time will be calculate 
    if elapsed_time > time_limit:
      print("Better luck next time") # When going the past the time limit this message will show up 
      break # It will end the loop when past the set time limit 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False       # Need to write this code at the end 



black = (0, 0, 0)
white = (255, 255, 255)

level_1 = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "x  S        xx                  x      x",
    "x     C     xx      E          x       x",
    "x    xx                     x   x  xx  x", 
    "x    T    C     xxxxxxx  x  x      xx  x", 
    "x           x   xxxxxxx  x  x      xx  x",
    "x  xxxxxx   x  T    xxx  x  xxxx   xx  x",
    "x    xxx    x       xxx  x  xx     xx  x",
    "x    xxx    xxxxxxxxxxx  x  xx     xx  x",
    "xxx  xxx            xxx  x  xxxxxxxxxxxx",
    "xxx  xxx            xxx  x             x",
    "xxx  xxx  xxxxxxxx  xxx  x    T        x",
    "xxx  xxx            xxx  xxxxxxxxxxxxxxx",
    "x    xxx            xxx                x",
    "x   xxxxxxxxxxxxxxxxxx    C     P      x",
    "x   xxxxxxxxxxxxxxxxxxx                x",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",




]


level_1_no_obstacle= [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "x           xx                  x      x",
    "x           xx                 x       x",
    "x    xx                     x   x  xx  x", 
    "x               xxxxxxx  x  x      xx  x", 
    "x           x   xxxxxxx  x  x      xx  x",
    "x  xxxxxx   x       xxx  x  xxxx   xx  x",
    "x    xxx    x       xxx  x  xx     xx  x",
    "x    xxx    xxxxxxxxxxx  x  xx     xx  x",
    "xxx  xxx            xxx  x  xxxxxxxxxxxx",
    "xxx  xxx            xxx  x             x",
    "xxx  xxx  xxxxxxxx  xxx  x             x",
    "xxx  xxx            xxx  xxxxxxxxxxxxxxx",
    "x    xxx            xxx                x",
    "x   xxxxxxxxxxxxxxxxxx                 x",
    "x   xxxxxxxxxxxxxxxxxxx                x",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",




]

  
#creating level 2 
level_2 = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "x                        x           C x",
    "x                        x             x",
    "x    xxx       T         x      xxxxxxxx",
    "x    xxxxxxxxxxxxxxxx    x      x      x",
    "x                   x    x      x      x",
    "x                   x    x      x      x",
    "x      T      x     x    x      x      x",
    "x    xxxxxxxxxx     x    x      x      x",
    "x    x    C         x    x      x      x",
    "xxxxxx              x    x             x",
    "x         xxxxxxxxxxx    x     xxxxxxxxx",
    "x         xxx                  x   x S x",
    "x    x    xxx                T x   x   x",
    "x    x          xxxxxxxxxxxxxxxx   x E x",
    "x    x         C xxxx                  x",
    "x    xxxxxxxxxxxxxxx                   x",
    "x                                      x",
    "x                        x             x",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
]


 
level_2_no_obstacle = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "x                        xx            x",
    "x    xxx                 xx     xxxxxxxx",
    "x    xxxxxxxxxxxxxxxx    xx     x E    x",
    "x                   x    xx     x      x",
    "x               x   x    xx     xxx    x",
    "x   xxxxxxxxxxxxx   x    xx     xxx    x",
    "x   xx              x    xx     xxx    x",
    "xxxxxx              x    xx            x",
    "x        xxxxxxxxxxxx    xx    xxxxxxxxx",
    "x        xxxx                  x   x S x",
    "x   xx   xxxx                  x   x   x",
    "x   xx          xxxxxxxxxxxxxxxx   x   x",
    "x   xx          xxxx               x   x",
    "x   xxxxxxxxxxxxxxxx     x             x",
    "x                        xxxxxxxxxxxxxxx",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
]

level_3 = [

  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "x                                        x      x",
  "x                                        x      x",
  "x     x     x     T    xxxxxxxxx    xx   x      x",
  "x     x     x     x    x             x          x",
  "x     x     x     x    x      x       xxxxx     x",
  "x     x     x     x    x      x C        xx     x",
  "x     x     x     x    x      xxxxxxx    xx     x",
  "x     x     x     x    x            x    xx     x",
  "x     x     x     x    xxxxxxx    T x    xx  T  x",
  "x     x     x     x           x     x    xx     x",
  "x     x     x     x           x     x    xx     x",
  "x     x     x     x   xxx     x     x    xx     x",
  "x     x     x     x   T x     x     x    xxxxxxxx",
  "x   C x     x     x     x     x     x     x     x",
  "x     x     xxxxxxx     xxxxxxx     x     x     x",
  "x     x     x           xxx xxxx    x     x     x",
  "x     x     xxxxxxxxxxxxxx  C     xxx     x     x",
  "x     x                           x       x     x",
  "x     x                           x       x     x",
  "x     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx     x",
  "x                               S x  E          x",
  "x                               S x             x",
  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  
]

level_3_no_obstacle = [

  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "x                                         x",
  "x     x   x    T    xxxxxxxx    xxx   x   x",
  "x     x   x    x    x             x       x",
  "x     x   x    x    x     x       xxxx    x",
  "x     x   x    x    x     x          x    x",
  "x     x   x    x    x     xxxxxxx    x    x",
  "x     x   x    x    x           x    x    x",
  "x     x   x    x    xxxxxx      x    x    x",
  "x     x   x    x          x     x    x    x",
  "x     x   x    x   xxx    x     x    x    x",
  "x     x   x    x     x    x     x    xxxxxx",
  "x     x   x    x     x    x     x         x",
  "x     x   xxxxxx     xxxxxx     x    x    x",
  "x     x   x          xxxxxxx    x    x    x",
  "x     x   xxxxxxxxxxxxx       xxx    x    x",
  "x     x                       x      x    x",
  "x     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    x",
  "x                           S x  E        x",
  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  
]
TILE_SIZE = 24

current_level = level_1
current_level_no_obstacle=level_1_no_obstacle

loop=True
#Make player start at S
traps_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
for y, row in enumerate(current_level):
    for x, char in enumerate(row):
        if char == "S":
            player_x, player_y = x * TILE_SIZE, y * TILE_SIZE
        elif char == "P":
            enemy_x, enemy_y = x * TILE_SIZE, y * TILE_SIZE
        if char == "T":
            trap = Trap(x * TILE_SIZE, y * TILE_SIZE, TRAP_IMAGE)
            traps_group.add(trap)



maze_walls = []  #For collisions with player
traps_list = []
coins_list = []
for y, row in enumerate(current_level):
    for x, cell in enumerate(row):
        if cell == "x":
            wall_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            maze_walls.append(wall_rect)
        elif cell == "C":
            coin = Coin(x * TILE_SIZE, y * TILE_SIZE, COIN_IMAGE)  # The coin image will show and be place in the maze 
            coins_list.append(coin)
player_init = Player(PLAYER_WIDTH, PLAYER_HEIGHT, 100,50,PLAYER_IMAGE,player_x,player_y,101,5) #Creating a player as a object
enemy_init = enemy(ENEMY_WIDTH,ENEMY_HEIGHT,ENEMY_IMAGE,enemy_x,enemy_y,maze_walls)




start_time=time.time()
time_limit=3*60


  
  
while loop:

    old_player_x = player_init.rect.x
    old_player_y = player_init.rect.y
    old_enemy_x = enemy_init.rect.x
    old_enemy_y = enemy_init.rect.y 

    #WINDOW.fill((0,0,0))
    # pygame.draw.rect(WINDOW,(50,50,50),Player)
    WINDOW.blit(BACKGROUND_TEST, (0, 0))
    #pygame.draw.rect(WINDOW, BLACK, WIN_EDGE)
    #pygame.draw.rect(WINDOW, (255, 0, 0), player_init.rect)
    WINDOW.blit(PLAYER_COMP, (player_init.rect.x, player_init.rect.y))
    WINDOW.blit(ENEMY_COMP, (enemy_init.rect.x, enemy_init.rect.y))
    #WINDOW.fill(black) 
    draw_coins(coins_list)  # it will show the coins on the screen
    score_text = font.render(f"score: {player_init.score}", True, (255,255,255)) # it will show the player score on the top left in white text 
    WINDOW.blit(score_text, (10,10))  
    draw_maze(current_level) 
    

    move=pygame.key.get_pressed()
    if move:
        movement(player_init.rect,move)

    for wall_rect in maze_walls:
        if player_init.rect.colliderect(wall_rect):
            player_init.rect.x = old_player_x
            player_init.rect.y = old_player_y

    for coins in range(len(coins_list)):
        if player_init.rect.colliderect(coins_list[coins]):
            player_init.score += 1
            del coins_list[coins]
            break
    trap_collision = pygame.sprite.spritecollide(player_init, traps_group, True)
    if trap_collision:
        player_init.health -= 25
            
    enemy_init.enemy_to_player(player_init.rect,maze_walls)
    enemy_collision(player_init.rect,enemy_init.rect,player_init)
    draw_lives(player_init)


    if current_level[int(player_init.rect.y / TILE_SIZE)][int(player_init.rect.x / TILE_SIZE)] == 'E':
        if current_level==level_1:
            current_level=level_2
            current_level_no_obstacle=level_2_no_obstacle
        elif current_level==level_2:
            current_level=level_3
            current_level_no_obstacle=level_3_no_obstacle
        maze_walls = [] 
        traps_list = []
        coins_list = []
        for y, row in enumerate(current_level):
            for x, cell in enumerate(row):
                if cell == "x":
                    wall_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    maze_walls.append(wall_rect)
                elif cell == "C":
                    coin = Coin(x * TILE_SIZE, y * TILE_SIZE, COIN_IMAGE) 
                    coins_list.append(coin)
                elif cell == "S":
                    player_init.rect.x, player_init.rect.y = x * TILE_SIZE, y * TILE_SIZE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
            
    pygame.display.update()

    

       






    




