from world.tile import *
import random
import pythonperlin
import noise.perlin
import pygame
import colorManipulation

class Chunk():
    
    def __init__(self,originx,originy,color1,color2,worldParent,terrainstartheight=0,):
        self.chunk_data = []
        
        self.color1 = color1
        self.color2 = color2
        self.active = False
        self.origin = (originx,originy)

        self.findAdjacent(worldParent=worldParent)
        self.generateChunk(originx,originy,terrainstartheight=terrainstartheight)

        self.rect = pygame.rect.Rect(originx,originy,CHUNKSIZE,CHUNKSIZE)
        self.rect.centerx = originx+CHUNKSIZE//2
        self.rect.centery = originy+CHUNKSIZE//2
        pass
    
    def generateChunk(self,originx,originy,terrainstartheight = 0):
        self.origin = (originx,originy)

        for y in range(self.origin[1],self.origin[1]+CHUNKSIZE,TILESIZE):
            for x in range(self.origin[0],self.origin[0]+CHUNKSIZE,TILESIZE):
                newchunkcoords = (x,y)
                # colorpick = pythonperlin.perlin((30,4),7,8)[0][1]
                colorpick = 1
                if colorpick == 1:
                    newcolor = self.color1
                else:
                    newcolor = self.color2
                # newtile = [[x,y],newcolor,0]
                newtile = Tile([x,y],newcolor,0)
                newtile.findAdjacent(self)
                self.chunk_data.append(newtile)
        
        newperlin = pythonperlin.perlin((100,4),100,2)
        newheightx = self.origin[0]
        for coords in newperlin:
            newheight = int(coords[0]*TILESIZE)+terrainstartheight
            coords[1] = newheight*3
            
            coords[0] = newheightx//TILESIZE
            # newheightx += TILESIZE
            
        
        height = []
        for coords in newperlin:
            newcoords = int(coords[1]//50)*50+100
            height.append(newcoords)
            print(height)  
        
        for x in range(originx,originx+CHUNKSIZE,TILESIZE):
            for y in range(originy,originy+CHUNKSIZE,TILESIZE):
                newx = ((x-originx)//TILESIZE) 
                print(newx,y)  
                if y < height[newx]:
                    self.erase(x,y)
                    self.erase(x+TILESIZE,y)
                    self.setBlockColor(x,y+TILESIZE,(self.color2))
                    self.setBlockColor(x+TILESIZE,y+TILESIZE,(self.color2))
                    # self.erase(x-TILESIZE,y)

        self.checkShadows() 
        pass

    def findAdjacent(self,worldParent):
        self.above = worldParent.getChunk(self.origin[0],self.origin[1]-CHUNKSIZE)
        self.below = worldParent.getChunk(self.origin[0],self.origin[1]+CHUNKSIZE)
        self.left = worldParent.getChunk(self.origin[0]-CHUNKSIZE,self.origin[1])
        self.left = worldParent.getChunk(self.origin[0]+CHUNKSIZE,self.origin[1])
        pass

    def checkShadows(self):
        for tile in self.chunk_data:
            tile.calcShadow()

    def setBlockColor(self,x,y,color):
        for tile in self.chunk_data:
            if tile.position[0] == x and tile.position[1] == y:
                tile.color = color
        
        
        
        pass 
    
    

    def erase(self,x,y):
        
        for tile in self.chunk_data:
            if tile.position[0] == x and tile.position[1] == y:
                self.chunk_data.remove(tile)
                print("erased x ",x," y ",y ," ref ",x//TILESIZE,y//TILESIZE)

    def update(self,screen,position):
        

        self.draw(screen, position)

    def getTile(self,x,y):
        for tile in self.chunk_data:
            if tile.position == [x,y]:
                return tile
        if not (self.above == None):
            tile = self.above.getTile(x,y)
            if tile != None:
                return tile
        if not (self.below == None):
            tile = self.below.getTile(x,y)
            if tile != None:
                return tile
        
        return None
        pass 

    def draw(self, screen, position):
        for tile in self.chunk_data:
            newsurface = pygame.Surface((TILESIZE,TILESIZE))
            newsurface.fill(colorManipulation.darken(tile.color,tile.shadow))
            newrect = newsurface.get_rect()
            newrect.centerx = tile.position[0]+position[0]
            newrect.centery = tile.position[1]+position[1]
            screen.blit(newsurface,newrect)

        
        pass

    pass

    def intersectsRect(self,rect,position = (0,0)):
       
        if self.rect.colliderect(rect):
            return True 
            
        return False
        

    def originMatchesCoords(self,x,y):
        if self.origin == (x,y):
            return True
        return False
