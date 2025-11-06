from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    def descrivi(self):
        print("Sono una forma geometrica.")
