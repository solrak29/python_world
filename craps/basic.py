import random
from pass_line_strategy import PassLine
from craps_engine import CrapsEngine

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2


def place_pass_line_bet(bet_size):
    roll = roll_dice()
    if roll in (7, 11):
      # Win on 7 or 11
      return "win"
    elif roll in (2, 3, 12):
      # Lose on 2, 3, or 12
      return "loss"
    else:
        # Roll becomes the point number
        point = roll
        while True:
          roll = roll_dice()
          if roll == point:
            # Win on the point
            return "win"
          elif roll == 7:
            # Lose on 7
            return "loss"


def place_come_bet(bet_size):
      roll = roll_dice()
      if roll in (7, 11):
        # Win on 7 or 11
        return "win"
      elif roll in (2, 3, 12):
        # Lose on 2, 3, or 12
        return "loss"
      else:
        # Roll becomes the point number
        point = roll
        while True:
          roll = roll_dice()
          if roll == point:
            # Win on the point
            return "win"
          elif roll == 7:
            # Lose on 7
            return "loss"


if __name__ == "__main__":

    # Set up the simulation
    bankroll = 500
    pass_line_bet = 5
    come_bet = 5
    p = PassLine(bankroll, pass_line_bet)

    craps = CrapsEngine(num_rolls=100, strategy=p)
    craps.play()
    p.show_result()

'''
    # Play 100 rolls
    for roll in range(1, 101):
      # Place a pass line bet
      result = place_pass_line_bet(pass_line_bet)
      if result == "win":
        # Calculate the winnings and add them to the bankroll
        pass_line_odds_multiplier = 2 if point == 4 or point == 10 else 3/2
'''
