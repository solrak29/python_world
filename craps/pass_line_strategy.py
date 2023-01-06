from craps_strategy import CrapsStrategy, validate_balance


class PassLine(CrapsStrategy):

    def __init__(self, bank_roll: float, base_bet: float):
        self.base_bet = base_bet
        self.wins = 0
        self.lost = 0
        super().__init__(bank_roll)


    @validate_balance
    def craps(self, roll: int):
        ''' Method when the roll is craps or 7,11 '''
        print("winner")
        self.wins += 1
        self.end_balance += self.base_bet


    def point_made(self, roll: int):
        '''Method when the point is initially made'''
        pass


    def point(self, roll: int):
        '''Method when the a point is rolled after it was made'''
        self.end_balance += self.base_bet
        self.wins += 1
        print("winner")


    def roll(self, roll: int):
        ''' Method called when the point is made and roll is not the point'''
        pass

    def out(self, roll: int):
        '''Method when you 7 out'''
        self.end_balance -= self.base_bet
        self.lost += 1
        print("loser")

    def show_result(self):
        print(f'Winners {self.wins} Losers {self.lost} Final Balance {self.end_balance}')
