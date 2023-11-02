#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
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

def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (tuple): The first queen's position.
        pos1 (tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    row0, col0 = pos0
    row1, col1 = pos1
    return row0 == row1 or col0 == col1 or abs(row0 - row1) == abs(col0 - col1)

def build_solutions(n):
    """Builds all solutions for the N-Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list of lists: List of solutions.
    """
    def build_solution(row, current_solution):
        if row == n:
            solutions.append(current_solution.copy())
        else:
            for col in range(n):
                current_position = (row, col)
                if all(not is_attacking(current_position, pos) for pos in current_solution):
                    current_solution.append(current_position)
                    build_solution(row + 1, current_solution)
                    current_solution.pop()

    solutions = []
    build_solution(0, [])
    return solutions

def print_solutions(solutions):
    """Prints the solutions in the specified format.

    Args:
        solutions (list of lists): List of solutions.
    """
    for solution in solutions:
        print(solution)

if __name__ == "__main":
    n = get_input()
    solutions = build_solutions(n)
    print_solutions(solutions)
