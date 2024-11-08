#!/usr/bin/python3

import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid_position(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N, solutions):
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_valid_position(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)
            board[row] = -1


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    main()
