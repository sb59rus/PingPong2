from pygame import *
from random import randint
from time import time as timer

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_s] and self.rect.y<450:
            self.rect.y+=self.speed 

class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_DOWN] and self.rect.y<450:
            self.rect.y+=self.speed 

#переменные
ball = 'ball.png'
racket = 'racket.png'
finish = False
run = True
clock = time.Clock()
white = (255,255,255)

#Игровая сцена:
window = display.set_mode((1200, 600))
display.set_caption("PingPong")
window.fill(white)

#создание спрайтов
racket1 = Player1(racket, 40, 150, 10, 250, 5)
racket2 = Player2(racket, 40, 150, 1150, 250, 5)

#музыка
'''mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
shot = mixer.Sound('fire.ogg')'''

#шрифты
'''font.init()
win = font.SysFont('Arial', 70).render('YOU WIN', 1, (0,255,0))
lose = font.SysFont('Arial', 70).render('GAME OVER', 1, (255,0,0))'''

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not(finish):
        window.fill(white)
        racket1.update()
        racket2.update()
        racket1.reset()
        racket2.reset()
    display.update()
    clock.tick(60)