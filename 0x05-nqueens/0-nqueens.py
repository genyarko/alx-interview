#!/usr/bin/python3
"""N-Queens Solver

This program finds and prints all possible solutions to the N-Queens problem.

Usage:
    nqueens N
    Where N is an integer greater than or equal to 4.
"""

import sys

solutions = []  # The list of possible solutions to the N-Queens problem.
n = 0  # The size of the chessboard.
pos = None  # The list of possible positions on the chessboard.

def get_input():
    """Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard (N).
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(position1, position2):
    """Checks if two queen positions are in an attacking mode.

    Args:
        position1 (list or tuple): The first queen's position.
        position2 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    row1, col1 = position1
    row2, col2 = position2
    return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)

def group_exists(new_group):
    """Checks if a group of positions exists in the list of solutions.

    Args:
        new_group (list of tuples): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for existing_solution in solutions:
        if all(pos in existing_solution for pos in new_group):
            return True
    return False

def build_solution(row, current_group):
    """Builds a solution for the N-Queens problem using backtracking.

    Args:
        row (int): The current row in the chessboard.
        current_group (list of tuples): The group of valid positions.
    """
    global solutions
    if row == n:
        new_solution = current_group.copy()
        if not group_exists(new_solution):
            solutions.append(new_solution)
    else:
        for col in range(n):
            current_position = (row, col)
            is_safe = all(not is_attacking(current_position, pos) for pos in current_group)
            if is_safe:
                current_group.append(current_position)
                build_solution(row + 1, current_group)
                current_group.pop()

def get_solutions():
    """Finds and stores all solutions for the given chessboard size (N).
    """
    global pos, n
    pos = [(i // n, i % n) for i in range(n * n)]
    row = 0
    current_group = []
    build_solution(row, current_group)

if __name__ == "__main__":
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)
