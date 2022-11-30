# TicTacToe
Tic Tac Toe using pygame

1) New issue: error installing pygame
Solution:
pip install --upgrade setuptools
(need to update the setuptools for installing libraries like pygame)
2) Updated issue: There are no official precompiled pygame packages for Python 3.11 available yet, so pip install pygame doesn't work
solution: pip install pygame --pre
This gives the pre release version of the library

Improvements:
1. Handle case where mouse click is out of window
2. Can add a restart button
3. Handle event when mouse is held down instead of mouse click