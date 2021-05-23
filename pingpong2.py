from pygame import *
from random import randint
from time import time as timer

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.speed_x = player_speed
        self.speed_y = int(player_speed/2)
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
        if key_pressed[K_s] and self.rect.y<win_h-int(win_h/4):
            self.rect.y+=self.speed 

class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_DOWN] and self.rect.y<win_h-int(win_h/4):
            self.rect.y+=self.speed 

class Ball(GameSprite):
    def update(self):
        global score1
        global score2
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<1 or self.rect.y>win_h-51:
            self.speed_y*=-1
        if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
            self.speed_x*=-1
            pong.play()
        if self.rect.x<1:
            score2+=1
            self.rect.x = int(win_w/2)
            self.rect.y = int(win_h/2)
        if self.rect.x>win_w-1:
            score1+=1
            self.rect.x = int(win_w/2)
            self.rect.y = int(win_h/2)
#переменные
win_w = int(1440/2)
win_h = int(720/2)
fon_music = 'fon.ogg'
pong_sound = 'pong.ogg'
ball = 'ball.png'
racket = 'racket.png'
finish = False
run = True
clock = time.Clock()
white = (150,150,150)
score1 = 0
score2 = 0

#Игровая сцена:
window = display.set_mode((win_w, win_h))
display.set_caption("PingPong")
window.fill(white)

#создание спрайтов
racket1 = Player1(racket, 40, int(win_h/4), 10, 250, 5)
racket2 = Player2(racket, 40, int(win_h/4), win_w-50, 250, 5)
ball = Ball(ball, int(win_h/10), int(win_h/10), win_h-15, 275, 8)

#музыка
mixer.init()
mixer.music.load(fon_music)
mixer.music.play()
pong = mixer.Sound(pong_sound)

#шрифты
font.init()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(white)
    if not(finish):
        racket1.update()
        racket2.update()
        ball.update()

        text_score1 = font.SysFont('Arial', 70).render(str(score1), 1, (255,255,255))
        text_score2 = font.SysFont('Arial', 70).render(str(score2), 1, (255,255,255))
        if score1 == 10:
            text_score1 = font.SysFont('Arial', 70).render('W', 1, (0,255,0))
            text_score2 = font.SysFont('Arial', 70).render('L', 1, (255,0,0))
            finish = True
        if score2 == 10:
            text_score1 = font.SysFont('Arial', 70).render('L', 1, (255,0,0))
            text_score2 = font.SysFont('Arial', 70).render('W', 1, (0,255,0))
            finish = True
    window.blit(text_score1, (100, win_h/2-30))
    window.blit(text_score2, (win_w-100, win_h/2-30))
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(60)