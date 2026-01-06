import uuid

from exceptions import CreditCardException


class CreditCard:
    def __init__(self, user, number, credit_balance=None):
        self.user = user
        self.number = number
        self.credit_balance = credit_balance

    def validate_credit_card(self, user, number, credit_balance):
        if self.number is not None:
            raise CreditCardException('Only one credit card per user!')

        if self._is_valid_credit_card_number(number):
            self.number = number
        else:
            raise CreditCardException('Invalid credit card number.')

    def _is_valid_credit_card_number(self, credit_card_number):
        return credit_card_number in ["4111111111111111", "4242424242424242"]


    def charge_amount(self, amount):
        if amount <= self.credit_balance:
            self.credit_balance -= amount
            return True
        else:
            raise CreditCardException('Credit card does not have enough balance.')



class Payment:

    def __init__(self, amount, actor, target, note, payment_type):
        self.id = str(uuid.uuid4())
        self.type = payment_type
        self.amount = float(amount)
        self.actor = actor
        self.target = target
        self.note = note
