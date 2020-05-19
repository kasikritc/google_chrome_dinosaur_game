GRAVITY = -1.1

class Dino:
    def __init__(self, img, x, y, w, h):
        self.img = img
        self.x = x
        self.y = y
        self.W = w
        self.H = h
        self.speedY = 0
        self.JUMP_POWER = 18
        self.isJumping = False
        
    def update_loc(self):
        if self.isJumping:
            self.y += self.speedY
            self.speedY -= GRAVITY
        if self.y > height/2:
            self.y = height/2
            self.speedY = 0
            self.isJumping = False
        
    def show(self):
        imageMode(CENTER)
        image(self.img, self.x, self.y, self.W, self.H)
