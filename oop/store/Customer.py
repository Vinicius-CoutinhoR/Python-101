from .Person import Person


def get_data(shopping):
    return shopping.data


class Customer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.shoppingList = []

    def shopping_register(self, shopping):
        self.shoppingList.append(shopping)

    def getLastShoppingDate(self):
        return None if not self.shoppingList else \
            sorted(self.shoppingList, key=get_data)[-1].data

    def total_purchases(self):
        total = 0
        for purchase in self.shoppingList:
            total += purchase.value
        return total
