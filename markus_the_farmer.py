import pgzrun
import random

WIDTH = 700
HEIGHT = 700

markus = Actor("farmer")
markus.pos = 200,600
potato = Actor('potatoes')
potato.pos = 600,600
score = 0

def draw():
    screen.blit("farm",(0,0))
    markus.draw()
    potato.draw()
    screen.draw.text("score: " + str(score), color="black", topleft=(10,10))
    

def place_potato():
    potato.x = random.randint(100, 650)
    potato.y = random.randint(100, 700)

def update():
     global score
     if keyboard.left:
          markus.x = markus.x - 2
     if keyboard.right:
          markus.x = markus.x + 2
     if keyboard.up:
          markus.y = markus.y -2
     if keyboard.down:
          markus.y = markus.y + 2
     potato_collected = markus.colliderect(potato)
     if potato_collected:
          score = score + 10
          place_potato()
    
# we will add a wolf so if farmer collides with the wolf you lose
# add timer in the game


pgzrun.go()