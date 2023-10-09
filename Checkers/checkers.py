import pygame
from pygame.locals import *
from constants import WIDTH, HEIGHT, SQSIZE, BLACK, GREEN, WHITE, CLOUD, DARKGREY, GREY, playButton, exitButtonPause, exitButton, continueButton, resetButton, winnerPlate, ownerNameButton, ownerRollNo, easyButton, mediumButton, hardButton, extremeButton, ORANGE, PURPLE, RED
from pieces import *
from game import Game
from algorithm import minimax


pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")
font = pygame.font.SysFont('bitstreamverasans', 25, italic=True)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y//SQSIZE
    col = x//SQSIZE
    return row, col


def pauseOptions():
    # play option
    pygame.draw.rect(window, GREEN, continueButton, border_radius=50)
    text = font.render("Continue", True, (0, 0, 0))
    text_rect = text.get_rect(center=continueButton.center)
    window.blit(text, text_rect)

    # resetOption
    pygame.draw.rect(window, CLOUD, resetButton, border_radius=50)
    text = font.render("New Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=resetButton.center)
    window.blit(text, text_rect)

    # exit option
    pygame.draw.rect(window, DARKGREY, exitButtonPause, border_radius=50)
    text = font.render("Exit Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=exitButtonPause.center)
    window.blit(text, text_rect)
    pygame.display.update()


def playOptions():

    # ownerDetails
    # ownerName
    detailsFont = pygame.font.SysFont(
        'bitstreamverasans', 15, bold=False, italic=True)
    pygame.draw.rect(window, BLACK, ownerNameButton)
    text = detailsFont.render("Made By Ronit Chinda", True, (230, 0, 0))
    text_rect = text.get_rect(center=ownerNameButton.center)
    window.blit(text, text_rect)

    # ownerRollNo
    pygame.draw.rect(window, BLACK, ownerRollNo)
    text = detailsFont.render("RollNo - 2101174", True, (230, 0, 0))
    text_rect = text.get_rect(center=ownerRollNo.center)
    window.blit(text, text_rect)

    # play option
    pygame.draw.rect(window, CLOUD, playButton, border_radius=50)
    text = font.render("Play Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=playButton.center)
    window.blit(text, text_rect)

    # exit option
    pygame.draw.rect(window, GREY, exitButton, border_radius=50)
    text = font.render("Exit Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=exitButton.center)
    window.blit(text, text_rect)
    pygame.display.update()


def levelOptions():
    # Easy option
    pygame.draw.rect(window, GREEN, easyButton, border_radius=50)
    text = font.render("EASY", True, (0, 0, 0))
    text_rect = text.get_rect(center=easyButton.center)
    window.blit(text, text_rect)

    # Medium Option
    pygame.draw.rect(window, ORANGE, mediumButton, border_radius=50)
    text = font.render("MEDIUM", True, (0, 0, 0))
    text_rect = text.get_rect(center=mediumButton.center)
    window.blit(text, text_rect)

    # Hard option
    pygame.draw.rect(window, RED, hardButton, border_radius=50)
    text = font.render("HARD", True, (0, 0, 0))
    text_rect = text.get_rect(center=hardButton.center)
    window.blit(text, text_rect)
    pygame.display.update()

    # Extreme option
    pygame.draw.rect(window, PURPLE, extremeButton, border_radius=50)
    text = font.render("EXTREME", True, (0, 0, 0))
    text_rect = text.get_rect(center=extremeButton.center)
    window.blit(text, text_rect)

    pygame.display.update()


def gameOverOptions(winner):

    # results
    winFont = pygame.font.SysFont('bitstreamverasans', 35, bold=True)
    pygame.draw.rect(window, BLACK, winnerPlate, border_radius=20)
    text = font.render("Congratulations! " + winner +
                       " won the match", True, (255, 255, 255))
    text_rect = text.get_rect(center=winnerPlate.center)
    window.blit(text, text_rect)

    # resetOption
    pygame.draw.rect(window, CLOUD, resetButton, border_radius=50)
    text = font.render("New Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=resetButton.center)
    window.blit(text, text_rect)

    # exit option
    pygame.draw.rect(window, DARKGREY, exitButtonPause, border_radius=50)
    text = font.render("Exit Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=exitButtonPause.center)
    window.blit(text, text_rect)
    pygame.display.update()


def toggle_turn(game):
    if game.turn == BLACK:
        game.turn = WHITE
    else:
        game.turn = BLACK


def main():
    run = True
    game = Game(window)
    option = 0
    choosenLevel = False
    level = 1
    start = False
    pause = False
    gameOverStatus = False
    while run:
        if (not start):
            playOptions()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.collidepoint(event.pos):
                        start = True
                        window.fill(BLACK)
                        pygame.time.delay(600)
                        break
                    elif exitButton.collidepoint(event.pos):
                        run = False
                        break
            pygame.display.update()
        if not run:
            break
        elif start:
            if not choosenLevel:
                pygame.display.update()
                levelOptions()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if easyButton.collidepoint(event.pos):
                            choosenLevel = True
                            level = 1
                            pygame.time.delay(600)
                            break
                        elif mediumButton.collidepoint(event.pos):
                            choosenLevel = True
                            level = 1
                            pygame.time.delay(600)
                        elif hardButton.collidepoint(event.pos):
                            choosenLevel = True
                            level = 3
                            pygame.time.delay(600)
                        elif extremeButton.collidepoint(event.pos):
                            choosenLevel = True
                            level = 4
                            pygame.time.delay(600)

            if not run:
                break
            elif choosenLevel:
                if game.turn == WHITE:
                    value, new_board = minimax(game.get_board(), level, True)
                    if new_board:
                        game.ai_move(new_board)
                    toggle_turn(game)

                if game.board.isWin() is not None:
                    window.fill(BLACK)
                    pygame.display.update()
                    gameOverStatus = True
                    gameOverOptions(game.board.isWin())
                    pygame.time.delay(1000)
                    while gameOverStatus:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                gameOverStatus = False  # Exit the loop when the user clicks the X button
                                break
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if resetButton.collidepoint(event.pos):
                                    game = Game(window)
                                    gameOverStatus = False
                                    break
                                elif exitButtonPause.collidepoint(event.pos):
                                    run = False
                                    gameOverStatus = False  # Exit the loop when the user clicks the exit button
                                    break

                if not run:
                    break
                if game.turn == BLACK:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            break

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            row, col = get_row_col_from_mouse(pos)
                            game.select(row, col)

                        if event.type == pygame.KEYDOWN:
                            if event.key == K_ESCAPE:
                                window.fill(BLACK)
                                pygame.display.update()
                                pause = True
                                pauseOptions()
                                pygame.time.delay(1000)
                                while pause:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            run = False
                                            pause = False  # Exit the loop when the user clicks the X button
                                            break
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            if continueButton.collidepoint(event.pos):
                                                pause = False  # Continue the game when the user clicks the continue button
                                                window.fill(BLACK)
                                                pygame.time.delay(250)
                                                game.update()
                                                break
                                            elif resetButton.collidepoint(event.pos):
                                                game = Game(window)
                                                pause = False
                                                break
                                            elif exitButtonPause.collidepoint(event.pos):
                                                run = False
                                                pause = False  # Exit the loop when the user clicks the exit button
                                                break
                    game.update()

    pygame.quit()


main()
