import pytest
from n_queens import NQueens


def test_solutions_brute_force_eight():

	problem = NQueens(8,1)
	assert problem.solutions_count == 92 
	assert len(problem.solutions) == 92 


def test_solutions_brute_force_nine():

	problem = NQueens(9,1)
	assert problem.solutions_count == 352
	assert len(problem.solutions) == 352 


def test_solutions_brute_force_ten():

	problem = NQueens(10,1)
	assert problem.solutions_count == 724
	assert len(problem.solutions) == 724


def test_solutions_backtracking_eight():

	problem = NQueens(8,2)
	assert problem.solutions_count == 92 
	assert len(problem.solutions) == 92 


def test_solutions_backtracking_nine():

	problem = NQueens(9,2)
	assert problem.solutions_count == 352
	assert len(problem.solutions) == 352 


def test_solutions_backtracking_ten():

	problem = NQueens(10,2)
	assert problem.solutions_count == 724
	assert len(problem.solutions) == 724

