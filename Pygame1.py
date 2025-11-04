import pygame

pygame.init()

height_dis=800
width_dis=600
dis = pygame.display.set_mode((height_dis, width_dis))
pygame.display.set_caption('Snake Game')
car = pygame.image.load("Buggatti.jpeg")
christmas2 = pygame.image.load("Clours.jpeg")
carx = 350
cary = 350

def cars(carx,cary):
    dis.blit(car,(carx,cary))

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0
    
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
            elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
            elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
            elif event.key == pygame.K_SPACE:
                    y1_change = 0
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

    dis.blit(christmas2,(0,0))
    cars(x1,y1)

    if x1 >= height_dis or y1 >= width_dis or x1 <= 0 or y1 <= 0:
        game_over = True

    pygame.display.update()

    clock.tick(25)
