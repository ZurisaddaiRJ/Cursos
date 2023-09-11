def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    first_place_racer=racers[0]
    last_place=racers[-1]
    racers[0]=last_place
    racers[-1]=first_place_racer
# Check your answer
#q3.check()