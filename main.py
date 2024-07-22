import pygame
import world.world as world


pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True

world1 = world.World()

position = [0,0]
velocity = [0,720//2]

while running: 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill("black")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    if keys[pygame.K_w]:
        velocity[1] += 10

        pass
    if keys[pygame.K_s]:
        velocity[1] -= 10
        

        pass
    if keys[pygame.K_a]:
        velocity[0] += 10
        
        pass

    if keys[pygame.K_d]:
        velocity[0] -= 10
        

        pass
    if keys[pygame.K_r]:
        world1 = world.World()

        pass
    # position[0] += velocity [0]
    # position[1] += velocity [1]

    world1.update(velocity)
    world1.draw(screen,velocity)
    keys = pygame.key.get_pressed()
    


    
    pygame.display.flip()
    fps = clock.get_fps()
    pygame.display.set_caption(str(fps))
    clock.tick(60)
    pass