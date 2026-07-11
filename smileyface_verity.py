import pgzrun
WIDTH = 800
HEIGHT = 600


x = 200
y = 200

x2=300
y2=200


def draw():
    screen.fill('yellow')

    screen.draw.filled_circle((300,200),150,'royal blue')

    stick = Rect((x,y),(6,10))
    stick2 = Rect((x2,y2),(6,10))
    
    screen.draw.filled_rect(stick,'black')
    screen.draw.filled_rect(stick2,'black')

    screen.draw.circle((400,350),100,'yellow')


pgzrun.go()