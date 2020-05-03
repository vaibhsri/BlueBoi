WIDTH = 1280/2
HEIGHT = 720/2
FPS = 60
FONT_NAME = 'Sceptre'

HS_FILE="highscore.txt"
SPRITESHEETTILES="tiles_spritesheet.png"
SPRITESHEETPLAYER="p1_spritesheet.png"
#Player Attributes
PLAYER_ACC=0.7
PLAYER_FRICTION=-0.12
#(X,Y,W,H)
PLATFORM_LIST=[(0,HEIGHT - 10),
               (35*10, HEIGHT - 150),
               (35 * 34 , HEIGHT - 150),(35*51, HEIGHT - 150),(35*60, HEIGHT - 150),
               (35*60+60, HEIGHT - 150),(35*73,HEIGHT-150),(35*89, HEIGHT-150),]
for i in range(1,9):
    PLATFORM_LIST.append((35*i,HEIGHT-10))
for i in range(11,24):
    PLATFORM_LIST.append((35*i,HEIGHT-10))
for i in range(27,33):
    PLATFORM_LIST.append((35*i,HEIGHT-10))
for i in range(35,50):
    PLATFORM_LIST.append((35*i,HEIGHT-10))
for i in range(55,60):
    PLATFORM_LIST.append((35*i,HEIGHT-10))
for i in range(66,72):
    PLATFORM_LIST.append((35*i,HEIGHT-10))
for i in range(75,88):
    PLATFORM_LIST.append((35*i,HEIGHT-10))

for i in range(90,100):
    PLATFORM_LIST.append((35*i,HEIGHT-10))

for i in range(103,110):
    PLATFORM_LIST.append((35*i,HEIGHT-10))
DOOR=[(35*105, HEIGHT - 45)]
DOORTOPS=[(35*105, HEIGHT - 45-30)]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0  )
TEAL = (125, 125, 0)
