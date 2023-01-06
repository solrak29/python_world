from abc import ABC, abstractmethod

def validate_balance(function):

    def wrapper(self, value):
        print(f'calling validate {self.end_balance}')
        if self.end_balance < 1:
            print('No play balance is 0')
        else:
            func = function(self, value)
    return wrapper


class CrapsStrategy(ABC):

    def __init__(self, bank_roll: float):
        self.start_balance = bank_roll
        self.end_balance = bank_roll
        super().__init__()

    @abstractmethod
    def craps(self, roll: int):
        ''' Method when the roll is craps or 7,11 '''
        pass

    @abstractmethod
    def point_made(self, roll: int):
        '''Method when the point is initially made'''
        pass

    @abstractmethod
    def point(self, roll: int):
        '''Method when the a point is rolled after it was made'''
        pass

    @abstractmethod
    def roll(self, roll: int):
        ''' Method called when the point is made and roll is not the point'''
        pass

    @abstractmethod
    def out(self, roll: int):
        '''Method when you 7 out'''
        pass

    @abstractmethod
    def show_result(self):
        '''Method when you 7 out'''
        pass
