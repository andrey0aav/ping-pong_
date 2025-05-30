from pygame import *

back = (150, 159, 0)
win_width = 600
win_height = 600


window = display.set_mode((win_height, win_width))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3
font.init()


class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



racket1 = Player('img.png', 30, 200, 50, 100, 15)
racket2 = Player('img.png', 520, 200, 50, 100, 15)
ball = GameSprite('img.png', 200, 200, 30, 30, 50)

font = font.Font(None, 35)
lose1 = font.render('Победа правого ламината!', True, (100, 100, 255))
lose2 = font.render('Победа левого ламината!', True, (100, 100, 255))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1


        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1


        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True


        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
