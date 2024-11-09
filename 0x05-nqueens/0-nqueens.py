#!/usr/bin/python3
"""
Optimized solution to the nqueens problem.
"""
import sys


def backtrack(row, n, cols, pos_diag, neg_diag, board, solutions):
    """
    Backtracking function to find all solutions for the n-queens problem.
    Args:
        row (int): Current row where the queen is to be placed.
        n (int): Total number of queens and the size of the board.
        cols (set): Set to track occupied columns.
        pos_diag (set): Set to track occupied positive diagonals.
        neg_diag (set): Set to track occupied negative diagonals.
        board (list): 2D list to represent the board state.
        solutions (list): List to store all possible solutions.
    """
    # Base case: if row reaches n, we've placed all queens successfully
    if row == n:
        # Collect solution as list of [row, col] positions and add to solutions
        solution = [[r, c] for r in range(n) for c in range(n) if board[r][c] == 1]
        solutions.append(solution)
        return

    # Try to place queen in each column of the current row
    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue  # Skip if placing a queen would cause a conflict

        # Place the queen
        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board[row][col] = 1

        # Move to the next row
        backtrack(row + 1, n, cols, pos_diag, neg_diag, board, solutions)

        # Backtrack: remove the queen and reset the sets
        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solves the n-queens problem and prints all solutions.
    Args:
        n (int): The number of queens and the size of the board (n x n).
    """
    # Initialize tracking sets and board
    cols = set()       # Tracks columns that are occupied
    pos_diag = set()   # Tracks positive diagonals (r + c)
    neg_diag = set()   # Tracks negative diagonals (r - c)
    board = [[0] * n for _ in range(n)]  # Initialize an n x n chessboard
    solutions = []     # List to store all found solutions

    # Start backtracking from the first row
    backtrack(0, n, cols, pos_diag, neg_diag, board, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check for proper command-line usage
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse and validate the argument
    try:
        n = int(args[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        # Call the nqueens function to solve for the given n
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
