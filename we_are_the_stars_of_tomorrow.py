# I have imported a library called pgzrun it is for 
import pgzrun

# to set the size of the screen
WIDTH = 800
HEIGHT = 600

# I have defined two variables spaceship and asteroid to call the two images using 
# Actor class (because it has got lots of other function draw,left,right,up,down,pos,x,y etc)

spaceship = Actor("spaceship1")
astreroid = Actor("astreroid")


# anything we put under draw function using draw method for asteroid and spaceship
def draw():
    screen.fill((128, 0, 0))
    spaceship.draw()
    astreroid.draw()


# to move things we put them under update function
def update():

    spaceship.right = spaceship.right + 1

    if spaceship.right > WIDTH: 
        spaceship.left = 0

    # Move up and down
    if keyboard.up:
        astreroid.y = astreroid.y - 5
    if keyboard.down:
        astreroid.y = astreroid.x + 5



pgzrun.go()

# https://pygame-zero.readthedocs.io/en/stable/introduction.html