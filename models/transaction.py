
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    transaction_date = Column(DateTime)
    amount = Column(Numeric)
    transaction_type = Column(String)
    description = Column(String)

    account = relationship("Account", back_populates="transactions")
