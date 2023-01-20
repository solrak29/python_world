from pass_line_strategy import PassLine
from pass_line_with_odds import PassLineOdds
from pass_line_odds_on import PassLineOddsOn
from craps_engine import CrapsEngine


if __name__ == "__main__":

    # Set up the simulation
    bankroll = 500
    pass_line_bet = 5
    come_bet = 5
    num_rolls = 1000
    p = PassLine(bankroll, pass_line_bet)
    p2 = PassLineOdds(bankroll, pass_line_bet, pass_line_bet * 2)
    p3 = PassLineOdds(bankroll, pass_line_bet, pass_line_bet * 10)
    p4 = PassLineOddsOn(bankroll, pass_line_bet, 10)

    #  A single session would be at the most 100 rolls of the dice.
    #  You can go higher, but maybe break this up into multiple games
    craps = CrapsEngine(num_rolls=num_rolls, strategy=(p, p2, p3, p4))
    craps.play()
    print("--------")
    print(f"Bank Roll Start {bankroll}")
    print(f"Min bet {pass_line_bet}")
    print(f"Num Rolls {num_rolls}")
    print("--------")
    print("Pass Line Only")
    print("--------")
    p.show_result()
    print("--------")
    print("Pass Line Odds x 2")
    print("--------")
    p2.show_result()
    print("--------")
    print("Pass Line Odds x 10")
    print("--------")
    p3.show_result()
    print("--------")
    print("Pass Line Odds On Winnings only up 10X")
    print("--------")
    p4.show_result()
