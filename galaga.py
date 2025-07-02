import pgzrun
import random

WIDTH=1000
HEIGHT=600

ship=Actor("ship")
bug=Actor("bug")

ship.pos=(WIDTH/2,HEIGHT-100)
speed=1
bullets=[]
enemies=[]

for x in range(8):
    for y in range(4):
        enemies.append(Actor("bug"))
        enemies[-1].x=100+50*x
        enemies[-1].y=100+50*y

score=0
direction=1
ship.dead=False
ship.countdown=90

def displayScore():
    screen.draw.text(str(score), (50,30))
def gameOver():
    screen.draw.text("GAME OVER", (250,300))

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor('bullets'))
            #the last bullet added , set its position
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 50

def update():
    global score
    global direction
    moveDown = False
    #move the ship left or right with arrow keys
    if ship.dead == False:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0
        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH

        

def draw():
    screen.clear()
    screen.fill("black")
    
    for enemy in enemies:
        enemy.draw()

    if ship.dead==False:
        ship.draw()

    

pgzrun.go()
    