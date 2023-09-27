"""
Category: Structural pattern

Intent: This pattern provides a simplified interface to a library, a
framework, or any other complex set of classes.

Real-world analogy:
    When a call is made to a shop to place an order, an operator is the
    facade to all services and departments of the shop.
"""


class Facade:
    def __init__(self, subsystem1, subsystem2):
        # use existing subsystem objects or create them
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    def operation(self):
        return "Subsystem1: Ready!"

    def operation_n(self):
        return "Subsystem1: Go!"


class Subsystem2:
    def operation(self):
        return "Subsystem2: Ready!"

    def operation_n(self):
        return "Subsystem2: Fire!"


def client_code(facade):
    """
    client code works with complex subsystems through a simple interface
    provided by the Facade.
    """
    print(facade.operation(), end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
