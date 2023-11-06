from craps_strategy import CrapsStrategy, validate_balance


'''
Point numbers (2,3,12,11,7)

Any 7 pays 4 to 1
2,3 pays 15 to 1
11,12 pays 30 to 1


'''
class HornOnly(CrapsStrategy):
    '''
        This strategy will only play odds with winnings up to max odds set
        
    '''

    def __init__(self, bank_roll: float, base_bet: float, max_odds_multiplier: float = 0.0):
        self.base_bet = base_bet
        self.odds_bet = 0
        self.orig_bank_roll = bank_roll
        self.max_odds = max_odds_multiplier
        super().__init__(bank_roll)


    @validate_balance
    def craps(self, roll: int):
        ''' Method when the roll is craps or 7,11 '''
        if roll == 7:
            self.lost += 1
            self.end_balance -= (self.base_bet * 4)
        if roll in [11, 3]:
            self.win(self.base_bet * 15 - (self.base_bet * 4))
        if roll in [2, 12]:
            self.win(self.base_bet * 30 - (self.base_bet * 4))

    @validate_balance
    def point_made(self, roll: int):
        '''Method when the point is initially made'''
        '''Dont care about the point'''
        self.lost += 1
        self.end_balance -= (self.base_bet * 4)


    @validate_balance
    def point(self, roll: int):
        '''Method when the a point is rolled after it was made'''
        self.lost += 1
        self.end_balance -= (self.base_bet * 4)


    @validate_balance
    def roll(self, roll: int):
        ''' Method called when the point is made and roll is not the point'''
        if roll in [2,3,12,11]:
            if roll in [12,2]:
                self.win(self.base_bet * 30 - self.base_bet * 4)
            else:
                self.win(self.base_bet * 15 - self.base_bet * 4)
        else:
            self.lost += 1
            # horn bet you lose on all cases
            self.end_balance -= (self.base_bet * 4)
                

    @validate_balance
    def out(self, roll: int):
        '''Method when you 7 out'''
        self.lost += 1
        self.end_balance -= (self.base_bet * 4)

    def show_result(self):
        print(f'Winners {self.wins} Losers {self.lost} Final Balance {self.end_balance}')
        print(f'Percentage wins {self.wins/(self.wins+self.lost)}')
        print(f'Percentage lost {self.lost/(self.wins+self.lost)}')
        print(f'Max Winnings On Roll {self.max_win[0]} on roll {self.max_win[1]}')
