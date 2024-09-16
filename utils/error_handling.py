class InsufficientFundsError(Exception):
    """Exception raised for errors in the transfer due to insufficient funds."""
    def __init__(self, message="Insufficient funds in account."):
        self.message = message
        super().__init__(self.message)