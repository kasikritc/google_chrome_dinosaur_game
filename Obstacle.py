class Obstacle:
    def __init__(self, img, x, y, w, h, speedX):
        self.img = img
        self.x = x
        self.y = y
        self.W = w
        self.H = h
        self.speedX = speedX
    
    def update_loc(self):
        self.x += self.speedX
        
    def show(self):
        imageMode(CENTER)
        image(self.img, self.x, self.y, self.W, self.H)
