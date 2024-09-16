from sqlalchemy import create_engine, MetaData, Table, select

# Assuming the connection URL is set correctly
engine = create_engine('your_connection_url_here')
metadata = MetaData(bind=engine)
accounts = Table('Accounts', metadata, autoload_with=engine)

def get_customer_balance(account_id):
    with engine.connect() as connection:
        query = select([
            accounts.c.AccountNumber,
            accounts.c.AccountType,
            accounts.c.Balance
        ]).where(accounts.c.AccountID == account_id)

        result = connection.execute(query).fetchone()
        return {
            'AccountNumber': result.AccountNumber,
            'AccountType': result.AccountType,
            'Balance': result.Balance
        } if result else None