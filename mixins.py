
class BacktrackingMixing:

	"""
	Mixing to use backtracking algorithm to solve the queens problem borrowed from this site https://goo.gl/5ZWtrh and refactorized with OOP.
	Also, I created the get_positions() functions, in order to return a list of tuples printable by the parents print_solutions() function   


	"""

	def solve_backtracking(self, n):

		"""
		n = Integer

		Receive a number of queens and returns a list of tuples printable by the parent's respective function. 

		"""
		solutions = [[]]
		for row in range(n):
			solutions = (solution+[i+1] for solution in solutions for i in range(n) if not self.under_attack(i+1, solution))

		return self.get_positions(solutions)

	def under_attack(self, col, queens):
	    return col in queens or \
	           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

	def get_positions(self, answers):

		"""
		For the sake of this problem I created this function in order to make this mixin compatible with the print function of the parent class 

		"""

		results = []
		final_results = []

		while True:
			
			try:
				result = list(enumerate(next(answers),start=1))
				results.append(result)
			except:

				break

		for result in results:
			new_set = tuple(result[i][1] for i in range(len(result))) 
			final_results.append(new_set)

		return final_results




