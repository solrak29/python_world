from abc import ABC, abstractmethod

def validate_balance(function):

    def wrapper(self, value):
        #print(f'calling validate for {self.__class__.__name__} {self.end_balance}')
        if self.end_balance < 1:
            print(f'{self.__class__.__name__}: No play balance is 0')
        else:
            func = function(self, value)
    return wrapper


class CrapsStrategy(ABC):

    def __init__(self, bank_roll: float):
        self.start_balance = bank_roll
        self.end_balance = bank_roll
        self.wins = 0
        self.lost = 0
        self.max_win = [0, 0]  # max win on which roll
        self.tracking = []  # track roll #, roll, and balance to see in graph
        super().__init__()


    def save( self, roll_num, roll):
        '''
            Tracks the rolls so we can plot the roll and balance on graph
            This call is done after all the calls are made base on the rolls.
            See craps_engine.py line 54
        '''
        self.tracking.append((roll, self.end_balance))


    def save_to_file(self):
        with open( f'{self.__class__.__name__}.csv', 'w') as f:
            for x,y in enumerate(self.tracking):
                f.write(f'{x},{y[0]},{y[1]}\n')


    def win(self, base_bet):
        print(f'wins {base_bet}')
        print(f'before {self.end_balance}')
        self.wins += 1
        self.end_balance = self.end_balance + base_bet
        self.end_balance = round(self.end_balance,2)
        print(f'wins {self.end_balance}')
        if self.max_win[0] < self.end_balance:
            self.max_win[0] = self.end_balance
            self.max_win[1] = self.wins + self.lost


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
