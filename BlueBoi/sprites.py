import pygame
from settings import *
import os
from random import choice
import random
import pytmx
vec=pygame.math.Vector2
#assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "PyProj")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
class Spritesheet:
    def __init__(self,filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self,x,y,width,height):
        image=pygame.Surface((width,height))
        image.blit(self.spritesheet,(0,0),(x,y,width,height))
        image=pygame.transform.scale(image, (width/2,height/2))
        return image


# class TiledMap:
#     def __init__(self,filename):
#         tm=pytmx.load_pygame(filename, pixelalpha=True)
#         self.width=tm.width*tm.tilewidth
#         self.height=tm.height*tm.tileheight
#         self.tmxdata=tm
#
#     def render(self,surface):
#         ti=self.tmxdata.get_tile_image_by_grid
#         for layer in self.tmxdata.visible_layers:
#             if isinstance(layer,pytmx.TiledTileLayer):
#                 for x,y,gid, in layer:
#                     tile=ti(gid)
#                     if tile:
#                         surface.blit(tile, (x*self.tmxdata.tilewidth, y*self.tmxdata.tileheight))
#     def make_map(self):
#         temp_surface=pygame.Surface((self.width, self. height))
#         self.render(temp_surface)
#         return temp_surface

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        self.dsound=pygame.mixer.Sound("dead.wav")
        self.lsound = pygame.mixer.Sound("level.wav")
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        #self.image=pygame.image.load(os.path.join(img_folder, "sanicsmall.png")).convert()
        playerimg=[self.game.spritesheetplayer.get_image(67 ,196 ,66 ,92),self.game.spritesheetplayer.get_image(0 ,0 ,72 ,97)]
        self.image=playerimg[0]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.center=(WIDTH-(WIDTH-50),HEIGHT-50)
        self.pos=vec(WIDTH-(WIDTH-50),HEIGHT-50)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def play_dsound(self):
        self.dsound.play()

    def play_lsound(self):
        self.lsound.play()

    def jump(self):
        playerimg = [self.game.spritesheetplayer.get_image(438, 93, 67, 94)]
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.game.jump_sound.play()
            self.vel.y = -15
        self.image = playerimg[0]
        self.image.set_colorkey(BLACK)
    def still(self):
        playerimg=[self.game.spritesheetplayer.get_image(67 ,196 ,66 ,92),self.game.spritesheetplayer.get_image(0 ,0 ,72 ,97)]
        self.image=playerimg[0]
        self.image.set_colorkey(BLACK)

    def update(self):
        playerimg=[self.game.spritesheetplayer.get_image(67 ,196 ,66 ,92),self.game.spritesheetplayer.get_image(0 ,0 ,72 ,97)]
        self.acc=vec(0,0.5)

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x=-PLAYER_ACC
            self.image = pygame.image.load(os.path.join(img_folder, "p1_walk05.png")).convert()
            self.image = pygame.transform.scale(self.image, (40, 50))
            self.image.set_colorkey(WHITE)
        if keys[pygame.K_RIGHT]:
            self.acc.x=PLAYER_ACC
            self.image=playerimg[1]
            self.image.set_colorkey(BLACK)

        #apply friction
        self.acc.x+=self.vel.x*PLAYER_FRICTION
        self.vel+=self.acc
        self.pos+=self.vel+0.5*self.acc
        #restrict backwards movement
        if self.pos.x<(WIDTH+40)-WIDTH:
            self.pos.x=(WIDTH+40)-WIDTH


        self.rect.midbottom=self.pos

class Platform(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        images=[self.game.spritesheet.get_image(576,864,70,70)]
        self.image=choice(images)
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class DoorTop(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        images=[self.game.spritesheet.get_image(648,360,70,70)]
        self.image=choice(images)
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Door(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        images=[self.game.spritesheet.get_image(648,432,70,70)]
        self.image=choice(images)
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y



