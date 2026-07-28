import pgzrun

WIDTH = 800
HEIGHT = 600


s_x = 0
s_y = 0

def draw():
    screen.blit('spaceship.png',(s_x,s_y))
    screen.blit('astreroid.png',(10,10))

def update():
     global s_x
     s_x +=0.5

     if s_x > WIDTH + 40:
         s_x = -40

pgzrun.go()
     