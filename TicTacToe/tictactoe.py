# %% [markdown]
# Importing pygame and other useful packages and initializing pygame

# %%
import copy
import random
import numpy as np
import pygame
pygame.init()

# %% [markdown]
# Setting window dimesions and rectangle Dimensions

# %%
windowWidth = 900
windowHeight = 500
width = 100
height = 100

# %% [markdown]
# Making window and adding caption to it

# %%
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("TicTacToe")

# %% [markdown]
# Setting values for some useful variables

# %%
ROWS = 3
COLS = 3
RADIUS = 28
LINEWIDTH = 12
CIRWIDTH = 10

# %% [markdown]
# Creating array of size 3x3

# %%
squares = np.zeros((ROWS, COLS))
print(squares)

# %% [markdown]
# Define color for circles , rectangles and lines

# %%
RECTCOLOR = (152, 251, 152)
CIRCOLOR = (0, 0, 0)
LineColor= (250,0,0)

# %% [markdown]
# Define colors for toggle button

# %%
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# %% [markdown]
# Define font for text

# %%
font = pygame.font.Font(None, 30)

# %% [markdown]
# Define Toggle button states , button rect,Define pointer rect

# %%
button_states = ["left", "right"]
button_rect = pygame.Rect(600, 350, 100, 30)
pointer_rect = pygame.Rect(button_rect.x, button_rect.y, button_rect.width/2, button_rect.height)

# %% [markdown]
# Colors for reset button and making resetButton rectangle

# %%
resetButton = pygame.Rect(600, 200, 100, 50) #button rectangle
DEFAULT_COLOR = (100, 100, 100)
HOVER_COLOR = (150, 150, 150)
CLICKED_COLOR = (173, 216, 230)

# %% [markdown]
# Function to draw Reset Button

# %%
def draw_button(window, state):
    if state == "default":
        color = DEFAULT_COLOR
    elif state == "hover":
        color = HOVER_COLOR
    elif state == "clicked":
        color = CLICKED_COLOR

    # draw the button rectangle
    pygame.draw.rect(window, color, resetButton)

    # draw the button label (text)
    resetfont = pygame.font.SysFont(None, 25)
    text = resetfont.render("RESET", True, (255, 255, 255))
    text_rect = text.get_rect(center=resetButton.center)
    window.blit(text, text_rect)

# %% [markdown]
# 

# %% [markdown]
# Mark the rectangle/board with value - player number 

# %%
def markSqr(row, col, player, board):
    board[row][col] = player

# %% [markdown]
# Check if location is empty or not

# %%
def isEmpty(row, col, board):
    if board[row][col] == 0:
        return True
    return False

# %% [markdown]
# Check if board is full or not (In Draw Condition)

