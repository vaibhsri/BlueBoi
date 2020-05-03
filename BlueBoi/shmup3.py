import pygame
import random
import os
from settings import *
from sprites import *
from bonusshmup import newscore3
import time


#Set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "PyProj")



#Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
font_name=pygame.font.match_font('Sceptre')
def draw_text(surf,text,size, x, y):
    font = pygame.font.Font(font_name,size)
    text_surace=font.render(text, True, WHITE)
    text_rect=text_surace.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surace,text_rect)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.sound = pygame.mixer.Sound("laser.wav")
        # self.esound = pygame.mixer.Sound("explosion.wav")
        self.dsound=pygame.mixer.Sound("dead.wav")
        self.lsound=pygame.mixer.Sound("level.wav")
        self.score=0
        self.font_name=pygame.font.match_font(FONT_NAME)
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.transform.scale(img, (50,50))
        self.image = pygame.image.load(os.path.join(img_folder, "sanicsmall.png")).convert()
        self.image = pygame.transform.scale(self.image, (40,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 30
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    # def play_esound(self):
    #     self.esound.play()
    def play_dsound(self):
        self.dsound.play()
    def play_sound(self):
        self.sound.play()
    def play_lsound(self):
        self.lsound.play()

    def still(self):
        self.image = pygame.image.load(os.path.join(img_folder, "sanicsmall.png")).convert()
        self.image = pygame.transform.scale(self.image, (40,50))
        self.image.set_colorkey(BLACK)

    def update(self):
        self.speedx=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx= -5
        if keystate[pygame.K_RIGHT]:
            self.speedx=5
        self.rect.x+=self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if keystate[pygame.K_RIGHT]:
            self.image = pygame.image.load(os.path.join(img_folder, "p1_walk03.png")).convert()
            self.image = pygame.transform.scale(self.image, (40, 50))
            self.image.set_colorkey(BLACK)
        if keystate[pygame.K_LEFT]:
            self.image = pygame.image.load(os.path.join(img_folder, "p1_walk04.png")).convert()
            self.image = pygame.transform.scale(self.image, (40, 50))
            self.image.set_colorkey(BLACK)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def draw_text(self,text,size,color,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text, True, color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        screen.blit(text_surface,text_rect)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        self.score=0
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(meteor_images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 4)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x=random.randrange(WIDTH - self.rect.width)
        self.rect.y=random.randrange(-200,-40)
        self.speedy=random.randrange(1,8)
        self.speedx=random.randrange(-3,3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y +=self.speedy
        if self.rect.top>HEIGHT +10 or self.rect.left <=25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-200, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image = pygame.image.load(os.path.join(img_folder, "beam.png")).convert()
        self.image = pygame.transform.scale(self.image, (10, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        self.speedy = -5
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
meteor_images = []
meteor_list=['a1.png','a2.png','a3.png','a4.png','a5.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(os.path.join(img_folder, img)).convert())

background = pygame.image.load(os.path.join(img_folder, "spaceone.jpg")).convert()
background_rect=background.get_rect()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets=pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# score=1
# #hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
# hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
# if hits:
#     score=score+1
# if score<=100:

for i in range(1):
        m=Mob()
        all_sprites.add(m)
        mobs.add(m)
# elif score>200 and score<=500:
#     for i in range(4):
#         m=Mob()
#         all_sprites.add(m)
#         mobs.add(m)
# if score>500:
#     for i in range(8):
#         m=Mob()
#         all_sprites.add(m)
#         mobs.add(m)
#


score=newscore3
totalscore=100
# Game loop
running = True
start_ticks = pygame.time.get_ticks()
while running:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    # keep loop running at the right speed
    clock.tick(FPS)
    #Player.draw_text("Score :" + str(self.score), 22, RED, WIDTH / 2, HEIGHT / 4)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.play_sound()
                player.shoot()

        if event.type == pygame.KEYUP:
             player.still()


    # Update
    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs,bullets,True, True)
    for hit in hits:
        # player.play_dsound()
        #player.play_esound()
        score+=10
        for i in range(2):
            m=Mob()
            all_sprites.add(m)
            mobs.add(m)

    #check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        player.play_lsound()
        draw_text(screen, str("GAME OVER"), 50, WIDTH / 2, HEIGHT / 2)
        draw_text(screen, str("Score :") + str(score), 22, WIDTH / 2, HEIGHT / 4)
        #        draw_text(screen"High Score :" + str(self.highscore), 22, WHITE, WIDTH / 2, 40)
        draw_text(screen, str("You Made It!"), 70, WIDTH / 2, HEIGHT / 4 + 20)
        draw_text(screen, str("press the F to continue.."), 40, WIDTH / 2, HEIGHT - 60)
        # if score > highscore:
        #     highscore = score
        #     with open(path.join(self.dir, HS_FILE), 'w')as f:
        #         f.write(str(score))

        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_f]:
                    import menu
    # Draw / render
    screen.fill(GREEN)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str("Score :"), 18, WIDTH / 1.2, 10)
    draw_text(screen, str("Level Time :"), 18, WIDTH / 1.2, 25)
    draw_text(screen, str(score), 18, WIDTH / 1.1, 10)
    draw_text(screen, str(clock), 12, WIDTH / 8, 10)
    draw_text(screen,str(seconds),18,WIDTH/1.1,25)
    draw_text(screen,str("Score as much as you can!"),24,WIDTH/2,20)
    draw_text(screen,str("FINAL LEVEL!"),24,WIDTH/2,40)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()