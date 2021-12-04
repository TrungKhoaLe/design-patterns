from __future__ import annotations
from abc import ABC, abstractmethod

class Logistics: 
    @abstractmethod
    def create_transport(self) -> str:
        """This is a factory method"""
        raise NotImplementedError

    def plan_delivery(self):
        transport = self.create_transport()
        result = f'Logistics: The same logistics\'s code  has just worked with {transport.deliver()}'
        return result

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

class Transport:
    """This is an interface"""
    def deliver(self):
        raise NotImplementedError

class Truck(Transport):
    def deliver(self) -> str:
        return '{Deliver by land in boxes}'

class Ship(Transport):
    def deliver(self) -> str:
        return '{Deliver by sea in containers}'

def client_code(logistics: Logistics) -> None:
    print(f'Client: I am not aware of the logistics\' class, but I still work.\n'
          f'{logistics.plan_delivery()}', end='')

if __name__ == '__main__':
    print('App: Launched with the RoadLogistics')
    client_code(RoadLogistics())
    print('\n')
    print('App: Launched with the SeaLogistics')
    client_code(SeaLogistics())
