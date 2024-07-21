from sqlalchemy import Column, Integer, String, Date
from database import Base


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    cpf = Column(String(11), unique=True)
    birthdate = Column(Date)
    email = Column(String, unique=True)
    state = Column(String)
