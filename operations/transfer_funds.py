from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.account import Account
from models.transaction import Transaction
from utils.error_handling import InsufficientFundsError
from datetime import datetime

def transfer_funds(db: Session, source_account_id: int, target_account_id: int, amount: float):
    source_account = db.query(Account).filter(Account.account_id == source_account_id).first()
    target_account = db.query(Account).filter(Account.account_id == target_account_id).first()

    if not source_account or not target_account:
        raise ValueError("One or both accounts do not exist.")

    if source_account.balance < amount:
        raise InsufficientFundsError("Insufficient funds in the source account.")

    try:
        # Deduct amount from source account
        source_account.balance -= amount
        # Add amount to target account
        target_account.balance += amount

        # Record the transaction for source account
        transaction_debit = Transaction(
            account_id=source_account_id,
            transaction_date=datetime.now(),
            amount=-amount,
            transaction_type='Debit',
            description=f'Transfer to Account {target_account_id}'
        )
        db.add(transaction_debit)

        # Record the transaction for target account
        transaction_credit = Transaction(
            account_id=target_account_id,
            transaction_date=datetime.now(),
            amount=amount,
            transaction_type='Credit',
            description=f'Transfer from Account {source_account_id}'
        )
        db.add(transaction_credit)

        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise e