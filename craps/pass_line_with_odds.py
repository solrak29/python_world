from craps_strategy import CrapsStrategy, validate_balance


'''
Point numbers (4, 5, 6, 8, 9, 10):
True odds: 2:1 for points of 4 and 10; 3:2 for points of 6 and 8; 6:5 for points of 5 and 9
Payouts: typically match the true odds, although some casinos may offer slightly lower payouts

house take on pass line bet is 1.41% because the only pay 1:1 instead of true odds of hitting the 7.
you could say that when you put 100 dollars down, the house already has taken 1.40.

'''
class PassLineOdds(CrapsStrategy):

    def __init__(self, bank_roll: float, base_bet: float, odds_bet: float):
        self.base_bet = base_bet
        self.odds_bet = odds_bet
        self.wins = 0
        self.lost = 0
        super().__init__(bank_roll)


    def _true_odds(self, point: int) -> float:
        if point in (4,10):
            return 2
        if point in (5,9):
            return 1.5
        if point in (6,8):
            return 1.2

    @validate_balance
    def craps(self, roll: int):
        ''' Method when the roll is craps or 7,11 '''
        if roll in (7,11):
            self.wins += 1
            self.end_balance += self.base_bet
            print(f"winner {self.end_balance}")
        else:
            self.lost += 1
            self.end_balance -= self.base_bet
            print(f"loser {self.end_balance}")


    @validate_balance
    def point_made(self, roll: int):
        '''Method when the point is initially made'''
        if self.end_balance < self.odds_bet:
            self.odds_bet = 0
        print(f"point is {roll}")


    def point(self, roll: int):
        '''Method when the a point is rolled after it was made'''
        print(f"roll => {roll}")
        print(f"Balance before {self.end_balance}")
        self.end_balance += self.base_bet
        self.end_balance += (self.odds_bet * self._true_odds(roll))
        print(f"Balance after {self.end_balance}")
        self.wins += 1
        print("winner")


    def roll(self, roll: int):
        ''' Method called when the point is made and roll is not the point'''
        pass

    @validate_balance
    def out(self, roll: int):
        '''Method when you 7 out'''
        self.end_balance -= (self.base_bet + self.odds_bet)
        self.lost += 1
        print(f"loser {self.end_balance}")

    def show_result(self):
        print(f'Winners {self.wins} Losers {self.lost} Final Balance {self.end_balance}')
        print(f'Percentage wins {self.wins/(self.wins+self.lost)}')
        print(f'Percentage lost {self.lost/(self.wins+self.lost)}')
