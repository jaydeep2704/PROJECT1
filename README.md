#Tic Tac Toe (Python, Terminal Version)

##Overview

This is a simple two-player Tic Tac Toe game that runs in the terminal. I built it in Python to practice working with lists, loops, functions and basic input handling. Two people sit at the same computer, type in their names, and take turns picking a number from 1 to 9 to place their mark on the board. The game figures out on its own when someone has won or when the board is full and it's a draw.

There's no GUI and no external library involved. Everything happens in plain text, so it should run on pretty much any machine that has Python installed.

##Features

- Two-player game on a single computer (Player 1 is X, Player 2 is O)
- Players enter their own names, and the game uses those names during play
- Board positions are numbered 1 to 9, so you always know what to type
- Checks all 8 winning combinations (3 rows, 3 columns, 2 diagonals)
- Detects a draw when all 9 spots are filled with no winner
- Handles bad input without crashing (letters, numbers out of range, or a spot that's already taken)
- Prints the board again after every move

##Technologies / Tools Used

- **Language:** Python 3
- **Libraries:** None (only built-in functions like `input()`, `print()` and `range()`)
- **Editor used:** Any text editor or IDE works (VS Code, PyCharm, IDLE, etc.)

##Steps to Install & Run

1. Make sure Python 3 is installed. You can check with:
   ```
   python --version
   ```
   If it isn't installed, download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository (or just download the ZIP and extract it):
   ```
   git clone <your-repository-link>
   ```

3. Open a terminal inside the project folder:
   ```
   cd <your-repository-folder>
   ```

4. Run the game:
   ```
   python Tic-Tac-Toe.py
   ```
   On some systems you may need to use `python3` instead of `python`.

5. Enter both player names when asked, then take turns typing a number between 1 and 9.

###How to play

The board starts out like this:

```
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
```

Type the number of the square where you want to place your mark. The first player to get three of their marks in a row (across, down or diagonally) wins. If all nine squares get filled and nobody has three in a row, it's a draw.

##Instructions for Testing

There's no automated test suite for this project, so testing is done by playing the game and checking a few situations by hand:

| What to test | What to do | Expected result |
|---|---|---|
| Normal win | Fill one full row, column or diagonal with the same player | Game prints a congratulations message with the winner's name and ends |
| Draw | Fill the board so no line has three matching marks | Game prints "It's a draw!" and ends |
| Taken spot | Choose a square that already has X or O | Message says the spot is taken, and the same player tries again |
| Out-of-range number | Enter `0`, `10` or `-3` | Message asks for a number between 1 and 9 |
| Non-number input | Enter a letter or leave the input blank | Message asks for a valid number, no crash |

A quick draw sequence to try (X and O alternating): `1, 2, 3, 5, 4, 6, 8, 7, 9`

A quick win sequence for Player 1: `1, 4, 2, 5, 3` (X takes the top row).

##Screenshots

_Uploaded in the Project File_

##Project Structure

```
.
├── Tic-Tac-Toe.py   # main game code
├── README.md        # this file
└── statement.md     # problem statement and scope
```

##Possible Future Improvements

- Add a single-player mode with a computer opponent
- Keep score across multiple rounds
- Ask the players if they want a rematch at the end
- Build a graphical version using Tkinter or Pygame
