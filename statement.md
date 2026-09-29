#Project Statement: Tic Tac Toe

##Problem Statement

Tic Tac Toe is a game almost everyone knows, but playing it usually needs pen and paper, and people often argue over whether someone actually won or whether a move was legal. The goal of this project is to build a small program that takes care of all of that automatically. It sets up the board, keeps track of whose turn it is, rejects moves that aren't allowed, and announces the result at the end. It's also a good beginner exercise for understanding how a simple game loop works in Python.

##Scope of the Project

**What the project covers:**

- A two-player game played in the terminal on one computer
- A 3x3 board with squares numbered 1 to 9
- Player names taken as input at the start
- Turn-by-turn play, alternating between X and O
- Input validation for wrong numbers, non-numeric text and already-filled squares
- Automatic win detection and draw detection

**What the project does not cover:**

- Playing against the computer (no AI opponent)
- Online or networked multiplayer
- A graphical interface
- Saving scores or game history between runs

##Target Users

- Two people who want a quick game without setting anything up
- Beginner programmers and students who want to read a simple, complete example of a Python game
- Teachers or learners looking for a small project that shows lists, functions, loops and conditionals working together

##High-Level Features

- Custom player names shown throughout the game
- Numbered board that gets redrawn after every move
- Checks all 8 possible winning lines
- Draw detection when the board fills up
- Error messages that let the player retry instead of crashing the program
- Clear win or draw message at the end of the game
