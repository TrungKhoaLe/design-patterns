"""

Category: Creational pattern

Intent: Provides us an interface for creating objects in a superclass, but allows
subclasses to alter the type the type of objects that will be created.

Problem: 
    Imagine I built an app for a specific use case, so a bulk of my code lives inside
    a particular class. Now, my app has become so popular that I have received a lot
    of requests from a company to incorporate their use case into the app.

    A the present, most of my code is coupled with that specific class. Adding the new
    customer's use case would require making changes to the entire codebase. If later
    I decide to add another use case to the app, I will probably need to make all of
    these changes again.

    As a result, I will end up with pretty nasty code, riddled with conditionals that
    switch the app's behavior depending on the customers' use cases.

Solution:
    The creational method pattern suggests that we replace direct object construction
    calls with calls to a special factory method. Objects returned by a factory method
    are often referred to as products.

Analogy: 
    Imagine we opened a burger restaurant that has ingredients necessary to create
different types of burgers. However, we don't want to put all the ingredients
to create a burger; we want each type of burger to have different ingredients.
The FACTORY design pattern can help us achieve this goal.

Applicability:
    - Use the Factory Method when we don't know beforehand the exact types and dependencies
    of the objects our code should work with,
    
    - use the Factory Method when we want to provide users of our library or framework with
    a way to extent its internal components,

    - use the Factory Method when we want to save system resources by reusing existing objects
    instead of rebulding them each time.
"""

from abc import ABC, abstractmethod

##############################################################################################
######################################GENERAL EXAMPLE########################################
##############################################################################################


class Factory(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        # use the product
        result = f"""Depending on created products that will be more specific in subclasses,
                     the core business result will be different{product.operation()}"""
        return result


class Product1(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product1):
    def operation(self) -> str:
        return "Result of ConcreteProduct1"


class ConcreteFactory1(Factory):
    def factory_method(self) -> Product1:
        return ConcreteProduct1()


##############################################################################################
######################################SPECIFIC EXAMPLE########################################
##############################################################################################


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
