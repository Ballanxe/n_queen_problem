from sqlalchemy import Column, Integer, PickleType
from sqlalchemy.schema import UniqueConstraint
from db import Base



class Solution(Base):

	__tablename__ = "solution"

	pk = Column('id',Integer, primary_key=True)
	n_queen = Column('Queen number',Integer)
	solution = Column('Solution', PickleType(), unique=True)
	

	def __init__(self, n_queen, solution):
		self.n_queen = n_queen
		self.solution = solution

