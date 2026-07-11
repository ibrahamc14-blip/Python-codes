import pgzrun

WIDTH = 800
HEIGHT = 800


def draw():
    screen.fill('Royal Blue')

    screen.draw.filled_circle((400,800),350,'red')
    screen.draw.filled_circle((400,800),300,'orange')
    screen.draw.filled_circle((400,800),250,'yellow')
    screen.draw.filled_circle((400,800),200,'green')
    screen.draw.filled_circle((400,800),150,'blue')
    screen.draw.filled_circle((400,800),100,'indigo')
    screen.draw.filled_circle((400,800),50,'violet')

pgzrun.go()