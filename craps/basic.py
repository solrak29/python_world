import random
from pass_line_strategy import PassLine
from pass_line_with_odds import PassLineOdds
from craps_engine import CrapsEngine


if __name__ == "__main__":

    # Set up the simulation
    bankroll = 500
    pass_line_bet = 5
    come_bet = 5
    p = PassLine(bankroll, pass_line_bet)
    p2 = PassLineOdds(bankroll, pass_line_bet, pass_line_bet * 2)
    p3 = PassLineOdds(bankroll, pass_line_bet, pass_line_bet * 10)

    craps = CrapsEngine(num_rolls=1000, strategy=(p, p2, p3))
    craps.play()
    print("--------")
    p.show_result()
    print("--------")
    p2.show_result()
    print("--------")
    p3.show_result()
