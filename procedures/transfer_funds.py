
from sqlalchemy.orm import Session
from models.account import Account
from models.transaction import Transaction
from datetime import datetime

class TransferError(Exception):
    pass

def transfer_funds(db: Session, source_account_id: int, target_account_id: int, amount: float):
    source_account = db.query(Account).filter(Account.id == source_account_id).first()
    target_account = db.query(Account).filter(Account.id == target_account_id).first()

    if not source_account or not target_account:
        raise TransferError("Source or target account not found.")

    if not source_account.has_sufficient_balance(amount):
        raise TransferError("Insufficient funds in the source account.")

    source_account.balance -= amount
    target_account.balance += amount

    transaction_date = datetime.now()

    source_transaction = Transaction(
        account_id=source_account_id,
        transaction_date=transaction_date,
        amount=-amount,
        transaction_type='Debit',
        description=f'Transfer to Account {target_account_id}'
    )

    target_transaction = Transaction(
        account_id=target_account_id,
        transaction_date=transaction_date,
        amount=amount,
        transaction_type='Credit',
        description=f'Transfer from Account {source_account_id}'
    )

    db.add(source_transaction)
    db.add(target_transaction)
    db.commit()
