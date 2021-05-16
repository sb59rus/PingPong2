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
        self.speed_x = player_speed
        self.speed_y = int(player_speed/2)
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

class Ball(GameSprite):
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<1 or self.rect.y>549:
            self.speed_y*=-1
        if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
            self.speed_x*=-1
            pong.play()

#переменные
fon_music = 'fon.ogg'
pong_sound = 'pong.ogg'
ball = 'ball.png'
racket = 'racket.png'
finish = False
run = True
clock = time.Clock()
white = (150,150,150)

#Игровая сцена:
window = display.set_mode((1200, 600))
display.set_caption("PingPong")
window.fill(white)

#создание спрайтов
racket1 = Player1(racket, 40, 150, 10, 250, 5)
racket2 = Player2(racket, 40, 150, 1150, 250, 5)
ball = Ball(ball, 50, 50, 575, 275, 8)

#музыка
mixer.init()
mixer.music.load(fon_music)
mixer.music.play()
pong = mixer.Sound(pong_sound)

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
        ball.update()
        ball.reset()
    display.update()
    clock.tick(60)