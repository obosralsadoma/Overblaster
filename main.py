import pygame as p

p.init()
w, h = 800, 1000 
s = p.display.set_mode((w, h))
nm = "lox"
p.display.set_caption(nm)

bg1 = (222, 159, 91)
bg2 = (10, 124, 255)


class Pole:
    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.rect = p.Rect(self.x, self.y, self.w, self.h)
        self.color = (25, 166, 0)
    def draw(self, s):
        p.draw.rect(s, self.color, self.rect)

grass = Pole(200, h, 0, 0)
g = True
while g:
    for e in p.event.get():
        if e.type == p.QUIT:
            g = False
    
    s.fill(bg2)
    grass.draw(s)
    p.display.flip()

p.quit()