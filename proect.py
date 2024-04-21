import pygame
import random
pygame.init()


FPS = 60
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (200, 0, 0)
YELLOW = (200, 200, 0)
GREEN = (34, 177, 76)



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YRA I NAPISAT IGRU")

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5


def update(self, keys):
    if keys[pygame.K_LEFT]:
        self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]:
        self.rect.x += self.speed
    if keys[pygame.K_UP]:
        self.rect.y -= self.speed
    if keys[pygame.K_DOWN]:
        self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed = 3


def update(self):
    self.rect.x += self.speed
    if self.rect.right > WIDTH:
        self.speed = -self.speed
    if self.rect.left < 0:
        self.speed = -self.speed


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10


def update(self):
    self.rect.y -= self.speed
    if self.rect.bottom < 0:
        self.kill()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


def create_enemies(num_enemies):
    for i in range(num_enemies):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        create_enemies(10)




running = True
while running:
    clock.tick(FPS)
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    keys = pygame.key.get_pressed()
    player.update(keys)
    enemies.update()
    bullets.update()

    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
for hit in hits:
    create_enemies(1)

screen.fill((0, 0, 255))
all_sprites.draw(screen)
pygame.display.flip()

pygame.quit()


