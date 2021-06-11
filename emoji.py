import pygame, sys, os, random
import pymunk

# constants
SCREEN_SIZE = (800,800)
FPS = 120
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
EMOJI = pygame.image.load('emoji.png') # downloaded from https://emojipedia.org/
GRAVITY = 250


class Emoji:
    global space
    global screen
    def __init__(self, pos):
        self.image = get_random_emoji_images()
        self.body = pymunk.Body(1,1, body_type= pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, int(self.image.get_height()/2))
        space.add(self.body, self.shape)
    def draw(self):
        x = int(self.body.position.x)
        y = int(self.body.position.y)
        emoji_rec = self.image.get_rect(center= (x,y))
        screen.blit(self.image, emoji_rec)
        
           
def get_random_emoji_images():
    path = './emojis/'
    images = os.listdir(path)
    rand = random.randint(0,len(images)-1)
    return pygame.image.load(path+"/"+ images[rand])
    
    
# playground / exprimental         
def playground():
    # circle 01
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (505,405)
    shape = pymunk.Circle(body, 100)
    space.add(body, shape)
    x = int(body.position.x)
    y = int(body.position.y)
    pygame.draw.circle(screen, WHITE,  (x,y),100)
    # circle 02    
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (150,700)
    shape = pymunk.Circle(body, 200)
    space.add(body, shape)
    x = int(body.position.x)
    y = int(body.position.y)
    pygame.draw.circle(screen, WHITE,  (x,y),200)
    # ground      
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos = (0,600)
    width = 800
    height = 100
    vs = [pos, (width, pos[1]), (width, height), (pos[0], height)]
    shape = pymunk.Poly(body, vs)
    space.add(body, shape)   
    x = int(body.position.x)
    y = int(body.position.y)
    pygame.draw.rect(screen, GREEN,  (0,700, 800, 100))
    


# pymunk setup
space = pymunk.Space()
space.gravity = (0,GRAVITY)

# pygame setup
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

emojis = []

while True:
    # track events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            emojis.append(Emoji(pos= event.pos))
           
                       
    # while body   
    screen.fill((217,217,217))
    space.step(1/50)
    
    for emoji in emojis:
        emoji.draw()

    playground()
    
    pygame.display.update()
    clock.tick(FPS) # frame per sec
    