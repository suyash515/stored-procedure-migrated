from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

# Database setup - Adjust connection string as necessary
database_uri = 'sqlite:///example.db'  # Change this to your database connection string
engine = create_engine(database_uri)
metadata = MetaData(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Define the Accounts model
Accounts = Table('Accounts', metadata,
    Column('AccountID', Integer, primary_key=True),
    Column('AccountNumber', String),
    Column('AccountType', String),
    Column('Balance', Integer)
)

# Function to get customer balance using SQLAlchemy
def get_customer_balance(account_id):
    connection = engine.connect()
    try:
        # Equivalent SQL: SELECT a.AccountNumber, a.AccountType, a.Balance FROM Accounts a WHERE a.AccountID = :account_id
        query = Accounts.select().where(Accounts.c.AccountID == account_id)
        result = connection.execute(query).fetchone()
        if result:
            return {'AccountNumber': result.AccountNumber, 'AccountType': result.AccountType, 'Balance': result.Balance}
        else:
            return None  # Account not found
    finally:
        connection.close()