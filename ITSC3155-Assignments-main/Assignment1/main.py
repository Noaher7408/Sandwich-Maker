### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        return self.machine_resources["bread"] >= ingredients["bread"] and \
            self.machine_resources["ham"] >= ingredients["ham"] and \
            self.machine_resources["cheese"] >= ingredients["cheese"]

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print(f'{sandwich_size} sandwich is ready. Bon appetit!')

### Make an instance of SandwichMachine class and write the rest of the codes ###

sm = SandwichMachine(resources)
while True:
    food = input('What would you like? (small/ medium/ large/ off/ report): ')
    if food == "off":
        break
    elif food == "report":
        print(f'Bread: {sm.machine_resources["bread"]} slice(s)')
        print(f'Ham: {sm.machine_resources["ham"]} slice(s)')
        print(f'Cheese: {sm.machine_resources["cheese"]} pound(s)')
    elif food == "small" or food == "medium" or food == "large":
        sandwich_ingredients = recipes[food]['ingredients']
        sandwich_cost = recipes[food]['cost']

        if sm.check_resources(sandwich_ingredients):
            print('Please insert coins.')
            coins = sm.process_coins()

            if sm.transaction_result(coins, sandwich_cost):
                change = coins - sandwich_cost
                print(f"Here is ${change} in change")
                sm.make_sandwich(food, sandwich_ingredients)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if sm.machine_resources["bread"] < sandwich_ingredients["bread"]:
                print('Sorry there is not enough bread.')
            elif sm.machine_resources["ham"] < sandwich_ingredients["ham"]:
                print('Sorry there is not enough ham.')
            elif sm.machine_resources["cheese"] < sandwich_ingredients["cheese"]:
                print('Sorry there is not enough cheese.')

