from n_queens import NQueens
from utils import get_size_input, store_solutions, get_type_algorithm


def main():
    
    n = get_size_input()

    type = get_type_algorithm()
    
    problem = NQueens(n, type)

    problem.print_solutions()

    # solutions = problem.solutions

    store_solutions(n,problem.solutions)


if __name__ == "__main__":
    
    main()