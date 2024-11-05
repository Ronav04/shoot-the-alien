import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
message = ""

alien = Actor("alien")
#alien.pos = 200,200

def draw():
    screen.fill("blue")
    place_alien()
    alien.draw()
    screen.draw.text(message,center = (400,10),fontsize = 30)
    
def place_alien():
    alien.x = randint(50,WIDTH - 50)
    alien.y = randint(50,HEIGHT - 50)  
     
def on_mouse_down(pos):
    global message 
    if alien.collidepoint(pos):
        message = "Good shot"
        place_alien()
        
    else:
        message = "You missed"
        
        
place_alien()       
        
pgzrun.go()      