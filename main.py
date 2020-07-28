 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 27/07/2020
 #    Version   : 1.0.1
 #    Game Name : Tic Tac Toe
 #    ------------------------------------------------------------------------------------------


#   for game
import pygame

#   game sound
pygame.mixer.init()

#   start pygame
pygame.init()

#   screen size input
screen_width = 550
screen_height = 550

# Colors
white = (255, 255, 255)
red = (255,0,77)
black = (0, 0, 0)
gameName = (255, 0, 77)
enterToPlay = (0,181,184)
quitGame = (254, 225, 26)
scoreHighScore = (254, 225, 26)
gameOver = (255, 0, 77)
enterToContinue = (90, 39, 193)
qToQuit = (39, 159, 0)
food = (255, 0, 77)


#   game control
run = True
won = False

#   game window
window = pygame.display.set_mode((screen_width, screen_height))

#   game font
font = pygame.font.SysFont(None, 30)

#   game title
pygame.display.set_caption("Tic Tac Toe")
pygame.display.update()

#   game icon
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#   draw rectangle
first = pygame.draw.rect(window, (255, 255, 255), (25, 25, 150, 150))
second = pygame.draw.rect(window, (255, 255, 255), (200, 25, 150, 150))
third = pygame.draw.rect(window, (255, 255, 255), (375, 25, 150, 150))

fourth = pygame.draw.rect(window, (255, 255, 255), (25, 200, 150, 150))
fifth = pygame.draw.rect(window, (255, 255, 255), (200, 200, 150, 150))
sixth = pygame.draw.rect(window, (255, 255, 255), (375, 200, 150, 150))

seventh = pygame.draw.rect(window, (255, 255, 255), (25, 375, 150, 150))
eighth = pygame.draw.rect(window, (255, 255, 255), (200, 375, 150, 150))
ninth = pygame.draw.rect(window, (255, 255, 255), (375, 375, 150, 150))


#   keep track of player
draw_object = 'rect'

#   prevent from double typing
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

#   display score to screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x,y])

#   play welcome music
def welcome():
    window.fill(black)
    text_screen("Tic Tac Toe By Montasim", gameOver, 160, 205)
    text_screen("Press Enter To Continue", enterToContinue, 160, 230)
    text_screen("Press Q To Quit", qToQuit, 200, 255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameloop()

            if event.key == pygame.K_q:
                quit()

    pygame.mixer.music.load('sounds/gameover.mp3')
    pygame.mixer.music.play()

#   play welcome music
def gameOverSound(player):
    window.fill(black)
    text_screen(f"Player {player} Won", scoreHighScore, 211, 200)
    text_screen("Game Over!", gameOver, 215, 235)
    text_screen("Press Q To Quit", qToQuit, 200, 265)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameloop()

            if event.key == pygame.K_q:
                quit()

    pygame.mixer.music.load('sounds/gameover.mp3')
    pygame.mixer.music.play()

def result(board):
    #   row wise check
    if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1):
        print("Player 2 Won")
        gameOverSound(2)
    elif  (board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2):
        print("Player 1 Won")
        gameOverSound(1)
    elif (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1):
        print("Player 2 Won")
        gameOverSound(2)
    elif (board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2):
        print("Player 1 Won")
        gameOverSound(1)
    elif (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1):
        print("Player 2 Won")
        gameOverSound(2)
    elif (board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2):
        print("Player 1 Won")
        gameOverSound(1)

    #   column wise check
    elif (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1):
        print("Player 2 Won")
        gameOverSound(2)
    elif (board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2):
        print("Player 1 Won")
        gameOverSound(1)
    elif (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1):
        print("Player 2 Won")
        gameOverSound(2)
    elif (board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2):
        print("Player 1 Won")
        gameOverSound(1)
    elif (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
        print("Player 2 Won")
        gameOverSound(2)
    elif (board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2):
        print("Player 1 Won")
        gameOverSound(1)

    #   cross check
    elif (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
        print("Player 2 Won")
        gameOverSound(2)
    elif (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
        print("Player 1 Won")
        gameOverSound(1)
    elif (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
        print("Player 2 Won")
        gameOverSound(2)
    elif (board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2):
        print("Player 1 Won")
        gameOverSound(1)

    #   game tie
    else:
        print("Game Running")


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#   game loop
while run:
    #   set a delay
    pygame.time.delay(100)

    #   if close icon is pressed close the game
    for event in pygame.event.get():

        #   quit event
        if event.type == pygame.QUIT:
            run = False

        #   get mouse position
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            #   print(position)

            if won != True:
                if first.collidepoint(position) and first_open:
                    # Draws a shapes based on whose turn it is
                    if draw_object == 'circle':
                        # pygame.draw.circle(surface, (color), (centerx, centery),radius)
                        pygame.draw.circle(window, (255, 0, 0), (100, 100), 50)
                        draw_object = 'rect'
                        board[0][0] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (50, 50, 100, 100))
                        draw_object = 'circle'
                        board[0][0] = 2
                    # Marks this space as taken
                    first_open = False

                if second.collidepoint(position) and second_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(window, (255, 0, 0), (275, 100), 50)
                        draw_object = 'rect'
                        board[0][1] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (225, 50, 100, 100))
                        draw_object = 'circle'
                        board[0][1] = 2
                    second_open = False

                if third.collidepoint(position) and third_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(window, (255, 0, 0), (450, 100), 50)
                        draw_object = 'rect'
                        board[0][2] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (400, 50, 100, 100))
                        draw_object = 'circle'
                        board[0][2] = 2
                    third_open = False

                if fourth.collidepoint(position) and fourth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(window, (255, 0, 0), (100, 275), 50)
                        draw_object = 'rect'
                        board[1][0] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (50, 225, 100, 100))
                        draw_object = 'circle'
                        board[1][0] = 2
                    fourth_open = False

                if fifth.collidepoint(position) and fifth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(window, (255, 0, 0), (275, 275), 50)
                        draw_object = 'rect'
                        board[1][1] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (225, 225, 100, 100))
                        draw_object = 'circle'
                        board[1][1] = 2
                    fifth_open = False

                if sixth.collidepoint(position) and sixth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(window, (255, 0, 0), (450, 275), 50)
                        draw_object = 'rect'
                        board[1][2] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (400, 225, 100, 100))
                        draw_object = 'circle'
                        board[1][2] = 2
                    sixth_open = False

                if seventh.collidepoint(position) and seventh_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(window, (255, 0, 0), (100, 450), 50)
                        draw_object = 'rect'
                        board[2][0] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (50, 400, 100, 100))
                        draw_object = 'circle'
                        board[2][0] = 2
                    seventh_open = False

                if eighth.collidepoint(position) and eighth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(window, (255, 0, 0), (275, 450), 50)
                        draw_object = 'rect'
                        board[2][1] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (225, 400, 100, 100))
                        draw_object = 'circle'
                        board[2][1] = 2
                    eighth_open = False

                if ninth.collidepoint(position) and ninth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(window, (255, 0, 0), (450, 450), 50)
                        draw_object = 'rect'
                        board[2][2] = 1
                    else:
                        pygame.draw.rect(window, (0, 255, 0), (400, 400, 100, 100))
                        draw_object = 'circle'
                        board[2][2] = 2
                    ninth_open = False

            #   print(board)
            result(board)

    #   display rectangle
    pygame.display.update()

#   Closes game
pygame.quit()
quit()

#   welcome Screen
#   welcome()