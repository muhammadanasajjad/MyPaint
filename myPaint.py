import pygame
from tkinter import *

pygame.init()

White = 255, 255, 0

win = pygame.display.set_mode((500, 500))
win.fill((White))

window = Tk()

pygame.display.set_caption("Draw")

x = 50
y = 50
width = 40
height = 60
vel = 5

pygame.mouse.set_cursor(*pygame.cursors.broken_x)


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed:
            print("i am so happy this works")
            
    win.fill((White))
    pygame.display.update()
    #window.mainloop()

pygame.quit()
