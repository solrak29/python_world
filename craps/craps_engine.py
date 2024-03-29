import random
import numpy as np
from craps_strategy import CrapsStrategy
from dice_roll import dice_roll

class CrapsEngine:
    '''
    This class will simulate a craps game.
    The Engine will do nothing but provide rolls and state
    '''
    GAME_STATE_OFF = -1

    def __init__(self, num_rolls: int = 1, strategy: CrapsStrategy = ()):
        self.num_rolls = num_rolls
        self.strategy = strategy
        self.game_state = CrapsEngine.GAME_STATE_OFF
        self.dice_roll = dice_roll.dice_factory.create(dice_roll.DiceRoller.Crypt)


    def roll_dice(self):
       #dice1 = random.randint(1, 6)
       #dice1 = np.random.randint(1, 7)
       #dice2 = random.randint(1, 6)
       #dice2 = np.random.randint(1, 7)
       dice1, dice2 = self.dice_roll.roll()
       return dice1 + dice2


    def _call_strat_save(self, method: str, roll_num: int = None, roll: int = None):
        for strat in self.strategy:
            func = getattr(strat, method)
            if method == "save":
                func(roll_num, roll)
            else:
                func()


    def _call_strat(self, method: str, roll: int):
        for strat in self.strategy:
            func = getattr(strat, method)
            func(roll)


    def play(self):
       for rolls in range(1, self.num_rolls + 1):
           print("***Place your bets***")
           #self._call_strat("place_bets")
           roll = self.roll_dice()
           if self.game_state == CrapsEngine.GAME_STATE_OFF: 
               if roll in (7,11,2,3,12):
                   print(f"***craps {roll}***")
                   self._call_strat("craps", roll)
               else:
                   print(f"***point {roll}***")
                   self.game_state = roll
                   self._call_strat("point_made", roll)
           else:
               if roll == 7:
                   print(f"*** {roll} out ***")
                   self.game_state = CrapsEngine.GAME_STATE_OFF
                   self._call_strat("out", roll)
               if roll == self.game_state:
                   print(f"*** winner {roll} ***")
                   self.game_state = CrapsEngine.GAME_STATE_OFF
                   self._call_strat("point", roll)
               else:
                   self._call_strat("roll", roll)
           self._call_strat_save("save", rolls, roll)
       self._call_strat_save("save_to_file")

    
