# Tic-Tac-Toe (איקס עיגול)

A simple two-player Tic-Tac-Toe game that runs in the terminal. The board and prompts are in Hebrew.

## Requirements

- Python 3

## How to run

From the project folder:

```bash
python tiktaktok.py
```

On some systems you may need:

```bash
python3 tiktaktok.py
```

## How to play

1. Player **X** starts, then players take turns with **O**.
2. On your turn, enter a row and a column as two numbers from `1` to `3`, separated by a space.
   - Example: `1 3` places a mark in the first row, third column.
3. The game ends when a player gets three in a row (horizontal, vertical, or diagonal), or when the board is full (draw).
4. Invalid input or a taken cell is rejected, and you are asked to try again.

## Project files

| File | Description |
|------|-------------|
| `tiktaktok.py` | Game logic: board display, win/draw checks, and the main loop |
