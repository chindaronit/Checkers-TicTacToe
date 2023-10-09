import pygame 

WIDTH=800
HEIGHT=800

ROWS=8
COLS=8
SQSIZE=WIDTH//8
WHITE=(253,253,253)
BLACK=(0,0,0)
GREEN=(38, 166, 91)
CLOUD=(246,246,246)
DARKGREY=(116,116,116)
GRAY=(204,204,204)
GREY=(144,144,144)
ORANGE=(255, 172, 28)
RED=(230,0,0)
PURPLE=(112, 41, 99)

PADDING=22
OUTLINE=5

ownerNameButton=pygame.Rect(640, 720, 150, 30)
ownerRollNo=pygame.Rect(640 , 750, 150, 30)
playButton = pygame.Rect(300, 250, 200, 100)
exitButton = pygame.Rect(300, 400, 200, 100)
continueButton = pygame.Rect(300, 150, 200, 100)
resetButton = pygame.Rect(300, 300, 200, 100)
exitButtonPause = pygame.Rect(300, 450, 200, 100)
winnerPlate = pygame.Rect(0, 50, 800, 130)

easyButton = pygame.Rect(300, 150, 250, 100)
mediumButton = pygame.Rect(300, 300, 250, 100)
hardButton = pygame.Rect(300, 450, 250, 100)
extremeButton = pygame.Rect(300, 600, 250, 100)

BLACKPIECE=pygame.transform.scale(pygame.image.load("Black.png"),(120,120))
WHITEPIECE=pygame.transform.scale(pygame.image.load("White.png"),(120,120))
LIGHTWOOD=pygame.transform.scale(pygame.image.load("lightWood.png"),(100,100))
CROWN=pygame.transform.scale(pygame.image.load("crown.png"),(60,60))
