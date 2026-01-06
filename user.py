import re
from exceptions import UsernameException, PaymentException, BalanceException
from payment import Payment, CreditCard


class User:

    def __init__(self, username, balance, credit_card_number, credit_card_balance):
        if self._is_valid_username(username):
            self.username = username
        else:
            raise UsernameException('Username not valid.')

        self.balance = 0
        self.credit_card = None

        self.create_balance(balance)
        self.create_credit_card(credit_card_number, credit_card_balance)


    def retrieve_feed(self):
        # TODO: add code here
        return []

    def add_friend(self, new_friend):
        # TODO: add code here
        pass

    def create_balance(self, amount):
        if amount <= 0.0:
            raise BalanceException('Amount must be a non-negative number.')
        self.balance += float(amount)

    def create_credit_card(self, credit_card_number, credit_card_balance=None):
        self.credit_card = CreditCard(self, credit_card_number, credit_card_balance)

    def add_to_balance(self, amount):
        self.balance += float(amount)

    def remove_from_balance(self, amount):
        self.balance -= float(amount)

    def pay(self, target, amount, note):
        amount = float(amount)

        if self.username == target.username:
            raise PaymentException('User cannot pay themselves.')

        if amount <= 0.0:
            raise PaymentException('Amount must be a non-negative number.')

        if self.pay_with_balance(target, amount, note):
            return True
        elif self.pay_with_card(target, amount, note):
            return True

        return False

    def pay_with_card(self, target, amount, note):
        if self.username == target.username:
            raise PaymentException('User cannot pay themselves.')


        if self.credit_card is None:
            raise PaymentException('Must have a credit card to make a payment.')

        self._charge_credit_card(amount)
        payment = Payment(amount, self, target, note, 'credit_card')
        target.add_to_balance(amount)

        return payment

    def pay_with_balance(self, target, amount, note):
        if amount <= self.balance:
            if isinstance(target, User):
                target.add_to_balance(amount)
                self.remove_from_balance(amount)
                return True

            raise PaymentException('The attribute is not an User object')

        return False

    def _is_valid_username(self, username):
        return re.match('^[A-Za-z0-9_\\-]{4,15}$', username)

    def _charge_credit_card(self, amount):
       self.credit_card.charge_amount(amount)