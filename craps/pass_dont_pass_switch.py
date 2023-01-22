from craps_strategy import CrapsStrategy, validate_balance


'''
Point numbers (4, 5, 6, 8, 9, 10):
True odds: 2:1 for points of 4 and 10; 3:2 for points of 6 and 8; 6:5 for points of 5 and 9
Payouts: typically match the true odds, although some casinos may offer slightly lower payouts

house take on pass line bet is 1.41% because the only pay 1:1 instead of true odds of hitting the 7.
you could say that when you put 100 dollars down, the house already has taken 1.40.

'''
class PassDontSwitch(CrapsStrategy):
    '''
        This strategy will switch from pass to don't pass but still use winnings for odds
        This includes come out rolls
        TODO: need to fix so proper odds are placed
        TODO: maybe compensate for winners not just losers for when we switch
        
    '''

    def __init__(self, bank_roll: float, base_bet: float, max_odds_multiplier: float):
        self.base_bet = base_bet
        self.odds_bet = 0
        self.orig_bank_roll = bank_roll
        self.max_odds = max_odds_multiplier
        self.dont = False
        self.lost_limit = 3  # number of times we can lose before switch
        self._point = 0  # need to store point since on the dont we don't know what the point was
        super().__init__(bank_roll)


    def _true_odds(self, point: int) -> float:
        if point in (4,10):
            return 2
        if point in (5,9):
            return 1.5
        if point in (6,8):
            return 1.2


    def check_lost_limit(self):
        self.lost_limit -= 1
        if self.lost_limit == 0:
            self.dont = True if self.dont == False else True 
            self.lost_limit = 3
            print (f"Switching dont {self.dont}")


    @validate_balance
    def craps(self, roll: int):
        ''' Method when the roll is craps or 7,11 '''
        if roll in (7,11):
            if self.dont:
                self.end_balance -= self.base_bet
                self.lost += 1
                self.check_lost_limit()
            else:
                self.win(self.base_bet)
        else:
            if self.dont:
                if roll != 12:
                    self.win(self.base_bet)
            else:
                self.lost += 1
                self.end_balance -= self.base_bet
                self.check_lost_limit()
        print(f"PassLineOdds ( {self.odds_bet} ) => {self.end_balance}")


    @validate_balance
    def point_made(self, roll: int):
        '''Method when the point is initially made'''
        ''' TODO Need to check proper odds as the dont side you have put extra'''
        self._point = roll
        if self.end_balance < self.odds_bet:
            self.odds_bet = 0
        winnings = self.end_balance - self.orig_bank_roll
        if winnings > self.base_bet:
            odds_play = int(winnings/self.base_bet)
            if odds_play > self.max_odds:
                odds_play = self.max_odds
            self.odds_bet = odds_play * self.base_bet
        else:
            self.odds_bet = 0
        print(f"PassDont Switch Placing odds {self.odds_bet}")


    @validate_balance
    def point(self, roll: int):
        '''Method when the a point is rolled after it was made'''
        if self.dont:
            self.end_balance -= (self.base_bet + self.odds_bet)
            self.lost += 1
            self.check_lost_limit()
        else:
            self.win(self.base_bet + ( self.odds_bet * self._true_odds(roll)))
        print(f"PassLineOdds ( {self.odds_bet} ) => {self.end_balance}")


    @validate_balance
    def roll(self, roll: int):
        ''' Method called when the point is made and roll is not the point'''
        pass

    @validate_balance
    def out(self, roll: int):
        '''Method when you 7 out'''
        if self.dont:
            print(f'point craps {self._point}')
            print(f'{self.base_bet} {self.odds_bet} {self._true_odds(self._point)}')
            self.win(self.base_bet + ( self.odds_bet * self._true_odds(self._point)))
            self._point = 0
        else:
            self.end_balance -= (self.base_bet + self.odds_bet)
            self.lost += 1
            self.check_lost_limit()
        print(f"PassDontSwitch ( {self.odds_bet} ) => {self.end_balance}")

    def show_result(self):
        print(f'Winners {self.wins} Losers {self.lost} Final Balance {self.end_balance}')
        print(f'Percentage wins {self.wins/(self.wins+self.lost)}')
        print(f'Percentage lost {self.lost/(self.wins+self.lost)}')
        print(f'Max Winnings On Roll {self.max_win[0]} on roll {self.max_win[1]}')
