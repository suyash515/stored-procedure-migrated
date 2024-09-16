
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from database.connection import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    account_type = Column(String)
    balance = Column(Numeric)

    transactions = relationship("Transaction", back_populates="account")

    def has_sufficient_balance(self, amount):
        return self.balance >= amount
