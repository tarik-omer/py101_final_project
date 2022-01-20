# Python101 Final Project - Tower Stack

  This is our final Py101 course project. It is the classic game of
Tower Stack - one of the many names it has been given. It is a simple, yet
fun and intriguing game.

  We will start by first explaining the building blocks of the game, both code-wise and play-wise:
We use one class for the Brick object, and one class for the Stack, which contains multiple bricks.

  The brick class contains functions for it's self-draw and for moving. The stack class is more complex,
since it contains multiple bricks. It sets up the initial stack and also contains the function to add a new
brick to the tower.

  Then, we have to important separate functions: game_over() and GAME(). GAME() contains the main loop for
the game, which waits for user input, but it also initializes some values. The game_over() function is called
whenever the user loses the game. It display the Game Over text and awaits further input.

  The command for playing the game are: SPACE / LMB - placing a brick, Q - quit, R - reset.
  
  In order to install the game you have to install pygame and a font used for the Game Over text:
sudo apt install python3
sudo apt install python3-pip
python3 -m pip install pygame
  
  and then, for the font:
    https://www.dafont.com/game-over.font

I hope that I was thorough enough! :)
  
