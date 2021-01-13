# TicTacToe
# Description: Allows 2 players to play a game of Tic Tac Toe
# First player is "O", second player is "X"
# When a player has won, the game draws a winning line to indicate game over
# Press "Enter" to play a new game at any point in the game

import pygame
import sys
import numpy

# Initialize the pygame
pygame.init()

# Create screen, initialize constants
WIDTH = 600
HEIGHT = WIDTH
BG_COLOR = (20, 189, 172)
GRID_LINE_COLOR = (13, 161, 146)
LINE_WIDTH = WIDTH//40
SQUARE_SIZE = WIDTH//3
COLOR1 = (242, 235, 211)
COLOR2 = (84, 84, 84)
CIRCLE_RADIUS = SQUARE_SIZE//3
SPACE_X = SQUARE_SIZE//4
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board
board = numpy.zeros((3, 3))


def draw_grid():
    for i in range(2):
        pygame.draw.line(screen, GRID_LINE_COLOR, (0, (i+1)*SQUARE_SIZE),
                         (WIDTH, (i+1)*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, GRID_LINE_COLOR, (((i+1)*SQUARE_SIZE), 0),
                         ((i+1)*SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def check_win(player):
    # check verticals
    won = False
    if player:
        p = 1
    else:
        p = 2
    for col in range(3):
        if p == board[0][col] == board[1][col] == board[2][col]:
            draw_ver_win_line(col, player)
            won = True

    # check horizontals
    for row in range(3):
        if p == board[row][0] == board[row][1] == board[row][2]:
            draw_hor_win_line(row, player)
            won = True

    # check diagonals
    if p == board[1][1] == board[0][0] == board[2][2]:
        draw_down_dia_win_line(player)
        won = True
    if p == board[1][1] == board[2][0] == board[0][2]:
        draw_up_dia_win_line(player)
        won = True
    return won


def draw_ver_win_line(col, player):
    midPointX = col*SQUARE_SIZE + SQUARE_SIZE//2
    if player:
        color = COLOR1
    else:
        color = COLOR2
    pygame.draw.line(screen, color, (midPointX, LINE_WIDTH),
                     (midPointX, HEIGHT-LINE_WIDTH), LINE_WIDTH)


def draw_hor_win_line(row, player):
    midPointY = row*SQUARE_SIZE + SQUARE_SIZE//2
    if player:
        color = COLOR1
    else:
        color = COLOR2
    pygame.draw.line(screen, color, (LINE_WIDTH, midPointY),
                     (WIDTH-LINE_WIDTH, midPointY), LINE_WIDTH)


def draw_up_dia_win_line(player):
    if player:
        color = COLOR1
    else:
        color = COLOR2
    line = LINE_WIDTH + SQUARE_SIZE//40
    pygame.draw.line(screen, color, (LINE_WIDTH*2, HEIGHT-LINE_WIDTH*2),
                     (WIDTH-LINE_WIDTH*2, LINE_WIDTH*2), line)


def draw_down_dia_win_line(player):
    if player:
        color = COLOR1
    else:
        color = COLOR2
    line = LINE_WIDTH + SQUARE_SIZE//40
    pygame.draw.line(screen, color, (LINE_WIDTH*2, LINE_WIDTH*2),
                     (WIDTH-LINE_WIDTH*2, HEIGHT-LINE_WIDTH*2), line)


def restart():
    screen.fill(BG_COLOR)
    draw_grid()
    global player, board, game_over
    player = True
    board = numpy.zeros((3, 3))
    game_over = False


def draw_shape():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen, COLOR1, (col*SQUARE_SIZE + SQUARE_SIZE//2,
                                     row*SQUARE_SIZE + SQUARE_SIZE//2),
                    CIRCLE_RADIUS, LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, COLOR2, (col*SQUARE_SIZE + SPACE_X,
                                                  row*SQUARE_SIZE + SQUARE_SIZE - SPACE_X),
                                 (col*SQUARE_SIZE + SQUARE_SIZE - SPACE_X,
                                  row*SQUARE_SIZE + SPACE_X),
                                 LINE_WIDTH + SQUARE_SIZE//40)
                pygame.draw.line(screen, COLOR2, (col*SQUARE_SIZE + SPACE_X,
                                                  row*SQUARE_SIZE + SPACE_X),
                                 (col*SQUARE_SIZE + SQUARE_SIZE - SPACE_X,
                                  row*SQUARE_SIZE + SQUARE_SIZE - SPACE_X),
                                 LINE_WIDTH + SQUARE_SIZE//40)


# Running part
draw_grid()
player = True
game_over = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if available_square(clicked_row, clicked_col):
                if player:
                    mark_square(clicked_row, clicked_col, 1)
                else:
                    mark_square(clicked_row, clicked_col, 2)
                if check_win(player):
                    game_over = True
                player = not player
                draw_shape()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                restart()

    pygame.display.update()
