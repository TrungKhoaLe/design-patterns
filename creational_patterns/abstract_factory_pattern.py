"""
Category: Creational pattern

Intent: Lets us create families of related objects without specifying their concrete
classes.

Problem: 
    Imagine that we are building a furniture shop simulator. Our code is comprised of
    several classes that represent:
    
    - A family of related products, e.g. Chair + Sofa + CoffeeTable,
    - several variants of that family, e.g. Chair + Sofa + CoffeeTable can have these
    variants - Modern, Victorian, ArtDeco.

    We need a way to create individual furniture objects so that they match other obj-
    ects of the same family.

    In addition, we don't want to change existing code when adding new products or fa-
    milies of products to the program.

Solution:
    Firstly, the abstract factory pattern suggests us declaring interfaces for each
    distinct product of the product family (e.g. chair, sofa, or coffee table). Then,
    we can make all variants of products following those interfaces,

    Secondly, declaring the abstract factory that has a list of creation methods for
    all products that are part of the product family (e.g. create_chair(), create_sofa(),
    and create_coffee_table()). Those methods must return abstract product types repre-
    sented by the interfaces defined in the step one,

    Thirdly, for each variant of a product family, we create a separate factory class
    based on the abstract factory interface declared in the step two. This class returns
    products of a particular kind. For example, the ModernFurnitureFactory can only
    create ModernChair, ModernSofa, and ModernCoffeeTable objects.

    Client works with both products and factories via their respective abstract interfaces.
    
Applicability:
    - Use the abstract factory when our code needs to work with various families of related
    products, but we do not want it to depend on the concrete classes of those products

    - consider using the abstract factory when we have a class with a set of factory methods
    that blur its primary responsibility.
"""
from abc import ABC, abstractmethod


class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):

    @abstractmethod
    def useful_function_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})."


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets us pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