# %%
def isFull(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return False
    return True

# %% [markdown]
# Print board in terminal

# %%
def printBoard():
    print(squares)

# %% [markdown]
# Change turn 

# %%
def toggleTurn(player):
    return ((player % 2)+1)

# %% [markdown]
# Get center of circle to make figure

# %%
def getCenter(row, col):
    if row == 0 and col == 0:
        return pygame.Rect(70, 70, width, height)
    if row == 0 and col == 1:
        return pygame.Rect(180, 70, width, height)
    if row == 0 and col == 2:
        return pygame.Rect(290, 70, width, height)
    if row == 1 and col == 0:
        return pygame.Rect(70, 180, width, height)
    if row == 1 and col == 1:
        return pygame.Rect(180, 180, width, height)
    if row == 1 and col == 2:
        return pygame.Rect(290, 180, width, height)
    if row == 2 and col == 0:
        return pygame.Rect(70, 290, width, height)
    if row == 2 and col == 1:
        return pygame.Rect(180, 290, width, height)
    if row == 2 and col == 2:
        return pygame.Rect(290, 290, width, height)

# %% [markdown]
# Drawing circle or cross based on player at marked location

# %%
def makeFig(player, row, col):
    if (player == 1):
        rectDim = getCenter(row, col)
        pygame.draw.rect(window, RECTCOLOR, rectDim)
        pygame.draw.line(window, (14, 0, 124), (
            rectDim[0]+67, rectDim[1]+28), (rectDim[0] + width-67, rectDim[1] + height-28), LINEWIDTH)
        pygame.draw.line(window, (14, 0, 124), (
            rectDim[0] + width-67, rectDim[1]+28), (rectDim[0]+67, rectDim[1] + height-28), LINEWIDTH)
    if (player == 2):
        rectDim = getCenter(row, col)
        center = rectDim.center
        pygame.draw.rect(window, RECTCOLOR, rectDim)
        pygame.draw.circle(window, CIRCOLOR, center, RADIUS, CIRWIDTH)

# %% [markdown]
# Checking the game status (any player won the game or not)

# %%
def isWin(board):
    #status for vertical =0
    # for vertical condn
    for col in range(COLS):
        if (board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0):
            return [board[0][col],0,col]  
    #status for horizotal=1
    # for horizontal condn
    for row in range(ROWS):
        if (board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0):
            return [board[row][0],1,row]

    #status for right diagonal =2
    #status for left diagonal =3
    # for diagonal condn
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return [board[0][0],2,-1]
    if board[2][0] == board[1][1] == board[0][2] and board[1][1] != 0: 
        return [board[2][0],3,-1]
    # else
    return -1, -1,-1

# %% [markdown]
# Get line coordinate to print cut lines

# %%
def getLineCoordinate(value, position):
    if (position == 0):  # vertical
        if (value == 0):
            return [120, 100, 120, 360]
        if (value == 1):
            return [230, 100, 230, 360]
        if (value == 2):
            return [340, 100, 340, 360]
    else:  # horizontal
        if (value == 0):
            return [100, 120, 360, 120]
        if (value == 1):
            return [100, 230, 360, 230]
        if (value == 2):
            return [100, 340, 340, 360]

# %% [markdown]
# Printing cut Lines after winning the game 

# %%
def printCutLines(status,value,resetStatus):
    if resetStatus==0:
        if status==0 :
            dim = getLineCoordinate(value, 0)
            pygame.draw.line(window, (120, 0, 0),(dim[0], dim[1]), (dim[2], dim[3]), LINEWIDTH)
        elif status==1:
            dim = getLineCoordinate(value, 1)
            pygame.draw.line(window, (120, 0, 0),
                                (dim[0], dim[1]), (dim[2], dim[3]), LINEWIDTH)
        elif status==2:
            pygame.draw.line(window, (120, 0, 0), (110, 110), (360, 360), LINEWIDTH)
        elif status==3:
            pygame.draw.line(window, (120, 0, 0), (350, 110), (100, 360), LINEWIDTH)
    else:
        if status==0 :
            dim = getLineCoordinate(value, 0)
            pygame.draw.line(window, (0, 0, 0),(dim[0], dim[1]), (dim[2], dim[3]), LINEWIDTH)
        elif status==1:
            dim = getLineCoordinate(value, 1)
            pygame.draw.line(window, (0, 0, 0),
                                (dim[0], dim[1]), (dim[2], dim[3]), LINEWIDTH)
        elif status==2:
            pygame.draw.line(window, (0, 0, 0), (110, 110), (360, 360), LINEWIDTH)
        elif status==3:
            pygame.draw.line(window, (0, 0, 0), (350, 110), (100, 360), LINEWIDTH)

# %% [markdown]
# Get all the empty squares left 

# %%
def getEmptySquares(board):
    emptySquares = []
    for row in range(ROWS):
        for col in range(COLS):
            if isEmpty(row, col, board):
                emptySquares.append((row, col))
    return emptySquares

# %% [markdown]
# Making Empty Rectangles

# %%
def rectangles(board):
    if board[0][0] == 0:
        pygame.draw.rect(window, RECTCOLOR, (70, 70, width, height))
    if board[0][1] == 0:
        pygame.draw.rect(window, RECTCOLOR, (180, 70, width, height))
    if board[0][2] == 0:
        pygame.draw.rect(window, RECTCOLOR, (290, 70, width, height))
    if board[1][0] == 0:
        pygame.draw.rect(window, RECTCOLOR, (70, 180, width, height))
    if board[1][1] == 0:
        pygame.draw.rect(window, RECTCOLOR, (180, 180, width, height))
    if board[1][2] == 0:
        pygame.draw.rect(window, RECTCOLOR, (290, 180, width, height))
    if board[2][0] == 0:
        pygame.draw.rect(window, RECTCOLOR, (70, 290, width, height))
    if board[2][1] == 0:
        pygame.draw.rect(window, RECTCOLOR, (180, 290, width, height))
    if board[2][2] == 0:
        pygame.draw.rect(window, RECTCOLOR, (290, 290, width, height))

# %% [markdown]
# Get coordinates of matrix (which rectangle is touched in the window)

# %%
def getCoordinates(xpos, ypos):
    if (xpos >= 70 and xpos <= 170 and ypos >= 70 and ypos <= 170):
        return [0, 0]
    if (xpos >= 70 and xpos <= 170 and ypos >= 180 and ypos <= 280):
        return [0, 1]
    if (xpos >= 70 and xpos <= 170 and ypos >= 290 and ypos <= 390):
        return [0, 2]
    if (xpos >= 180 and xpos <= 280 and ypos >= 70 and ypos <= 170):
        return [1, 0]
    if (xpos >= 180 and xpos <= 280 and ypos >= 180 and ypos <= 280):
        return [1, 1]
    if (xpos >= 180 and xpos <= 280 and ypos >= 290 and ypos <= 390):
        return [1, 2]
    if (xpos >= 290 and xpos <= 390 and ypos >= 70 and ypos <= 170):
        return [2, 0]
    if (xpos >= 290 and xpos <= 390 and ypos >= 180 and ypos <= 280):
        return [2, 1]
    if (xpos >= 290 and xpos <= 390 and ypos >= 290 and ypos <= 390):
        return [2, 2]

# %% [markdown]
# Print Status in window

# %%
def printStatus(winner,buttonStatus):
    text_surface = font.render("Winner : None", True, (51, 255, 255))
    if winner == 1 and buttonStatus==1:
        text_surface = font.render("Player 1 Won!", True, (51, 255, 255))
    elif winner == 2 and buttonStatus==1:
        text_surface = font.render("Player 2 Won!", True, (51, 255, 255))
    elif winner==1 and buttonStatus==0:
        text_surface = font.render("You Won!", True, (51, 255, 255))
    elif winner == 2 and buttonStatus==0:
        text_surface = font.render("Computer Won!", True, (51, 255, 255))
    elif winner ==-1 and isFull(squares):
        text_surface=font.render("It's a Draw!", True, (255, 0, 0))
    # Get the text surface's rect and center it on the window
    text_rect = text_surface.get_rect(center=(650, 100))
    # Blit the text surface onto the window
    window.blit(text_surface, text_rect)

# %% [markdown]
# Clear Status of winner in window

# %%
def clearStatus():
    pygame.draw.rect(window, (0, 0, 0), (550, 50, 400, 100))

# %% [markdown]
# Minimax funtion to calculate best move to play by computer

# %%
def miniMax(board, maximizing, alpha=-float('inf'), beta=float('inf')):
    # Terminal case
    finalState = isWin(board)[0]
    # Player - 1 wins
    if finalState == 1:
        return [1, None]
    # AI wins
    if finalState == 2:
        return [-1, None]
    # DRAW
    if finalState==-1 and isFull(board) == True:
        return [0, None]
        
    if maximizing:
        bestMove = None
        emptySquares = getEmptySquares(board)
        for (row, col) in emptySquares:
            tempBoard = copy.deepcopy(board)
            markSqr(row, col, 1, tempBoard)
            utility, _ = miniMax(tempBoard, False, alpha, beta)
            if utility > alpha:
                alpha = utility
                bestMove = (row, col)
            if alpha >= beta:
                break  # beta cutoff
        return alpha, bestMove
    else:
        bestMove = None
        emptySquares = getEmptySquares(board)
        for (row, col) in emptySquares:
            tempBoard = copy.deepcopy(board)
            markSqr(row, col, 2, tempBoard)
            utility, _ = miniMax(tempBoard, True, alpha, beta)
            if utility < beta:
                beta = utility
                bestMove = (row, col)
            if beta <= alpha:
                break  # alpha cutoff
        return beta, bestMove

# %% [markdown]
# Get coordinates of ai move

# %%
def getAiMove(board):
        # minimax
        return miniMax(board, False)[1]

# %% [markdown]
# Every time play the move which mark the matrix and increase number of marked values 

# %%
def playMove(board, coordinates, player, marked,buttonStatus,resetStatus):
    markSqr(coordinates[0], coordinates[1], player, board)
    marked += 1
    makeFig(player, coordinates[0], coordinates[1])
    if (isWin(board)[0] == -1 and isFull(board)):
        print("Draw")
        printCutLines(isWin(board)[1], isWin(board)[2],resetStatus)
        clearStatus()
        printStatus(isWin(board)[0],buttonStatus)
    elif (isWin(board)[0] != -1):
        print(str(isWin(board)[0]) + "Won")
        printCutLines(isWin(board)[1], isWin(board)[2],resetStatus)
        clearStatus()
        printStatus(isWin(board)[0],buttonStatus) 
    elif isWin(board)[0] == -1 and marked != 9:
        clearStatus()
        printStatus(isWin(board)[0],buttonStatus)

# %% [markdown]
# Print Game Mode pvp or pvc

# %%
def printGameMode(buttonStatus):
    font = pygame.font.Font(None, 40)
    if buttonStatus==0: #playing with AI
        text_surface = font.render("Player vs Computer", True, (255, 255, 102))
        # Get the text surface's rect and center it on the window
        text_rect = text_surface.get_rect(center=(660, 300))
        # Blit the text surface onto the window
        window.blit(text_surface, text_rect)
    else:
        text_surface = font.render("Player vs Player", True, (255, 255, 102))
        # Get the text surface's rect and center it on the window
        text_rect = text_surface.get_rect(center=(660, 300))
        # Blit the text surface onto the window
        window.blit(text_surface, text_rect)

# %% [markdown]
# Clear Game Mode

# %%
def clearGameMode():
    pygame.draw.rect(window, (0, 0, 0), (520, 240, 300, 150))

# %% [markdown]
# Reset the Game

# %%
def resetMode(board,resetStatus):
    if (isWin(board)[0] !=1):
        printCutLines(isWin(board)[1], isWin(board)[2],resetStatus)
    for row in range (ROWS):
        for col in range (COLS):
            board[row][col]=0

# %%
def main():
    resetButtonStatus = "default"

    run = True
    player = 1
    marked = 0
    stillCanPlay = False
    buttonStatus=0
    resetStatus=0
    while run:
        rectangles(squares)
        if marked == 0 and isWin(squares)[0] == -1:
            clearStatus()
            printStatus(isWin(squares)[0],buttonStatus)
            printGameMode(buttonStatus)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEMOTION:
                if resetButton.collidepoint(event.pos):
                    resetButtonStatus = "hover"
                else:
                    resetButtonStatus = "default"

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1]
                col = pos[0]
                if resetButton.collidepoint(event.pos):
                    resetButtonStatus = "clicked"
                    marked=0
                    player=1
                    resetStatus=1
                    resetMode(squares,resetStatus)
                    continue
                if button_rect.collidepoint(event.pos):
                    # Toggle button state
                    button_states.reverse()
                    button_text = font.render(button_states[0], True, BLACK)
                    # Move pointer to left or right
                    if button_states[0] == "left":
                        buttonStatus=0
                        pointer_rect.x = button_rect.x
                    elif button_states[0] == "right":
                        buttonStatus=1
                        pointer_rect.x = button_rect.x + button_rect.width/2
                    clearGameMode()
                    printGameMode(buttonStatus)
                if (buttonStatus==0): #Playing with AI
                    if (player==1):
                        if (row <= 390 and row >= 70 and col >= 70 and col <= 390):
                            coordinates = getCoordinates(row, col)
                            if isEmpty(coordinates[0], coordinates[1], squares):
                                playMove(squares, coordinates, player, marked,buttonStatus,resetStatus)
                                player = toggleTurn(player)
                                printBoard()
                    if player == 2 and not isFull(squares):
                        coordinates = getAiMove(squares)
                        print(coordinates)
                        playMove(squares, coordinates, player, marked,buttonStatus,resetStatus)
                        player = toggleTurn(player)
                        printBoard()
                else:  #2 Player Game
                    if (row <= 390 and row >= 70 and col >= 70 and col <= 390):
                        coordinates = getCoordinates(row, col)
                        if isEmpty(coordinates[0], coordinates[1], squares):
                            playMove(squares, coordinates, player, marked,buttonStatus,resetStatus)
                            player = toggleTurn(player)
                            printBoard()
        
        # Draw button and pointer
        pygame.draw.rect(window, GRAY, button_rect)
        pygame.draw.rect(window, WHITE, pointer_rect)
        pygame.draw.rect(window, (255, 255, 255),
                         (55, 55, 350, 350), 2)  # hollow rectangle

        draw_button(window, resetButtonStatus)
        pygame.display.update()

    pygame.quit()


main()