import psycopg2
from itertools import permutations

from sqlalchemy.engine import create_engine

from mixins import BacktrackingMixing


engine = create_engine('postgresql+psycopg2://postgres:123456@172.17.0.3/n_queens_db?port=5432') ### 
connection = engine.connect()

class NQueens(BacktrackingMixing):

    def __init__(self, size):

        self.size = size
        self.solutions_count = 0
        self.solutions = []
        
        self.solve_brute_force()

        self.print_solutions(self.solutions)

    def solve_brute_force(self):

        cols = range(self.size)

        for positions in permutations(cols):

            positive_diagonal = set(positions[i]+i for i in cols)
            negative_diagonal = set(positions[i]-i for i in cols)

            if self.size == len(positive_diagonal) == len(negative_diagonal):

                self.solutions_count += 1
                self.solutions.append(positions)

        return self.solutions

    def print_solutions(self, solutions):

        N=self.size

        for solution in solutions:

            sol = solutions.index(solution) + 1
            print('Solution {}: {} \n'.format(sol, solution))
                
            print("\n".join(' o ' * i + ' X ' + ' o ' * (N-i-1) for i in solution) + "\n\n")


def get_size_input():

    while True:

        try:

            size = int(input('How many queens do you want? Leave blank to use eight (8).\n'))

            if size is None:
                return 8
            if size <= 1:
                print("Are you kidding me ?")
            if size <= 3:
                print("The fun starts with four (4) queens common dude...")
                continue
            return size 

        except ValueError:

            print("Why are you trying to break me ? Just numbers please !")


def main():
    
    n = get_size_input()
    
    NQueens(n)


if __name__ == "__main__":
    
    main()

# Dtabase name: n_queens_db
# database user: postgres
# database password: 123456
# database ip: 
# "HostPort": "32769"
# "IPAddress": "172.17.0.3"


# the ecuation of a line y = mx + c --> m es la pendiente y c es donde la recta intercepta el eje, combo [i] es la intercepcion de la recta y + i es la pendiente , entonces tienes una pendiente positiva y una pendiente negativa para probar ambas direcciones en las que se puede mover un alfil. Se usa set para evitar valores duplicados en la lista de posiciones lo que equivaldria 

# Para saber cuales cuales son las casilla en las que la reina puede estar comprometida, debemos usar, asumiendo que la reina se ecnuentra en (1,2), todas las casillas que tengan 1 en el primer indice y 2 en el segundo estan atacando y para saber cuales casillas atacan diagonalmente tenemos que restar 1 -2 da -1, todas las casillas en donde reste los valores y de -1 estan atacando igualmente para calcular la pendiente contraria todas las casillas que yo sume y de 3 estan atacando tambien, entonces tenemos que las diagonales son una de resta y la otra de suma.



# https://github.com/mission-peace/interview/blob/master/src/com/interview/recursion/NQueenProblem.java

# https://www.ploggingdev.com/2016/11/n-queens-solver-in-python-3/

#https://solarianprogrammer.com/2017/11/20/eight-queens-puzzle-python/

# https://rosettacode.org/wiki/N-queens_problem#Python


# docker and virtualenv
# https: // www.youtube.com/watch?v=QG84l1yMh-s

# docker and postgre
# https://www.youtube.com/watch?v=hO3UC3klumU

# Sharing docker image
# https://stackoverflow.com/questions/24482822/how-to-share-my-docker-image-without-using-the-docker-hub
