import random


def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def darken(color,darkeningFactor = 8):
    
    if darkeningFactor != 0:
        newr = color[0]//darkeningFactor
        newg = color[1]//darkeningFactor
        newb = color[2]//darkeningFactor
        return (newr,newg,newb)
    return color 