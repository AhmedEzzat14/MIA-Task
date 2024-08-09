# Import the modules we need
import pygame
import numpy as np

# Intializing PyGame
pygame.init()

# Set the dimensions of chess game screen
Width = 800
Height = 800
Game_Display = pygame.display.set_mode((Width,Height))

# Set colours of the chess board and the startup of black rectangles
White,Black = (255,255,255),(50,50,50)
X,Y = 200,0
run = True   

# First white has no turn
# Second White has turn
# Third black has no turn 
# Fourth black has turn
step = 0
Movement = 100
Valid_Moves = [] 
Game_Over = False  

Captured_White_Pieces = []
captured_Black_Pieces = []

# Put pieces onto board
def Put_Pieces(row,column,piece):
    Game_Display.blit(piece,(row*100,column*100))

# Set the game variables and their icons
White_Pieces = ['pawn', 'pawn', 'pawn', 'pawn',
                'pawn', 'pawn', 'pawn', 'pawn',
                'rook', 'knight', 'bishop', 'queen',
                'king', 'bishop', 'knight', 'rook']

White_Locations = [(0,1), (1,1), (2,1), (3,1),
                   (4,1), (5,1), (6,1) ,(7,1),
                   (0,0), (1,0), (2,0), (3,0),
                   (4,0), (5,0), (6,0), (7,0)]

Black_Pieces = ['pawn', 'pawn', 'pawn', 'pawn',
                'pawn', 'pawn', 'pawn', 'pawn',
                'rook', 'knight', 'bishop', 'queen',
                'king', 'bishop', 'knight', 'rook']

Black_Locations = [(0,6), (1,6), (2,6), (3,6),
                   (4,6), (5,6), (6,6) ,(7,6),
                   (0,7), (1,7), (2,7), (3,7),
                   (4,7), (5,7), (6,7), (7,7)]

White_Pieces_Movement = []
Black_Pieces_Movement = []

# Loading the game pieces images
White_Rook = pygame.image.load('batman.png')
White_Rook = pygame.transform.scale(White_Rook, (100,100))
White_Rook_Small = pygame.transform.scale(White_Rook, (60,60))

White_Pawn = pygame.image.load('cyborg.png')
White_Pawn = pygame.transform.scale(White_Pawn, (100,100))
White_Pawn_Small = pygame.transform.scale(White_Pawn, (60,60))

White_Knight = pygame.image.load('flash.png')
White_Knight = pygame.transform.scale(White_Knight, (100,100))
White_Knight_Small = pygame.transform.scale(White_Knight, (60,60))

White_Bishop = pygame.image.load('greenlantern.png')
White_Bishop = pygame.transform.scale(White_Bishop, (100,100))
White_Bishop_Small = pygame.transform.scale(White_Bishop, (60,60))

White_King = pygame.image.load('captainamerica.png')
White_King = pygame.transform.scale(White_King, (100,100))
White_King_Small = pygame.transform.scale(White_King, (60,60))

White_Queen = pygame.image.load('scarletwitch.png')
White_Queen = pygame.transform.scale(White_Queen, (100,100))
White_Queen_Small = pygame.transform.scale(White_Queen, (60,60))

Black_Bishop = pygame.image.load('spiderman.png')
Black_Bishop = pygame.transform.scale(Black_Bishop, (100,100))
Black_Bishop_Small = pygame.transform.scale(Black_Bishop, (60,60))

Black_Knight = pygame.image.load('blackpanther.png')
Black_Knight = pygame.transform.scale(Black_Knight, (100,100))
Black_Knight_Small = pygame.transform.scale(Black_Knight, (60,60))

Black_Pawn = pygame.image.load('antman.png')
Black_Pawn = pygame.transform.scale(Black_Pawn, (100,100))
Black_Pawn_Small = pygame.transform.scale(Black_Pawn, (60,60))

Black_King = pygame.image.load('superman.png')
Black_King = pygame.transform.scale(Black_King, (100,100))
Black_King_Small = pygame.transform.scale(Black_King, (60,60))

Black_Queen = pygame.image.load('wonderwoman.png')
Black_Queen = pygame.transform.scale(Black_Queen, (100,100))
Black_Queen_Small = pygame.transform.scale(Black_Queen, (60,60))

Black_Rook = pygame.image.load('ironman.png')
Black_Rook = pygame.transform.scale(Black_Rook, (100,100))
Black_Rook_Small = pygame.transform.scale(Black_Rook, (60,60))

# Grouping all white images and all black images
White_Images = [White_Rook, White_Pawn, White_Knight,
                White_Bishop, White_King, White_Queen]

White_Small_Images =[White_Rook_Small, White_Pawn_Small, White_Knight_Small,
                     White_Bishop_Small, White_King_Small, White_Queen_Small]

Black_Images = [Black_Bishop, Black_Knight, Black_Pawn,
                Black_King, Black_Queen, Black_Rook]

