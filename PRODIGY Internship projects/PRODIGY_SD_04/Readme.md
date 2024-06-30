# Sudoku Solver

This Python program solves Sudoku puzzles automatically using a backtracking algorithm. It takes an input grid representing an unsolved Sudoku puzzle and fills in the missing numbers to complete the puzzle.

## Features

- Reads a Sudoku puzzle from a predefined grid.
- Uses backtracking to find the correct arrangement of numbers.
- Prints the solved Sudoku puzzle.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the `sudoku_solver.py` file.

2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

3. Run the `sudoku_solver.py` script:

    ```bash
    python sudoku_solver.py
    ```

4. The program will print the unsolved Sudoku puzzle and the solved puzzle.

## Example

### Input (Unsolved Sudoku Puzzle)

```python
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
