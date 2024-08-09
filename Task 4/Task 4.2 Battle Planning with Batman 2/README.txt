PyGame Chess Game

This project is a simple implementation of a chess game using the PyGame library. The game features custom piece images and basic movement validation for each type of piece. The project includes the following main functionalities:

                   1-Drawing the chess board
                   2-Placing the pieces on the board
                   3-Validating moves for each type of piece
                   4-Handling piece captures
                   5-Switching turns between players
                   6-Displaying captured pieces

Requirements:
	1-Python 3.x
	2-PyGame

Installation:
	1-Install Python from the official website: Python.org
	2-Install PyGame using pip:
		pip install pygame
How to Run:
	1-Save the provided code into a Python file (e.g., chess_game.py).
	2-Ensure you have the necessary piece images (batman.png, cyborg.png, etc.) in the     	same directory as the Python file.
	3-Run the Python file:
		python chess_game.py

Game Components:
	Main Variables:
		1-Width and Height: Dimensions of the game screen (800x800 pixels).
		2-Game_Display: The game display surface.
		3-White and Black: RGB color values for the chessboard.
		4-X, Y: Initial positions for drawing the chessboard.
		5-run: Boolean to control the game loop.
	  	6-step: Variable to track the turn (White's turn or Black's turn).
		7-Movement: Index for the current piece being moved.
		8-Valid_Moves: List of valid moves for the selected piece.
		9-Game_Over: Boolean to check if the game has ended.
		10-Captured_White_Pieces and captured_Black_Pieces: Lists to track captured 		pieces

Piece Placement:
	1-Put_Pieces(row, column, piece): Function to place pieces on the board.
	2-White_Pieces and Black_Pieces: Lists of piece types for each side.
	3-White_Locations and Black_Locations: Lists of coordinates for each piece on the 	board.
	4-White_Images and Black_Images: Lists of piece images for each side.

Piece Movement Validation:
	Movement_Checker(pieces, locations, turn): Function to check valid moves for all 	pieces of a player.
	Individual functions to validate moves for each type of piece:
		1-King_Validation(position, color)
		2-Queen_Validation(position, color)
		3-Bishop_Validation(position, color)
		4-Rook_Validation(position, color)
		5-Pawn_Validation(position, color)
		6-Knight_Validation(position, color)

Valid Moves and Captured Pieces:
	1-Check_Valid_Moves(): Function to check valid moves for the currently selected 	piece.
	2-Draw_valid(Moves): Function to draw valid moves on the board.
	3-draw_captured(): Function to draw captured pieces on the side of the screen.

Event Handling:
	The main event loop handles:
		1-Quitting the game
		2-Mouse clicks to select and move pieces
		3-Piece captures
		4-Turn switching
Game Loop:
	The game runs in a loop that updates the display and handles events until the user 	quits.

Additional Notes:
	1-Ensure the piece images (batman.png, cyborg.png, etc.) are properly named and 	placed in the same directory as the script.
	
	2-The current implementation does not include complex chess rules such as castling 	or checkmate detection.