"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """return the value of the exchanged currency"""
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """return the remainder of the exchanged currency"""
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """return the value of the bills"""
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """return the number of bills"""
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """return the remainder of the bills"""
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """return the remainder of the exchanged currency"""
    # 1. Convert spread to decimal
    spread_decimal = spread / 100

    # 2. Adjust the exchange rate by adding the fee
    actual_rate = exchange_rate * (1 + spread_decimal)

    # 3. Convert your budget to the new currency
    exchanged = budget / actual_rate

    # 4. Determine how many whole bills you can get
    whole_bills = int(exchanged // denomination)

    # 5. Return the total value of those bills
    return whole_bills * denomination
