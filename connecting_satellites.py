import pygame
import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT = 400

satellites = []
lines = []
next_satellite = 0

start_time = 0
total_time = 0
end_time = 0

number_of_satellite = 8

def create_satellites():
    global start_time
    for count in range(0, number_of_satellite):
        satellite = Actor("satellite")
        satellite._surf = pygame.transform.scale(satellite._surf, (40,40))
        satellite.pos = (random.randint(40, WIDTH-40),random.randint(40, HEIGHT-40))
        satellites.append(satellite)
    start_time=time()



def draw():
    global total_time
    screen.blit("background",(0,0))
    number = 1
    for satillite in satellites:
        screen.draw.text(
            str(number),
            (satillite.pos[0],satillite.pos[1]+ 20),color='purple'
        )
        satillite.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
        if next_satellite < number_of_satellite and total_time <= 15:
            total_time = time() - start_time
            screen.draw.text(
                str(round(total_time, 1)),
                (10,10),
                fontsize=30
            )
        elif total_time > 15:
            screen.draw.text("game over",(200,200),fontsize=100)
         
        else:
            screen.draw.text(str(round(total_time, 1)),(10,10),fontsize=30)
            screen.draw.text("You Won",(200,200),fontsize=100)



        
            
               



def update():
    pass
def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite < number_of_satellite and total_time <= 15:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((
            
                satellites[next_satellite - 1].pos,
                satellites[next_satellite].pos,
            ))

            next_satellite = next_satellite + 1
        else:
            lines = []
            next_satellite = 0
create_satellites()   
pgzrun.go()