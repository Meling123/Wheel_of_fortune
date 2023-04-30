# press 'a'  to spin the wheel

import pygame as pg
import random as rd
import time
import math


def flip():
    pg.display.flip()



with open('titles.txt') as f:
    lista_seriali = f.readlines()


pg.init()

width, height = 700, 700

screen = pg.display.set_mode([width, height])

font = pg.font.SysFont('arial', 15)

podział = math.radians(360)/len(lista_seriali)


j = podział
radians = []
for e in range(len(lista_seriali)):
    radians.append(j)
    j += podział

run = True

center_distance = [width / 2, height / 2]
radius = 300
lines = []

i = 0
spim = False
cord = []

for e in range(len(lista_seriali)):
    cord.append([lista_seriali[e], radians[e]])


while run:

    cir = pg.draw.circle(screen, [255, 0, 0], center_distance, radius)
    pg.draw.line(screen, [0,0,0], (width/2, height/2 - radius), (width/2, height/2 - radius + 100))

    for x in  radians:
        line = pg.draw.line(screen, [0, 0,0], center_distance, (radius * math.sin(x+i) + 350, radius * math.cos(x+i) + 350))
        lines.append(line)


    for z in  cord:
        text = font.render(str(z[0]), True, (0, 0, 0), (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (radius/2 * math.sin(z[1] + i - radians[0]/2) + 350,radius/2 * math.cos(z[1] + i - radians[0]/2) + 350)
        screen.blit(text, textRect)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()


    if pg.key.get_pressed()[pg.K_a]:
        global past_time
        spim = not (spim)
        past_time = time.time()

    if spim:
        i += 0.005
        if time.time() - past_time >= rd.randrange(3, 10):
            spim = not (spim)


    pg.display.update()

