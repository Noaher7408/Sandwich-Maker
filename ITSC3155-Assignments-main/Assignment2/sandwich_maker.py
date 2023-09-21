
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        return self.machine_resources["bread"] >= ingredients["bread"] and \
            self.machine_resources["ham"] >= ingredients["ham"] and \
            self.machine_resources["cheese"] >= ingredients["cheese"]

    def make_sandwich(self, sandwich_size, order_ingredients):
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print(f'{sandwich_size} sandwich is ready. Bon appetit!')


