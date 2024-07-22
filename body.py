import random
import pygame
import colorManipulation 
class Block():

    def __init__(self,sizex,sizey,color):
        self.image = pygame.Surface((sizex,sizey))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        pass
    
    def place(self,x,y):
        self.rect.centerx = x
        self.rect.centery = y
    
    def move(self,x,y):
        self.rect.centerx += x
        self.rect.centery += y

class Body():


    def __init__(self):
        self.skincolor = colorManipulation.randomColor()
        self.skincolor2 = colorManipulation.darken(self.skincolor,2)
        headsize = random.randint(20,50)
        bodyheight = random.randint(20,50)
        headshrunk = random.randint(0,2)
        
        self.head = Block(headsize+headshrunk,headsize,self.skincolor)
        self.head.move(-(headsize+headshrunk)//2,-headsize//2)
        
        self.neck = Block(headsize//2,headsize//2*4,self.skincolor2)
        self.neck.move(-headsize//3,headsize//3)
        # self.neck.move(headsize//4,0)
        
        self.body = Block(headsize+headsize//3,headsize+bodyheight,self.skincolor)
        self.body.move(-(headsize+headshrunk)//2,headsize)

        self.limb = Block(headsize+headsize//2,headsize*2,self.skincolor)


        self.order = [self.neck,self.body,self.head]

        pass

    def draw(self,screen):
        for block in self.order:
            screen.blit(block.image,block.rect)

    def move(self,x,y):
        for block in self.order:
            block.move(x,y)

# import pygame


pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True


newBody = Body()
newBody.move(1280//2,720//2)

while running: 
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill("black")



    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        newBody = Body()
        newBody.move(1280//2,720//2)

        pass
    
    newBody.draw(screen=screen)

    pygame.display.flip()
    
    pass