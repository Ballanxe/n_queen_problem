import psycopg2
from itertools import permutations

from sqlalchemy.engine import create_engine

from mixins import BacktrackingMixin

from models import Solution


class NQueens(BacktrackingMixin):
    """
    Creates an object with the amount of queens, and its respective solutions. The solution was borrowed from this author https://goo.gl/xd1bj1 and refactorized with OOP.

    Inherits from BacktrackingMixing that allows using backtracking algorithm. It was done just for illustration matters of DRY principles. 

    """

    def __init__(self, size, type):

        """
        size = Integer
        type = Integer

        """

        self.size = size
        self.type = type
        self.solutions_count = 0
        self.solutions = []

        if self.type == 1: 
            self.solve_brute_force()
        elif self.type == 2:
            self.solutions = self.solve_backtracking(self.size)

    def solve_brute_force(self):

        cols = range(self.size)

        for positions in permutations(cols):

            positive_diagonal = set(positions[i]+i for i in cols)
            negative_diagonal = set(positions[i]-i for i in cols)

            if self.size == len(positive_diagonal) == len(negative_diagonal):

                self.solutions_count += 1
                self.solutions.append(positions)


        return self.solutions

    def print_solutions(self):

        N=self.size
        solutions = self.solutions

        for solution in solutions:

            sol = solutions.index(solution) + 1
            print('Solution {}: {} \n'.format(sol, solution))
                
            print("\n".join(' o ' * i + ' X ' + ' o ' * (N-i-1) for i in solution) + "\n\n")











