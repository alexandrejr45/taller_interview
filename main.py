import uuid

from exceptions import CreditCardException, PaymentException
from user import User



class MiniVenmo:
    def create_user(self, username, balance, credit_card_number, credit_card_balance):
        user = User(username, balance, credit_card_number, credit_card_balance)
        return user


    def render_feed(self, feed):
        # Bobby paid Carol $5.00 for Coffee
        # Carol paid Bobby $15.00 for Lunch
        # TODO: add code here
        pass

    @classmethod
    def run(cls):
        venmo = cls()

        bobby = venmo.create_user(
            username="Bobby",
            balance=5.00,
            credit_card_number="4111111111111111",
            credit_card_balance=1000
        )
        carol = venmo.create_user(
            username="Carol",
            balance=10.00,
            credit_card_number="4242424242424242",
            credit_card_balance=2000
        )

        try:
            # should complete using balance
            bobby.pay(carol, 5.00, "Coffee")

            # should complete using card
            carol.pay(bobby, 20.00, "Lunch")


            print(bobby.credit_card.credit_balance)
            print(bobby.balance)
            print(carol.credit_card.credit_balance)
            print(carol.balance)
        except PaymentException as e:
            print(e)

        feed = bobby.retrieve_feed()
        venmo.render_feed(feed)

        bobby.add_friend(carol)


if __name__ == '__main__':
    MiniVenmo.run()