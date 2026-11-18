from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass



class CardPayment(Payment):

    def pay(self, amount):
        # complex logic hidden here
        print("Processing card payment...")



Payment.pay(100)