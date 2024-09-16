from sqlalchemy import Column, Integer, String, Numeric
from database.config import Base

class Account(Base):
    __tablename__ = 'accounts'

    account_id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    account_type = Column(String)
    balance = Column(Numeric(18, 2))