Black_Small_Images = [Black_Bishop_Small, Black_Knight_Small, Black_Pawn_Small,
                      Black_King_Small, Black_Queen_Small, Black_Rook_Small]

# Make a list for general pieces 
Pieces_List = ['Rook', 'Knight', 'Bishop',
               'King', 'Queen', 'Pawn']

# Make the board game for chess #

# Fill the board with white colour
Game_Display.fill(White)

# Fill the rows with black
for X in range(100,800,200):
    for Y in range(0,800,200):
            pygame.draw.rect(Game_Display, Black, [X,Y,100,100])

# Fill the coloumns with black
for X in range(0,800,200):
    for Y in range(100,800,200):
            pygame.draw.rect(Game_Display, Black, [X,Y,100,100])

# Put pawn pieces
for i in range(0,8):
    Put_Pieces(i,6,White_Pawn)

for i in range(0,8):
    Put_Pieces(i,1,Black_Pawn)    

# Put rook pieces
Put_Pieces(0,7,White_Rook)
Put_Pieces(7,7,White_Rook)

Put_Pieces(0,0,Black_Rook)
Put_Pieces(7,0,Black_Rook)

# Put knight pieces
Put_Pieces(1,7,White_Knight)
Put_Pieces(6,7,White_Knight)

Put_Pieces(1,0,Black_Knight)
Put_Pieces(6,0,Black_Knight)

# Put bishop pieces
Put_Pieces(2,7,White_Bishop)
Put_Pieces(5,7,White_Bishop)

Put_Pieces(2,0,Black_Bishop)
Put_Pieces(5,0,Black_Bishop)

# Put queen pieces
Put_Pieces(3,0,White_Queen)
Put_Pieces(3,7,Black_Queen)

# Put king pieces
Put_Pieces(4,0,White_King)
Put_Pieces(4,7,Black_King)

# Check valid movements of pieces
def Movement_Checker(pieces,locations,turn):
    Move_List = []
    All_Moves_List = []
    for i in range((len(pieces))):
        Location = locations[i]
        piece = pieces[i]
        if piece == 'Pawn':
         # Save pieces information in Move List
            Move_List = Pawn_Validation(Location,turn)
        elif piece == 'Rook':
            Move_List = Rook_Validation(Location,turn)
        elif piece == 'Knight':
            Move_List = Knight_Validation(Location,turn)
        elif piece == 'Bishop':
            Move_List = Bishop_Validation(Location,turn)
        elif piece == 'Queen':
            Move_List = Queen_Validation(Location,turn)     
        elif piece == 'King':
            Move_List = King_Validation(Location,turn)       

        All_Moves_List.append(Move_List)
    return All_Moves_List

# King movement validation
def King_Validation(position,color):
    Move_List = []
    if color == 'White':
        Against_List = Black_Locations
        Friends_List = White_Locations
    elif color == 'Black':
        Against_List = White_Locations
        Friends_List = Black_Locations
     
    # Kings checking the squares they can move
    kings = ((1,0), (1,1), (1,-1), (-1,0),
             (-1,1), (-1,-1), (0,1), (0,-1),)
    for i in range(8):
        king = (position[0] + kings[i][0], position[1] + kings[i][1])
        if (king not in Friends_List) and (0 <= king[0] <= 7) and (0 <= king[1] <=7):
            Move_List.append(king)
    return Move_List

# Queen movement validation
def Queen_Validation(position,color):
    # By combining bishop & rook moves
    Moves_List1 = Bishop_Validation(position,color)
    Moves_List2 = Rook_Validation(position,color)
    for i in range(len(Moves_List2)):
        Moves_List1.append(Moves_List2[i])
    return Moves_List1

# Bishop movement validation
def Bishop_Validation(position,color):
    Moves_List = []
    if color == 'White':
        Against_List = Black_Locations
        Friends_List = White_Locations
    elif color == 'Black':
        Against_List = White_Locations
        Friends_List = Black_Locations
    for i in range (4): # UP Right, UP Left, Down Right, Down Left
        Move = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i ==2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1   
        while Move:
            if(position[0] + (chain * x), position[1] + (chain * y)) not in Friends_List and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain *y) <= 7:
                Moves_List.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in Against_List:
                    Move = False
                chain += 1
            else:
                Move = False
    return Moves_List

# Rook movement validation
def Rook_Validation(position, color):
    Moves_List = []
    if color == 'white':
        Against_List = Black_Locations
        friends_list = White_Locations
    else:
        Against_List = Black_Locations
        enemies_list = White_Locations
    for i in range(4):  # Down, UP, Right, Left
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        path = True
        chain = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                Moves_List.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return Moves_List

