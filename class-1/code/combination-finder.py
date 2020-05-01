"""Combination Finder

Problem Statement

Alice is a shopper and buys fruits everyday worth of 100$ of different types.
One day he decided to buy 100 fruits with 100$ with combination
following types.

- Apple  - 5$/pc
- Orange - 1$/pc
- Banana - 0.5$/pc

Help Alice in finding the different combinations that he can buy 100
fruits with 100$. And make sure that at-least 1pc of each type.

Keep in mind that, because of the fact that prices of these fruits will get
varied/changed.
"""


def find_combinations():
    # input
    one_apple_price = 5.00
    one_orange_price = 1.00
    one_banana_price = 0.50

    # expected
    no_of_pieces_required = 100.00
    amount_available = 100.00

    # combination
    no_of_apples_required = 0  # Initially we don't know...
    no_of_oranges_required = 0  # Initially we don't know...
    no_of_bananas_required = 0  # Initially we don't know...
    total_combinations_available = 0

    print("Alice: The following is one of the combination.")
    for no_of_apples_required in range(0, 100):
        for no_of_oranges_required in range(0, 100):
            for no_of_bananas_required in range(0, 100):
                combination_count = (
                    no_of_apples_required +
                    no_of_oranges_required +
                    no_of_bananas_required
                )
                combination_price = (
                    (no_of_apples_required * one_apple_price) +
                    (no_of_oranges_required * one_orange_price) +
                    (no_of_bananas_required * one_banana_price)
                )
                if (
                    combination_count == no_of_pieces_required and
                    combination_price == amount_available
                ):
                    print(f"""-----------------------------------------------\n \
                    No of Apples = {no_of_apples_required}\n \
                    No of Oranges = {no_of_oranges_required}\n \
                    No of Bananas = {no_of_bananas_required}\n \
                    """)
                    total_combinations_available += 1
    print(f"""\
        Alice, there are `{total_combinations_available}` combinations \
        available. \
        \n\nHappy to help you Alice. Thank you\n""")

if __name__ == "__main__":
    find_combinations()
