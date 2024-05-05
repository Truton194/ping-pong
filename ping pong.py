from pygame import *

WIN_WIDTH = 700
WIN_HEIGHT = 500
FPS = 40

BG = (51, 28, 115)

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption('PingPong')

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_sprite, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       self.image = transform.scale( image.load(player_sprite), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        mouse_keys = mouse.get_pressed()
        if keys[ K_w ] and self.rect.y >= 5:
            self.rect.y -= self.speed
        elif keys[ K_s ] and self.rect.y <= WIN_HEIGHT - 155:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        mouse_keys = mouse.get_pressed()
        if keys[ K_UP ] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[ K_DOWN ] and self.rect.y <= WIN_HEIGHT - 155:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_sprite, player_x, player_y, size_x, size_y, speed_x, speed_y):
        super().__init__(player_sprite, player_x, player_y, size_x, size_y, speed_x)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y >= WIN_HEIGHT:
            self.speed_y *= -1

        if self.rect.y <= 0:
            self.speed_y *= -1

    def collide_rect(self, player):
        if self.rect.colliderect(player):
            self.speed_x *= -1

player_1 = Player('racket.png', 50, WIN_HEIGHT -280, 50, 150, 4)
player_2 = Player('racket.png', WIN_WIDTH -100, WIN_HEIGHT - 280, 50, 150, 4)
ball = Ball('tenis_ball.png', 275, WIN_HEIGHT - 280, 50, 50, 4, 4)


game = True
finish = False

font.init()
font_win = font.SysFont('Arial', 70)
win_r = font_win.render('выйграл правый игрок', True, (255, 255, 255))
win_l = font_win.render('выйграл левый игрок', True, (255, 255, 255))
winner = None

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(BG)

        player_1.reset()
        player_1.update_r()
        player_2.reset()
        player_2.update_l()
        ball.reset()
        ball.update()
        ball.collide_rect(player_1)
        ball.collide_rect(player_2)

        if ball.rect.x < 50:
            winner = win_r
            finish = True
        if ball.rect.x > WIN_WIDTH - 50:
            winner = win_l
            finish = True
    elif finish:
        window.blit(winner, (50, 200))
    display.update()
    clock.tick(FPS)