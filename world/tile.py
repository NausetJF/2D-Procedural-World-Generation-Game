import random

TILESIZE = 50
CHUNKSIZE = 25*TILESIZE

class Tile():
    def __init__(self,position = (0,0),color = (0,0,0),shadow = 0) -> None:
        self.position = position
        self.color = color
        self.shadow = shadow
        
        
        pass
    
    def getSave(self):
        # implement 
        
        pass 

    def findAdjacent(self,chunkParent):
        self.above = chunkParent.getTile(self.position[0],self.position[1]-TILESIZE)
        self.left = chunkParent.getTile(self.position[0]-TILESIZE,self.position[1])
        self.below = chunkParent.getTile(self.position[0],self.position[1]+TILESIZE)
        self.right = chunkParent.getTile(self.position[0]+TILESIZE,self.position[1])
        
        pass
    
    def calcShadow(self):
        if self.above != None: 
            othershadow = 0
            if self.left != None:
                newshadow = self.left.shadow % 5
                othershadow += random.randint(0,newshadow)
            if self.right != None:
                newshadow = self.left.shadow % 5
                othershadow += random.randint(0,newshadow)
            self.shadow += 1+self.above.shadow
            # self.shadow = 0
            pass
    
    pass

