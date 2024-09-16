from sqlalchemy import Column, Integer, Numeric, String, DateTime
from database.config import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, index=True)
    transaction_date = Column(DateTime)
    amount = Column(Numeric(18, 2))
    transaction_type = Column(String)
    description = Column(String)