import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

def main():
    resources = data.resources
    recipes = data.recipes
    sandwich_maker_instance = SandwichMaker(resources)
    cashier_instance = Cashier()

    food = input("Enter sandwich size (small, medium, large): ")
    sandwich_ingredients = recipes[food]["ingredients"]
    if sandwich_maker_instance.check_resources(sandwich_ingredients):
        sandwich_cost = recipes[food]["cost"]
        print("Your order costs: $", sandwich_cost)
        coins = cashier_instance.process_coins()
        if cashier_instance.transaction_result(coins, sandwich_cost):
            sandwich_maker_instance.make_sandwich(food, sandwich_ingredients)

        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Ingredients are not available to make your order.")
if __name__=="__main__":
    main()
