from craps_strategy import CrapsStrategy, validate_balance


'''
Point numbers (4, 5, 6, 8, 9, 10):
True odds: 2:1 for points of 4 and 10; 3:2 for points of 6 and 8; 6:5 for points of 5 and 9
Payouts: typically match the true odds, although some casinos may offer slightly lower payouts

house take on pass line bet is 1.41% because the only pay 1:1 instead of true odds of hitting the 7.
you could say that when you put 100 dollars down, the house already has taken 1.40.

when you lay the odds you have to pay multiples (even taking the odds)

TODO: we need to code to provide proper odds and pay out for put bets.
so 6,8 your adds are 6:5 for every mulitiple of 5 you win 6.  for lay you have to put mutliple of 6 to get 5
for 9,5 your odds are 3:2 for every multiple of 2 you get 3.  you must lay a mutliple of 3 to get 2.
for 10,4, your odds are 2:1 for every mutlipl of 1 you get 2.  you must lay a mutliple of 2 to get 1

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
        self.on_dont = False
        self.lost_limit = 2  # number of times we can lose before switch
        self._point = 0  # need to store point since on the dont we don't know what the point was
        super().__init__(bank_roll)


    def _true_odds(self, point: int) -> float:
        if point in (4,10):
            if self.on_dont:
                return 0.5
            return 2
        if point in (5,9):
            if self.on_dont:
                return 0.6667
            return 1.5
        if point in (6,8):
            if self.on_dont:
                return 0.83
            return 1.2
        return 0.0


    def check_lost_limit(self):
        self.lost_limit -= 1
        if self.lost_limit == 0:
            self.on_dont = True if self.on_dont == False else True 
            self.lost_limit = 3
            print (f"Switching dont {self.on_dont}")


    @validate_balance
    def craps(self, roll: int):
        ''' Method when the roll is craps or 7,11 '''
        if roll in (7,11):
            if self.on_dont:
                self.end_balance -= self.base_bet
                self.lost += 1
                self.check_lost_limit()
            else:
                self.win(self.base_bet)
        else:
            if self.on_dont:
                if roll != 12:
                    self.win(self.base_bet)
            else:
                self.lost += 1
                self.end_balance -= self.base_bet
                self.check_lost_limit()
        print(f"{__name__} : PassLineOdds ( {self.odds_bet} ) => {self.end_balance}")


    def bet_on_pass_side(self, roll: int):
        '''Method when the point is initially made'''
        winnings = self.end_balance - self.orig_bank_roll
        if winnings > self.base_bet:
            odds_play = int(winnings/self.base_bet)
            if odds_play > self.max_odds:
                odds_play = self.max_odds
            self.odds_bet = odds_play * self.base_bet
        else:
            self.odds_bet = 0
        print(f"{__name__}: Placing odds {self.odds_bet}")


    def bet_on_dont_side(self, roll: int):
        multiple = 0
        winnings = self.end_balance - self.orig_bank_roll
        if winnings > self.base_bet:
            if self._point in ( 6,8 ):
                multiple = 6
            elif self._point in (5,9):
                multiple = 3
            elif self._point in (4,10):
                multiple = 2
            count = 1
            base_play = 0
            while base_play < winnings:
                prev_base = base_play
                base_play = multiple * count
                if base_play > winnings:
                    base_play = prev_base
                    break
                count += 1
            odds_play = int(base_play/self.base_bet)
            if odds_play <= self.max_odds:
                self.odds_bet = base_play
            else:
                self.odds_bet = self.max_odds * self.base_bet
        else:
            self.odds_bet = 0
        print(f"{__name__}: PassDont Switch Placing odds {self.odds_bet}")


    @validate_balance
    def point_made(self, roll: int):
        """
        Playing odds on dont is different
        6 and 8 you need multiples of 6 to win multiples of 5 (i.e. 6:5)
        for 5,9 you need multiples of 3 to win multiples of 2 (i.e. 3:2)
        for 4, 10,  you need multiples of 2 to win 1 (i.e. 2:1)
        """
        #  places the odds if we have enough
        self._point = roll
        if self.end_balance < self.odds_bet:
            self.odds_bet = 0
            print('Not enough to play odds')
        else:
            self.bet_on_dont_side(roll) if self.on_dont else self.bet_on_pass_side(roll)


    @validate_balance
    def point(self, roll: int):
        '''Method when the a point is rolled after it was made'''
        if self.on_dont:
            self.end_balance -= (self.base_bet + self.odds_bet)
            self.lost += 1
            self.check_lost_limit()
        else:
            self.win(self.base_bet + ( self.odds_bet * self._true_odds(roll)))
        print(f"{__name__}: PassLineOdds ( {self.odds_bet} ) => {self.end_balance}")


    @validate_balance
    def roll(self, roll: int):
        ''' Method called when the point is made and roll is not the point'''
        pass

    @validate_balance
    def out(self, roll: int):
        '''Method when you 7 out'''
        if self.on_dont:
            print(f'{__name__}: point craps {self._point}')
            print(f'{__name__}: {self.base_bet} {self.odds_bet} {self._true_odds(self._point)}')
            self.win(self.base_bet + ( self.odds_bet * self._true_odds(self._point)) + self.odds_bet)
            self._point = 0
        else:
            self.end_balance -= (self.base_bet + self.odds_bet)
            self.lost += 1
            self.check_lost_limit()
        print(f"{__name__}: PassDontSwitch ( {self.odds_bet} ) => {self.end_balance}")

    def show_result(self):
        print(f'{__name__}: Winners {self.wins} Losers {self.lost} Final Balance {self.end_balance}')
        print(f'{__name__}: Percentage wins {self.wins/(self.wins+self.lost)}')
        print(f'{__name__}: Percentage lost {self.lost/(self.wins+self.lost)}')
        print(f'{__name__}: Max Winnings On Roll {self.max_win[0]} on roll {self.max_win[1]}')
