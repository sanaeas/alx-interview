#!/usr/bin/python3
"""Solve the N queens problem"""
import sys


def main() -> None:
    """Main function to solve the challenge"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    def is_safe(board, row, col):
        """Check if it's safe to place a queen at board[row][col]"""
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        """Recursive function to find all possible queen placements"""
        if row == N:
            print([[r, c] for r, c in enumerate(board)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    solve([-1] * N, 0)


if __name__ == '__main__':
    main()
