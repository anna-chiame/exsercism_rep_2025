"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """Calculate the estimate value after exchange

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.

    The function divides the given budget by the exchange rate to determine 
    how much of the foreign currency can be obtained for the specified budget. 
    """
    value_after_exchange = budget / exchange_rate
    return value_after_exchange
    
def get_change(budget, exchanging_value):
    """Calculate curency left after an exchange
    
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.

    This function subtracts the exchanged amount from the total budget
    and returns the amount of money left in a starting currency
    
    """
    remaining_money = budget - exchanging_value
    return remaining_money
  
def get_value_of_bills(denomination, number_of_bills):
    """Calculate value of bills

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.

    Function multiplies the denomination of a bill
    by the number of such bills to calculate the total value
    and returns only the integer part of that value.
    """
    total_value_of_bills = int (number_of_bills * denomination)
    return total_value_of_bills
    
def get_number_of_bills(amount, denomination):
    """Calculate number of bills

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.

    Function divides the total amount of bills into the value of a single bill
    to to determine how many full bills can be given, return only integer part.
    """
    number_of_bills = int(amount / denomination)
    return number_of_bills
 
def get_leftover_of_bills(amount, denomination):
    """Calculate leftover after exchanging into bills

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.

    Function determines how much money is left over when the total amount 
    is exchanged into bills of a given denomination.
    """
    leftover = amount % denomination
    return leftover
    
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculte value after exchange

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    The function calculates the real exchange rate (adding the spread to the current
    exchange rate) and then calculates the maximum amount you can get 
    from the exchange booth when exchanging your current budget,
    taking into account the denomination of the available bills. 
    """
    real_exchange_rate = (exchange_rate+((exchange_rate/100)*spread))
    result = budget / real_exchange_rate
    number_bills_from_booth = int (result / denomination)
    real_sum = number_bills_from_booth * denomination
    return real_sum
