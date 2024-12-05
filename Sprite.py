class Sprite:
    def __init__(self, name, x, y, width, height, xspeed, yspeed):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xspeed = xspeed
        self.yspeed = yspeed


    def move(self, x, y):
        self.x += x
        self.y += y


    def draw(self):
        print(self.name, "is at x:", self.x, "y:", self.y)


    def update(self, screen):
        self.move(self.xspeed, self.xspeed)
        if self.x < 0 or self.x + self.width > screen.width:
            self.xspeed = -self.xspeed
        if self.y < 0 or self.y + self.height > screen.height:
            self.yspeed = -self.yspeed
        self.draw()

