# beta

import pygame, sys, os, random
import pymunk, math

# constants
SCREEN_SIZE = (800,800)
FPS = 120
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
EMOJI = pygame.image.load('emoji.png')

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
    
    
        
def object_circle(space,pos, size):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, size)
    space.add(body, shape)
    return shape

def object_rect(space,pos, width, height):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    vs = [(0, 600), (800, 600), (800, 100), (0, 200)]
    vx = [(0, 700), (800, 700), (800, 800), (0, 800)] # <---
    
    sb = [(0,-100), (  0,-100), (  0,-700), (0,-700)]
    

    shape = pymunk.Poly(body, vs)
    space.add(body, shape)
    return shape

     
def draw_playground(circles, rects):
    for circle in circles:
        x = int(circle.body.position.x)
        y = int(circle.body.position.y)
        pygame.draw.circle(screen, WHITE,  (x,y),circle.radius)   
    for rect in rects:
        x = int(rect.body.position.x)
        y = int(rect.body.position.y)
        # pygame.draw.rect(screen, GREEN,  (0,700, 800, 100))
        pygame.draw.polygon(screen,GREEN,[(0,700), (800,700),(800,800),(0,800)])



# pymunk setup
space = pymunk.Space()
space.gravity = (0,GRAVITY)

# pygame setup
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

emojis = []
circles = []
rects = []
# rects.append(object_rect(space, (0,600), 800, 100))

pixels = []


def pixel(pos,thickness=20):
        x = pos[0]
        y = pos[1]
        t = int(thickness / 2)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        vs = [( - t,-t),(+t,-t),(-t,+t),(+t,+t)]

        shape = pymunk.Poly(body, vs)
        space.add(body, shape)    


def draw_pixel(thickness=20, color =RED ):
    
    for pos in pixels:
        x = pos[0]
        y = pos[1]
        t = int(thickness / 2)
        pygame.draw.rect(screen, color , (x-t,y-t, thickness, thickness))




point = (0,0)

screen.fill((217,217,217))

enable_dots = True
clicked= False
while True:
    # track events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            # clear
            if event.key == pygame.K_c:
                screen.fill((217,217,217))
            
            # enter
            if event.key == pygame.K_RETURN:
                enable_dots = not enable_dots
                print(enable_dots)


        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            if enable_dots:
                pass
            else:
                emojis.append(Emoji(pos= event.pos))
        
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
            
            
        if clicked:  
            if enable_dots:
                pixels.append(event.pos)
                pixel(event.pos)

           
            
            
    # while body   
    space.step(1/50)
    screen.fill((217,217,217))
    for emoji in emojis:
        emoji.draw()

    # draw_playground(circles, rects)
    
    draw_pixel()
ASWB 
    
    pygame.display.update()
    clock.tick(FPS) # frame per sec
    