print("Initialization Python Code...")
import pygame as p

p.init()
print("Initialization library Pygame 2.6.1...")
print("Launching Pygame Window...")

try:
    w, h = 800, 1000 
    s = p.display.set_mode((w, h))
    nm = "lox"
    p.display.set_caption(nm)


    bg1 = (222, 159, 91)
    bg2 = (23, 153, 0)

    laro = p.image.load("images/person_laro_alpha-prototype")

    class Pole:
        def __init__(self, w, h, x, y):
            self.w = w
            self.h = h
            self.x = x
            self.y = y
            self.rect = p.Rect(self.x, self.y, self.w, self.h)
            self.color = (255, 221, 179)
        def draw(self, s):
            p.draw.rect(s, self.color, self.rect)

    # class Laro:
    #     def __init__(self, image):
    #         self.image = image
    #         self.x = 100
    #         self.y = 400
    #         self.speed = 20
    #     def draw(self, s):
    #         s.blit(self.image, self.x, self.y)
    #     def move(self):
    #         if e.type == p.KEYDOWN:
    #             if e.key == p.K_w or p.K_UP:


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
except BaseException as error:
    print(f"Operation has been falled by error: {error}")
finally:
    print("Operation has been successfully")