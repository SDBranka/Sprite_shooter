import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("thompson-1.wav")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        # makes object follow mouse
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)


# general set up
pygame.init()
clock = pygame.time.Clock()

# screen set up
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
# change the title of the displayed in display window
pygame.display.set_caption("Spritesheet Shooter")
# create background image
background = pygame.image.load("bg_blue.png")
# scale background imgage to match display screen size
background = pygame.transform.scale(background, (screen_width, screen_height))

# make mouse cursor invisible
pygame.mouse.set_visible(False)

# create crosshair object
crosshair = Crosshair("crosshair_outline_small.png")
# create group of objects so that each doesn't need to be drawn individually
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# create target group
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("duck_target_white.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    # draw targets before the crosshair so that crosshair shows on top of targets
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)








