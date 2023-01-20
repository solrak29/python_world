from craps_strategy import CrapsStrategy, validate_balance


class PassLine(CrapsStrategy):
    '''
    Basic strategy of just playing the past line
    '''

    def __init__(self, bank_roll: float, base_bet: float):
        self.base_bet = base_bet
        super().__init__(bank_roll)


    @validate_balance
    def craps(self, roll: int):
        ''' Method when the roll is craps or 7,11 '''
        if roll in (7,11):
            self.win(self.base_bet )
        else:
            self.lost += 1
            self.end_balance -= self.base_bet
        print(f"PassLine => {self.end_balance}")


    def point_made(self, roll: int):
        '''Method when the point is initially made'''
        pass


    @validate_balance
    def point(self, roll: int):
        '''Method when the a point is rolled after it was made'''
        self.win(self.base_bet)
        print(f"PassLine => {self.end_balance}")


    def roll(self, roll: int):
        ''' Method called when the point is made and roll is not the point'''
        pass

    @validate_balance
    def out(self, roll: int):
        '''Method when you 7 out'''
        self.end_balance -= self.base_bet
        self.lost += 1
        print(f"PassLine => {self.end_balance}")

    def show_result(self):
        print(f'Winners {self.wins} Losers {self.lost} Final Balance {self.end_balance}')
        print(f'Percentage wins {self.wins/(self.wins+self.lost)}')
        print(f'Percentage lost {self.lost/(self.wins+self.lost)}')
        print(f'Max Winnings On Roll {self.max_win[0]} on roll {self.max_win[1]}')
