import pygame
from constants import SQSIZE,OUTLINE,PADDING,WHITE,BLACKPIECE,BLACK,WHITEPIECE,CROWN


class Piece:
  
    def __init__(self,row,col,color):
        self.row=row    
        self.col=col
        self.color=color
        self.king=False
        self.x=0
        self.y=0
        self.calc_pos()
        

        if self.color==WHITE:
            self.direction=-1
        else :
            self.direction=1

    
    def calc_pos(self):
        self.x=SQSIZE*self.col+SQSIZE//2
        self.y=SQSIZE*self.row+SQSIZE//2        
    
    def make_king(self):
        self.king=True
    
    def draw(self,window):
        RADIUS=SQSIZE//2-PADDING
        pygame.draw.circle(window,WHITE,(self.x,self.y),RADIUS)
        if self.color==WHITE:
            window.blit(WHITEPIECE,(self.x-60,self.y-60))
        elif self.color==BLACK:
            window.blit(BLACKPIECE,(self.x-60,self.y-60))
        if self.king:
            window.blit(CROWN,(self.x-32,self.y-32))

    def move(self,row,col):
        self.row=row
        self.col=col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

    