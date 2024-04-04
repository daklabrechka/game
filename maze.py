#создай игру "Лабиринт"!
from time import *
from pygame import *

win_width = 700
win_hight = 500

window = display.set_mode((win_width,win_hight))
display.set_caption("Лабиринт")

backgraund = transform.scale(image.load("background.jpg"),(win_width,win_hight))

fps = time.Clock()

class GameSpite(sprite.Sprite):
    def __init__(self, image_sprite, img_x, img_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_sprite),(65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = img_x
        self.rect.y = img_y
    def show_s(self):
            window.blit(self.image,(self.rect.x, self.rect.y))


class Hero(GameSpite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Vrag(GameSpite):
    naprav = "left"
    def update(self):
        if self.rect.x <= 470:
            self.naprav = 'right'
        if self.rect.x >= win_width - 85:
            self.naprav = 'left'
        
        if self.naprav == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__ (self, color1, color2, color3, wall_x, wall_y, wall_width, wall_hight):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

        self.wall_width = wall_width
        self.wall_hight = wall_hight

        self.image = Surface ((self.wall_width, self.wall_hight))
        self.image.fill((self.color1, self.color2, self.color3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def show_s(self):
        window.blit(self.image, (self.rect.x, self.rect.y))






player = Hero("hero.png",5, win_hight-70, 4)
enemy = Vrag('cyborg.png',200, 400, 4)
gold = GameSpite('treasure.png', 410, win_hight-100, 0)
w1 = Wall(132,0,55,  90,90,  10,420)
w2 = Wall(132,0,55,  100,90,  100,10)
w3 = Wall(132,0,55,  200,90,  10,500)
w4 = Wall(132,0,55,  300,0,  10,400)
w5 = Wall(132,0,55,  400,100,  10,600)
w6 = Wall(132,0,55, 400,90,  150, 10)

image_vin = image.load('treasure.png')
image_vin = transform.scale(image_vin, (win_width, win_hight))

image_lose= image.load('pobeda.png')
image_lose = transform.scale(image_lose, (win_width, win_hight))


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')


run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    window.blit(backgraund,(0,0))

        
       
        

    player.show_s()
    player.update()
    enemy.show_s()
    enemy.update()
    w1.show_s()
    w2.show_s()
    w3.show_s()
    w4.show_s()
    w5.show_s()
    w6.show_s()
    gold.show_s()
    gold.update()

    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w1) :
        window.blit(image_vin, (0,0))
        kick.play()
    if sprite.collide_rect(player, gold)  :
        window.blit(image_lose, (0,0))
        money.play() 
    display.update()
    fps.tick(60)
