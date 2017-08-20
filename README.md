# Battleship
In this repository I have implemented a Board for the battleship game including the attack feature.

## Code Structure
The code is stored in the ```src``` folder. Tests are in the ```test``` folder.

### Modules Description
1) board.py - Board class that implements the game API and BoardTracker class that tracks the number of sunken ships
2) battleship.py - Battleship class that keep tracks of number of hits
3) cells.py - Cell class implementing a method ```attack``` that handles attacks on the different cell types in the board
4) outcomes.py - module that defines the possible API answers (HIT, MISS, ALREADY_TAKEN, SUNK, WIN)
5) example.py - to run the API example below ```python src/example.py```

### API Usage Example
Create a 5x5 empty board:
```python
from board import Board
game_board = Board(size_x=5, size_y=5)
```
Place a ship of length 3 horizontally starting at position ```(1, 1)```:
```python
game_board.place_ship(length=3, start_x=1, start_y=1, is_horizontal=True)
```
Place a ship of length 4 vertically starting at position ```(4, 1)```:
```python
game_board.place_ship(length=4, start_x=4, start_y=1, is_horizontal=False)
```
Attack an empty cell:
```python
game_board.attack(0, 0) # MISS
```
Attack and sink a ship:
```python
game_board.attack(1, 1) # HIT
game_board.attack(2, 1) # HIT
game_board.attack(3, 1) # SUNK
```
