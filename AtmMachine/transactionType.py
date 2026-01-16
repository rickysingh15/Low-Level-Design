
from enum import Enum

class TransactionType(Enum):

    DEBIT = "debit"
    CREDIT = "credit"
    CHECK_BALANCE = "check_balance"