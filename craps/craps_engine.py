import random
from craps_strategy import CrapsStrategy

class CrapsEngine:
    '''
    This class will simulate a craps game.
    The Engine will do nothing but provide rolls and state
    '''
    GAME_STATE_OFF = -1

    def __init__(self, num_rolls: int = 1, strategy: CrapsStrategy = None):
        self.num_rolls = num_rolls
        self.strategy = strategy
        self.game_state = CrapsEngine.GAME_STATE_OFF


    def roll_dice(self):
       dice1 = random.randint(1, 6)
       dice2 = random.randint(1, 6)
       return dice1 + dice2


    def play(self):
       for rolls in range(1, self.num_rolls + 1):
           roll = self.roll_dice()
           if self.game_state == CrapsEngine.GAME_STATE_OFF: 
               if roll in (7,11,2,3,12):
                   self.strategy.craps(roll)
               else:
                   self.game_state = roll
                   self.strategy.point_made(roll=roll)
           else:
               if roll == 7:
                   self.game_state = CrapsEngine.GAME_STATE_OFF
                   self.strategy.out(roll)
               if roll == self.game_state:
                   self.game_state = CrapsEngine.GAME_STATE_OFF
                   self.strategy.point(roll)
               else:
                   self.strategy.roll(roll)
