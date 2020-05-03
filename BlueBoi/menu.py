import pygame
import random
import os
from os import path
import settings1
from settings1 import *
from sprites1 import *

class Game:
    def __init__(self):
        #initialize game window
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Blue Boy!")
        self.clock = pygame.time.Clock()
        self.running=True
        self.font_name=pygame.font.match_font(FONT_NAME)
        self.load_data()
    def load_data(self):
        self.dir=path.dirname(__file__)
        img_dir=path.join(self.dir,'Player')
        with open(path.join(self.dir, HS_FILE),'w')as f:
            try:
                self.highscore=int(f.read())
            except:
                self.highscore=0
        self.spritesheet=Spritesheet(path.join(img_dir,SPRITESHEETTILES))
        self.spritesheetplayer=Spritesheet(path.join(img_dir,SPRITESHEETPLAYER))
        #load sounds
        self.snd_dir=path.join(self.dir,'snd')
        self.jump_sound=pygame.mixer.Sound(path.join(self.snd_dir, 'jump.wav'))
        #pass=do nothing
    def new(self):
        #start a new game
        self.score=0
        self.all_sprites = pygame.sprite.Group()
        self.door=pygame.sprite.Group()
        self.doortop=pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.platforms=pygame.sprite.Group()
        self.player=Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST1:
            p=Platform(self,*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.door=pygame.sprite.Group()
        for door in DOORS:
            d=Door(self,*door)
            #self.all_sprites.add(d)
            self.door.add(d)
        for doortop in DOORTOP:
            dt=DoorTop(self,*doortop)
            #self.all_sprites.add(d)
            self.doortop.add(dt)


        self.run()
    def run(self):
        #game loop
        self.clock.tick(FPS)
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        #game loop update
        self.all_sprites.update()
        if self.player.vel.y>0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top+1  # +1 for over the platform
                self.player.vel.y = 0
        #scrolling
            # if self.player.pos.y <=HEIGHT/2:
            #     self.player.pos.y +=max(abs(self.player.vel.y),2)
            #     for plat in self.platforms:
            #         if self.player.vel.y>0:
            #             plat.rect.y+=max(abs(self.player.vel.y),2)
        #     if self.player.pos.x >=WIDTH/2 :
        #         self.player.pos.x -= max(abs(self.player.vel.x),2)
        #         for plat in self.platforms:
        #             if self.player.vel.x > 0:
        #                 plat.rect.x -= max(abs(self.player.vel.x),2)
        # if self.player.rect.bottom>HEIGHT:
        #     self.playing = False
    def events(self):
        #game loop events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing=False
                self.running = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    self.player.jump()

            if event.type==pygame.KEYUP:
                self.player.still()
        #game loop events
        if self.player.pos.x >= WIDTH / 2 and self.player.pos.x <= WIDTH / 2 + 70:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                import shmup
        if self.player.pos.x >= WIDTH / 1.3 and self.player.pos.x <= WIDTH / 1.3 + 70:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                import game
    def draw(self):
        #game loop draw
        #background = pygame.image.load(os.path.join(img_folder, "space.jpeg")).convert()
        #background_rect = background.get_rect()
        background = pygame.image.load(os.path.join(img_folder, "spaceone.jpg")).convert()
        background_rect = background.get_rect()
        self.screen.fill(GREEN)
        self.screen.blit(background, background_rect)
        self.all_sprites.draw(self.screen)
        #self.screen.blit(background, background_rect)
        self.door.draw(self.screen)
        self.doortop.draw(self.screen)
        self.all_sprites.draw(self.screen)
        # self.draw_text(str(self.score),22,WHITE,WIDTH/2,15)
        if self.player.pos.x>=WIDTH/2 and self.player.pos.x<=WIDTH/2+70:
            self.draw_text("Destroy as many asteroids as possible and set your own legendary record!"
                           , 20, WHITE, WIDTH / 2, HEIGHT / 4)
            self.draw_text("SHOOT EM' UP!", 50, RED, WIDTH / 2, HEIGHT / 2)
            self.draw_text("Press F", 30, BLUE, WIDTH / 2, HEIGHT / 3)
        if self.player.pos.x<WIDTH/2:
            self.draw_text("WELCOME TO THE LIFE OF BLUE BOI!", 40, BLUE, WIDTH / 2, HEIGHT / 2)
        if self.player.pos.x>=WIDTH/1.3 and self.player.pos.x<=WIDTH/1.3+70:
            self.draw_text("Make your way through the asteroid showers to the finish line!",
                           20, WHITE, WIDTH / 2, HEIGHT / 4)
            self.draw_text("DODGE!", 50, RED, WIDTH / 2, HEIGHT / 2)
            self.draw_text("Press F", 30, BLUE, WIDTH / 2, HEIGHT / 3)
        pygame.display.flip()
    def show_start_screen(self):
        self.screen.fill(WHITE)
        self.draw_text("Blue Boy", 50, BLUE, WIDTH/2,HEIGHT/2)
        self.draw_text("press any key to start game...",22,RED,WIDTH/2,HEIGHT/4)
        self.draw_text("made by Lasya Priya Kanchi and  Vaibhav Srivastava",18,BLACK,WIDTH/2,HEIGHT-20)
        pygame.display.flip()
        self.wait()
    def show_gameover_screen(self):
        if not self.running:
            return
        self.screen.fill(WHITE)
        self.draw_text("GAME OVER", 50, BLACK, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Score :"+ str(self.score), 22, RED, WIDTH / 2, HEIGHT / 4)
        self.draw_text("High Score"+str(self.highscore),22, WHITE, WIDTH/2,15)
        self.draw_text("You Tried!",70, RED, WIDTH/2, HEIGHT/4+20)
        self.draw_text("press any key to continue..",40,BLACK, WIDTH/2,HEIGHT-60)
        if self.score>self.highscore:
            self.highscore=self.score
            with open(path.join(self.dir,HS_FILE),'w')as f:
                f.write(str(self.score))

        pygame.display.flip()
        self.wait()
    def wait(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    waiting=False
                    self.running=False
                if event.type==pygame.KEYUP:
                    waiting=False
    def draw_text(self,text,size,color,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text, True, color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface,text_rect)
g=Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameover_screen()
pygame.quit()
