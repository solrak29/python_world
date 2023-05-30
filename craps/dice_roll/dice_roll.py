from abc import ABC
from abc import abstractclassmethod
import os
import sqlite3
import datetime
#import random
#import numpy
#import pandas


class DiceRoller:
    Random = 'Random'
    NumPy = 'NumPy'
    Crypt = 'Crypt'


class DiceRoll(ABC):
    def __init__(self, dice_type: DiceRoller):
        self.type = dice_type
        try:
            file_name = f'./dice_roller_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.db'
            print(file_name)
            self.db_conn = sqlite3.connect(file_name)
            self.db_conn.execute('''CREATE TABLE ROLLS(
                            ID             INT PRIMARY KEY     NOT NULL,
                            DICE_1         INT    NOT NULL,
                            DICE_2         INT     NOT NULL);''')
            self.dice_roll_count = 1
        except sqlite3.OperationalError as e:
            print(f'Failed to initialize dice roll {e} {e.with_traceback(None)}')
            raise


    @abstractclassmethod
    def _roll(self) -> tuple:
        pass

    def roll(self) -> tuple:
        """
        Executes the dice roll and saves the result as well as returning the tuple
        """
        d1, d2 = self._roll()
        self.__save(d1, d2)
        return (d1, d2)

    def __load(self):
        """
        Load dice rols for sqllite db
        """

    def __save(self, d1: int, d2: int):
        """
        Saves the rolls for session.  Each session is saved in sqllite db so it can be extracted
        """
        self.db_conn.execute(f"""insert into ROLLS values ({self.dice_roll_count}, {d1}, {d2})""")
        self.dice_roll_count += 1

    # def stats() -> pandas.dataframe:
    #    pass


class DiceRollCreator():
    """
    Dice Roll object creator 
    
    In general this class to encapsulate dice rolls so we can switch and analyzed
    the rolls for a pariticular session.  This class will allow the "craps engine"
    to utilize different random libs to generate rolls.
    This class shall also keep track of rolls and provide statisctics on such rolls.

    Usage DiceRoll.use_dice(DiceRoller.Random)
    """
    def __init__(self):
        self._rollers = {}

    def _register_roller(self, dice_roller: DiceRoll):
        self._rollers[dice_roller.type]  = dice_roller

    def create(self, dice_roll_type: DiceRoller) -> DiceRoll:
        return self._rollers[dice_roll_type]


class CryptRoller(DiceRoll):

    def __init__(self):
        super().__init__(DiceRoller.Crypt)

    def _roll(self) -> tuple:
        rand_byte_1 = os.urandom(1)[0]
        rand_byte_2 = os.urandom(1)[0]
        return ((rand_byte_1 % 6) + 1, (rand_byte_2 % 6) + 1) 


dice_factory = DiceRollCreator()
dice_factory._register_roller(CryptRoller())
