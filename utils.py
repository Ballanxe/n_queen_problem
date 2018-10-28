from db import Session, engine, Base
from models import Solution
from sqlalchemy import exc


def get_type_algorithm():

	while True:

		try: 

			type = int(input('Brute force [1]. Backtracking[2]. Press enter to use Bruteforce \n') or 1)

			if type == 1 or type == 2:
				return type
				
			else:
				print("That is not a valid option")

		except:

			print("That is not a valid option")


def get_size_input():

    while True:

        try:

            size = int(input('How many queens do you want? Press enter to use eight (8).\n') or 8)

            if size <= 1:
                print("Are you kidding me ?")
            if size <= 3:
                print("The fun starts with four (4) queens common dude...")
                continue
            return size 

        except ValueError:

            print("Why are you trying to break me ? Just numbers please !")


def store_solutions(size, solutions):

	Base.metadata.create_all(engine)
	session = Session()
	n_queen = size

	try:

		for solution in solutions: 

			queen_positions = Solution(n_queen, solution)
			session.add(queen_positions)
			session.commit()

		print('Queen number {} solutions added to database.'.format(n_queen))

	except exc.IntegrityError as e:

		session.rollback()
		print('Queen number {} solutions already exists in database.'.format(n_queen))
		
	session.close()