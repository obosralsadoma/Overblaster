import pygame as p

p.init()
w, h = 800, 100
s = p.display.set_mode((w, h))
nm = "lox"
p.display.set_caption(nm)

clr1 = (222, 159, 91)

g = True
while g:
    for e in p.event.get:
        if e.type == p.QUIT:
            g = False
    
    s.fill(clr1)

p.quit()