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
PLATFORM_LIST1=[(0,HEIGHT - 10)
                ]
for i in range(1,50):
    PLATFORM_LIST1.append((35*i,HEIGHT-10))

DOORS=[(WIDTH/2, HEIGHT - 45),(WIDTH/1.3, HEIGHT - 45)]
DOORTOP=[(WIDTH/2, HEIGHT - 45-30),(WIDTH/1.3, HEIGHT - 45-30)]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0  )


