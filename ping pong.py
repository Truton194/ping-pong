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
        if keys[ K_u ] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[ K_d ] and self.rect.x < WIN_WIDTH - 695:
            self.rect.x += self.speed

    def update_l(self):
        keys = key.get_pressed()
        mouse_keys = mouse.get_pressed()
        if keys[ K_w ] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[ K_s ] and self.rect.x < WIN_WIDTH - 695:
            self.rect.x += self.speed

player_1 = Player
player_2 = Player

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(BG)

    display.update()
    clock.tick(FPS)deactivate