# Pawn movement validation
def Pawn_Validation(position, color):
    Moves_List = []
    if color == 'white':
        if (position[0], position[1] + 1) not in White_Locations and (position[0], position[1] + 1) not in Black_Locations and position[1] < 7:
            Moves_List.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in White_Locations and  (position[0], position[1] + 2) not in Black_Locations and position[1] == 1:
            Moves_List.append((position[0], position[1] + 2))

        if (position[0] + 1, position[1] + 1) in Black_Locations:
            Moves_List.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in Black_Locations:
            Moves_List.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in White_Locations and (position[0], position[1] - 1) not in Black_Locations and position[1] > 0:
            Moves_List.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in White_Locations and (position[0], position[1] - 2) not in Black_Locations and position[1] == 6:
            Moves_List.append((position[0], position[1] - 2))

        if (position[0] + 1, position[1] - 1) in White_Locations:
            Moves_List.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in White_Locations:
            Moves_List.append((position[0] - 1, position[1] - 1))
    return Moves_List

# Knight movement validation
def Knight_Validation(position, color):
    Moves_List = []
    if color == 'white':
        Against_List = Black_Locations
        friends_list = White_Locations
    else:
        friends_list = Black_Locations
        Against_List = White_Locations

    # Check for knights, they can go two squares in one direction and one in another
    knights = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        knight = (position[0] + knights[i][0], position[1] + knights[i][1])
        if (knight not in friends_list) and (0 <= knight[0] <= 7) and (0 <= knight[1] <= 7):
            Moves_List.append(knight)
    return Moves_List

# Check for valid moves for just selected piece
def Check_Valid_Moves():
    if step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[Movement]
    return valid_options

# Draw valid moves on screen
def Draw_valid(Moves):
    if step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(Moves)):
        pygame.draw.circle(Game_Display, color, (Moves[i][0] * 100 + 50, Moves[i][1] * 100 + 50), 5)

# Draw captured pieces on side of screen
def draw_captured():
    for i in range(len(Captured_White_Pieces)):
        captured_piece = Captured_White_Pieces = [][i]
        index = Pieces_List.index(captured_piece)
        Game_Display.blit(Black_Small_Images[index], (825, 5 + 50 * i))
    for i in range(len(captured_Black_Pieces)):
        captured_piece = captured_Black_Pieces[i]
        index = Pieces_List.index(captured_piece)
        Game_Display.blit(White_Small_Images[index], (925, 5 + 50 * i))

# event handling
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    # Handling left mouse button clicks when the game is not over
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not Game_Over:
        x_coord = event.pos[0] // 100
        y_coord = event.pos[1] // 100
        click_coords = (x_coord, y_coord)
        # Handling player input during the first two turns
        if turn_step <= 1:
            # Check if the player clicked on forfeit squares
            if click_coords == (8, 8) or click_coords == (9, 8):
                winner = 'black'
            # Check if the clicked coordinates belong to white pieces
            if click_coords in White_Locations:
                selection = White_Locations.index(click_coords)
                if turn_step == 0:
                    turn_step = 1
            # Check if the clicked coordinates are valid moves for the selected white piece
            if click_coords in valid_moves and selection != 100:
                White_Locations[selection] = click_coords
                # Check for capturing black pieces
                if click_coords in Black_Locations:
                    black_piece = Black_Locations.index(click_coords)
                    Captured_White_Pieces.append(Black_Pieces[black_piece])
                    if Black_Pieces[black_piece] == 'king':
                        winner = 'white'
                    Black_Pieces.pop(black_piece)
                    Black_Locations.pop(black_piece)
                # Update move options for both black and white
                black_options = Movement_Checker(Black_Pieces, Black_Locations, 'black')
                white_options = Movement_Checker(
                    White_Pieces, White_Locations, 'white')
                turn_step = 2
                selection = 100
                valid_moves = []
        # Handling player input during the last two turns
        if turn_step > 1:
            # Check if the player clicked on forfeit squares
            if click_coords == (8, 8) or click_coords == (9, 8):
                winner = 'white'
            # Check if the clicked coordinates belong to black pieces
            if click_coords in Black_Locations:
                selection = Black_Locations.index(click_coords)
                if turn_step == 2:
                    turn_step = 3
            # Check if the clicked coordinates are valid moves for the selected black piece
            if click_coords in valid_moves and selection != 100:
                Black_Locations[selection] = click_coords
                # Check for capturing white pieces
                if click_coords in White_Locations:
                    white_piece = White_Locations.index(click_coords)
                    captured_Black_Pieces.append(White_Pieces[white_piece])
                    if White_Pieces[white_piece] == 'king':
                        winner = 'black'
                    White_Pieces.pop(white_piece)
                    White_Locations.pop(white_piece)
                # Update move options for both black and white
                black_options = Movement_Checker(
                    Black_Pieces, Black_Locations, 'black')
                white_options = Movement_Checker(
                    White_Pieces, White_Locations, 'white')
                turn_step = 0
                selection = 100
                valid_moves = []
# Running of the game
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()















