from pass_dont_pass_switch import PassDontSwitch 


def setup_dont_side_with_30_odds( strat):
    # Lose 3 times to get into the don't mode of betting
    strat.out(7) # 495
    strat.out(7) # 490  # switch to don't here
    strat.out(7) # 495  # you win on the dont here
    assert strat.on_dont == True

    # Get our winnings to where we will play the odds.
    strat.craps(3) # 500
    strat.craps(3) # 505
    strat.craps(3) # 510
    strat.craps(3) # 515
    strat.craps(3) # 520
    strat.craps(3) # 525
    strat.craps(3) # 530
    assert strat.end_balance == 530 # check balance

def test_dont_with_odds_4():
    """
    Starting with 500 bank roll, 5 min bet with 10X odds.
    This strategy will switch from pass to dont if lost in 2 outs.
    This was set to 3 but we changed it to 2.
    """

    # Start off pass line 5 with 500
    p5 = PassDontSwitch(500, 5, 10)
    setup_dont_side_with_30_odds(p5)

    p5.point_made(4)
    assert p5.odds_bet == 30
    p5.roll(3)  # this is ok since point is made
    p5.roll(5)  # this is ok since point is made
    p5.out(7)  # this is ok since point is made
    #  odds are 2 to 1
    #  30/2 = 15
    assert p5.end_balance == 550 # 15 + 5 = 20 = 550


def test_dont_with_odds_5():
    """
    Starting with 500 bank roll, 5 min bet with 10X odds.
    """
    p5 = PassDontSwitch(500, 5, 10)
    setup_dont_side_with_30_odds(p5)

    p5.point_made(5)
    assert p5.odds_bet == 30 
    p5.roll(3)  # this is ok since point is made
    p5.roll(5)  # this is ok since point is made
    p5.out(7)  # this is ok since point is made
    assert p5.end_balance == 555 # 20 + 5 = 25 
