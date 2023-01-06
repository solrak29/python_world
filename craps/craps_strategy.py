from abc import ABC, abstractmethod

class CrapsStrategy(ABC):

    def __init__(self):
        super().__init__(self)

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
