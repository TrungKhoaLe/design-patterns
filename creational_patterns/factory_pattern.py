"""
Analogy:

Imagine we opened a burger restaurant that has ingredients necessary to create
different types of burgers. However, we don't want to put all the ingredients
to create a burger; we want each type of burger to have different ingredients.
The FACTORY design pattern can help us achieve this goal.
"""


class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print_(self):
        return self.ingredients


class BurgerFactory:
    def create_cheese_burger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)

    def create_deluxe_cheese_burger(self):
        ingredients = ["bun", "tomatoe", "lettuce", "cheese", "beef-patty"]
        return Burger(ingredients)


if __name__ == "__main__":
    print(BurgerFactory().create_cheese_burger().print_())
    print(BurgerFactory().create_deluxe_cheese_burger().print_())
