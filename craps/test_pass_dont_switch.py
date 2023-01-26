from pass_dont_pass_switch import PassDontSwitch 

def test_dont_with_odds():
    """
    Starting with 500 bank roll, 5 min bet with 10X odds.
    """
    p5 = PassDontSwitch(500, 5, 10)

    # Lose 3 times to get into the don't mode of betting
    p5.out(7) # 495
    p5.out(7) # 490
    p5.out(7) # 485
    assert p5.dont == True

    # Get our winnings to where we will play the odds.
    p5.craps(3) # 490
    p5.craps(3) # 500
    p5.craps(3)
    p5.craps(3)
    p5.craps(3)
    p5.craps(3)
    p5.craps(3) # 520

    p5.point_made(4)
    #  Odd are 2 to 1 you 20 to play odds with.
    #  Odds calculated should be 20 
    p5.roll(3)  # this is ok since point is made
    p5.roll(5)  # this is ok since point is made
    p5.roll(5)  # this is ok since point is made
    p5.roll(5)  # this is ok since point is made
    assert p5.odds_bet == 20
    p5.out(7)  # this is ok since point is made
    assert p5.end_balance == 535 # 20 + 10
