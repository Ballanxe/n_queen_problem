
class BacktrackingMixing:

	def __init__(self, size):

		self.solve_backtracking(size)

	 
	def solve_backtracking(self, n):
	    solutions = [[]]
	    for row in range(n):
	        solutions = (solution+[i+1]
	                       for solution in solutions # first for clause is evaluated immediately,
	                                                 # so "solutions" is correctly captured
	                       for i in range(n)
	                       if not self.under_attack(i+1, solution))

	    print(self.get_positions(solutions)) 

	def under_attack(self, col, queens):
	    return col in queens or \
	           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

	def get_positions(self, answers):

		results = []
		final_results = []

		while True:
			
			try:
				result = list(enumerate(next(answers),start=1))
				results.append(result)
			except:

				break

		# final_results = [tuple(result[i][1] for i in range(len(result))) for result in results]
		for result in results:
			new_set = tuple(result[i][1] for i in range(len(result))) 
			final_results.append(new_set)

		return final_results
		# print(final_results)



variable =  BacktrackingMixing(4)


# # print(first_answer)

# get_positions(variable.solutions)




 



# 	final_results.append(new_set) 

# print(final_results)
# print(len(final_results))
# 	for i in range(len(result)):

# 		final.results.append()
# final_results.append(set(result[i][1] for result in results for i in range(len(result))))