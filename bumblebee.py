import pgzrun
import random
TITLE="bumblebee game"
WIDTH=600
HEIGHT=700
score=0           
gameOver=False      
bee=Actor("bee")
bee.pos=(100,100)
flower=Actor("flower")
flower.pos=(500,500)                       
def draw():
    screen.blit("background", (0,0))    #to add an image straight on to the screen as a background image, to use colour/solid colour you use screen.fill(insertedColor)
    flower.draw()
    bee.draw()
    screen.draw.text("Score="+str(score), "black", topleft=(50,50))  #combining multiple strings together

def place():
    flower.x=random.randint(70,(WIDTH-70))
    flower.y=random.randint(100,(HEIGHT-100))

def timeUp():
    global gameOver         #if its not global, the value can not be access outside the function
    gameOver=True