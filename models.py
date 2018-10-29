import json

from sqlalchemy import Column, Integer, PickleType, String
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.types import TypeDecorator
from db import Base


class Json(TypeDecorator):

    impl = String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)


class Solution(Base):

	__tablename__ = "solution"

	pk = Column('id',Integer, primary_key=True)
	n_queen = Column('Queen number',Integer)
	solution = Column('Solution', Json(), unique=True)
	

	def __init__(self, n_queen, solution):
		self.n_queen = n_queen
		self.solution = solution

