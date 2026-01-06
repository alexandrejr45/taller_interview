import unittest


from exceptions import UsernameException
from user import User

class TestUser(unittest.TestCase):

    def test_this_works(self):
        with self.assertRaises(UsernameException):
            raise UsernameException()

    def test_should_charge_correct_amount_with_balance(self):
        john = User(username="john", balance=5, credit_card_number="4111111111111111", credit_card_balance=1000)
        jeff = User(username='jeff', balance=20, credit_card_number="4242424242424242", credit_card_balance=2000)

        john.pay(jeff, 5, note='coffe')
        jeff.pay(john, 10, note='breakfast')

        assert john.balance == 10
        assert jeff.balance == 15
        assert john.credit_card.credit_balance == 1000
        assert jeff.credit_card.credit_balance == 2000
