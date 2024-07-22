
import pygame
import colorManipulation
import noise
# import main
# from Tile import *
from world.gamechunk import *
import paralaxbackground

#tile = [[x,y],color,surface]
# y = 0 is the ground 




class World():
    
    def __init__(self):
        self.color1 = colorManipulation.randomColor()
        self.color2 = colorManipulation.randomColor()
        self.chunks = []
        startingChunk = Chunk(0,0,self.color1,self.color2,self)
        self.chunks.append(startingChunk)
        self.position = [0,0]


        self.background = paralaxbackground.ParalaxBackground(self.color1,self.color2)

        pass
    
    def update(self,position):
        # cord = (x,y)

        self.position = [position[0],position[1]]
        print(position[0],position[1])
        
        target_x = -((position[0]+0)//CHUNKSIZE*CHUNKSIZE)
        target_y = -((position[1]+0)//CHUNKSIZE*CHUNKSIZE)
        
        tar_chunk = (target_x,target_y)
        
        print(tar_chunk)

        if self.chunkDoesNotExistAt(target_x, target_y):
            self.createChunkAt(target_x, target_y)
        
        target_x = -((position[0]+0)//CHUNKSIZE*CHUNKSIZE)
        target_y = -((position[1]-CHUNKSIZE)//CHUNKSIZE*CHUNKSIZE)
        # tar_chunk = (tar_x,tar_y)
        # print(tar_chunk)
        if self.chunkDoesNotExistAt(target_x, target_y):
            self.createChunkAt(target_x, target_y)
        
        target_x = -((position[0]-CHUNKSIZE)//CHUNKSIZE*CHUNKSIZE)
        target_y = -((position[1]-0)//CHUNKSIZE*CHUNKSIZE)
        # tar_chunk = (tar_x,tar_y)s
        # print(tar_chunk)
        if self.chunkDoesNotExistAt(target_x, target_y):
            self.createChunkAt(target_x, target_y)
        
        target_x = -((position[0]+CHUNKSIZE)//CHUNKSIZE*CHUNKSIZE)
        target_y = -((position[1]-0)//CHUNKSIZE*CHUNKSIZE)
        # tar_chunk = (tar_x,tar_y)
        # print(tar_chunk)
        if self.chunkDoesNotExistAt(target_x, target_y):
            self.createChunkAt(target_x, target_y)

        
        target_x = -((position[0]+0)//CHUNKSIZE*CHUNKSIZE)
        target_y = -((position[1]+CHUNKSIZE)//CHUNKSIZE*CHUNKSIZE)
        # tar_chunk = (tar_x,tar_y)
        # print(tar_chunk)
        if self.chunkDoesNotExistAt(target_x, target_y):
            self.createChunkAt(target_x, target_y)
        

    def draw(self,screen,position):

        self.background.draw(screen)

        for chunk in self.chunks:
            screenreference = screen.get_rect()
            # screenreference.centerx = 0
            # screenreference.centery = 0
            movedrect = screenreference
            # movedrect.centerx += position[0]
            movedrect.centerx -= position[0]
            # movedrect.centery += position[1]
            movedrect.centery -= position[1]

            print(movedrect.centerx,movedrect.centery)
            if chunk.intersectsRect(screenreference,position):
                chunk.update(screen,position)
            # sur = pygame.surface.Surface((movedrect.width,movedrect.height))
            
            # sur.fill("gray")
            
            # rec = movedrect
            # rec.centerx += position[0]
            # rec.centery += position[1]
            # screen.blit(sur,rec)
        
        pass


    def createChunkAt(self, tar_x, tar_y):
        self.chunks.append(Chunk(tar_x,tar_y,self.color1,self.color2,self))
        # print("adding",tar_x,tar_y)


    def getChunk(self,x,y):
        for chunk in self.chunks:
            # print(chunk)
            if chunk.originMatchesCoords(x,y):
                return chunk
        return None
    

    def chunkDoesNotExistAt(self, tar_x, tar_y):
        answer = self.getChunk(tar_x,tar_y)
        if answer == None:
            return True
        return False

        print("Does not exist at",tar_x,tar_y)
        return answer
        

    pass