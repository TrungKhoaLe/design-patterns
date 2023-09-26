"""

Intent: This pattern lets us define a family of algorithms,
put each of them in a separate class, and make their objects
interchangeable.

Real-world analogy:
    We can use different stategies/methods to remove/filter values
    out of an array, be it removing positive or odd values

"""


from abc import ABC, abstractmethod


class FilterStrategy(ABC):
    @abstractmethod
    def remove_value(self, val):
        pass


class RemovePositiveValues(FilterStrategy):
    def remove_value(self, val):
        return val >= 0


class RemoveOddValues(FilterStrategy):
    def remove_value(self, val):
        return abs(val) % 2


class Values:
    def __init__(self, vals):
        self.vals = vals

    def filter(self, strategy):
        res = []
        for val in self.vals:
            if not strategy.remove_value(val):
                res.append(val)
        return res


if __name__ == "__main__":
    values = Values([-7, -4, -1, 0, 2, 6, 9])
    print(values.filter(RemovePositiveValues()))
    print(values.filter(RemoveOddValues()))
