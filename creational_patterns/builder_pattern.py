"""

Category: Creational pattern

Intent: Lets us create complex objects step by step. The pattern allows us to
produce different types and representations of an object using the same cons-
truction code.

Problem:
    Imagine building a complex object that requires laborious, step-by-step ini-
    tialization of many fields and nested objects. Such initialization code is
    usually buried inside a gigantic constructor with lots of parameters, or
    scattered all over the client code.


Solution:
    The builder pattern suggests that we extract the object construction code
    out of its own class and move it to a separate objects called builders.

    The pattern organizes object construction into a set of steps (add_cpu,
    add_memory, add_storage, etc.) as the below example.


Applicability:
    - Use the Builder pattern to get rid of a telescoping constructor,
    - use the Builder pattern when we want our code to be able to
    create different representations of some product,
    - use the builder to construct composite tree or other complex objects.

Real-world analogy:
    Build different computers by choosing different types of cpu, memory, and
    storage.

"""


# -- GENERIC EXAMPLE -- #
from abc import ABC, abstractmethod
from typing import Any


class Product1:
    def __init__(self):
        """
        The product object will have many parameters to configure. Ergo, it 
        makes sense to use the Builder design pattern.
        """
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def __str__(self) -> str:
        return f"Product parts: {', '.join(self.parts)}"


class Builder(ABC):
    """
    This is an interface specifying different methods used to create different
    parts of the Product objects.
    """
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        """
        We always start with a blank product object upon which other parts are
        built.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        The results are retrieved via this method. After returning the end re-
        sult to client, the builder is expected to produce other products.
        Hence, we observe the reset method being called after getting the re-
        sult.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Director:
    """
    This is an optional class and is responsible for executing the building
    steps in a particular sequence. Director is used when we want to produce
    products based on specific order or configuration. It is fine if we dont
    use Director as the client code can control builders directly.
    """
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


# -- SPECIFIC EXAMPLE -- #
class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None

    def set_cpu(self, cpu_type):
        self.cpu = cpu_type

    def set_memory(self, memory_type):
        self.memory = memory_type

    def set_storage(self, storage_type):
        self.storage = storage_type


class ComputerBuilder:
    def __init__(self):
        self.builder = Computer()

    def add_cpu(self, cpu_type):
        self.builder.set_cpu(cpu_type)
        return self

    def add_memory(self, memory_type):
        self.builder.set_memory(memory_type)
        return self

    def add_storage(self, storage_type):
        self.builder.set_storage(storage_type)
        return self

    def build(self):
        return self.builder


if __name__ == "__main__":
    # Client code for the generic example
    # Example 1: Building product objects via a Director
    builder = ConcreteBuilder()
    director = Director()
    director.builder = builder

    director.build_minimal_viable_product()
    print(str(builder.product))

    director.build_full_featured_product()
    print(str(builder.product))

    # Example 2: Building product objects without using Director
    builder.produce_part_a()
    builder.produce_part_b()
    print(str(builder.product))

    # Client code for the specific example
    my_computer = ComputerBuilder()\
            .add_cpu("M2")\
            .add_memory("64GB")\
            .add_storage("1TB")\
            .build()
    print(f"Result of the specific example {my_computer.cpu}")
