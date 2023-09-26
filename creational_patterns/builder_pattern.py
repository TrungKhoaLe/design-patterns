"""

Category: Creational pattern

Intent: Let us create complex objects step by step. The pattern allows us to produce
different types and representations of an object using the same construction code.

Real-world analogy:
    Build different computers by choosing different types of cpu, memory, and storage.

"""
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
    my_computer = ComputerBuilder()\
            .add_cpu("M2")\
            .add_memory("64GB")\
            .add_storage("1TB")\
            .build()
    print(my_computer.cpu)
