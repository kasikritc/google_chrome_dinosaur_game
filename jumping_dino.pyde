from Dino import *
from Obstacle import *

GRAVITY = -1.1

def isCollide(dino, obstacle):
    if dist(dino.x, dino.y, obstacle.x, obstacle.y) < 40:
        return True
    return False
    
def setup():
    global dino, cacti, cactus_img, isGameOver, loop_count, score, new_donut_timing
    
    size(1000, 700)
    background(255)
    
    dino = Dino(img=loadImage('dino.png'),
                x=width/10, y=height/2,
                 w=75, h=75)
    
    cactus_img = loadImage('cactus.png')
    cacti = []
    isGameOver = False
    loop_count = 0
    score = 0
    new_donut_timing = 0

def draw():
    global dino, cacti, cactus_img, isGameOver, loop_count, score, new_donut_timing
    
    background(255)
    # draw ground
    fill(100)
    stroke(100)
    rect(10, height/2+35, width-20, 2)
    
    textSize(20)
    text("Score:", 25, 50)
    text(str(score), 100, 50)
    
    if isGameOver:
        textSize(48)
        text("Game Over", width/2-115, height/2-150)
        textSize(28)
        text("Press 'R' to play again", width/2-135, height/2-100)
        dino.show()
        for cactus in cacti:
            cactus.show()
    else:
        new_donut_timing = int(random(25, 80))
        if loop_count % new_donut_timing == 0:
            loop_count = 0
            cacti.append(Obstacle(img=cactus_img, 
                                  x=width, y=height/2, 
                                  w=75, h=75, 
                                  speedX=-6))
        dino.show()
        dino.update_loc()
        for cactus in cacti:
            if cactus.x < 10:
                cacti.remove(cactus)
                continue
            else:
                cactus.show()
                cactus.update_loc()
            if isCollide(dino, cactus):
                isGameOver = True
                break
        loop_count += 1
        if loop_count % 3 == 0:
            score += 1
            
def keyPressed():
    global dino, cacti, isGameOver, score
    
    # check if SPACEBAR or 'W' or UP_ARROW is pressed to jump
    if (keyCode == 32 or keyCode == 87 or keyCode == UP) and not dino.isJumping:
        dino.isJumping = True
        dino.speedY = -(dino.JUMP_POWER)
        
    # check if 'R' is pressed to reset
    if keyCode == 82 and isGameOver:
        cacti = []
        isGameOver = False
        score = 0
        
        
