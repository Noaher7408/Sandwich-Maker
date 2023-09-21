class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("How many large dollars?: "))
        half_dollar = int(input("How many half dollars?: "))
        quarter = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        total = dollars + (half_dollar * 0.5) + (quarter * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        return coins >= cost
