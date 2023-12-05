from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Foreign


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    category = Column(String)
    date = Column(String)
    is_income = Column(Boolean)
