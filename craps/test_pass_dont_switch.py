from pass_dont_pass_switch import PassDontSwitch 

def test_dont_with_odds():
    p5 = PassDontSwitch(500, 5, 10)
    p5.out(7)
    p5.out(7)
    p5.out(7)
    assert p5.dont == True
    p5.craps(3)
    p5.craps(3)
    p5.craps(3)
    p5.craps(3)
    p5.craps(3)
    p5.craps(3)
    p5.craps(3)
    #  Should lay 20 odds with 5 dollar bet and 4 wins
    p5.point_made(4)
    p5.roll(3)  # this is ok since point is made
    p5.roll(5)  # this is ok since point is made
    p5.roll(5)  # this is ok since point is made
    p5.roll(5)  # this is ok since point is made
    assert p5.odds_bet == 20
    p5.out(7)  # this is ok since point is made
    assert p5.end_balance == 565


