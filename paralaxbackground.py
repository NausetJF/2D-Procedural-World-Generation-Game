import random 
import pygame
import colorManipulation
class ParalaxBackground:
    
    def __init__(self,color1,color2):

        self.color1 = color1
        self.color2 = color2
        possibleterrainshape = ["circle","square","triangle"]
        self.hillshape = random.choice(possibleterrainshape)
        print(self.hillshape)
        self.layers = []
        
        self.generateBackground()


        pass

    def generateBackground(self):
        background = pygame.sprite.Sprite()
        background.image = pygame.Surface((1280,1280))
        background.image.fill(self.color1)
        background.rect = background.image.get_rect()
        self.layers.append(background)


    
    def update(self,screen):


        
        

        pass 


    def draw(self,screen):
        
        screen.blit(self.layers[0].image,self.layers[0].rect)
    pass 