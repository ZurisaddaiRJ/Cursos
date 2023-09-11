def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    ordered_list=arrivals.index(name)
    return ordered_list>=len(arrivals)/2 and ordered_list != len (arrivals)-1

# Check your answer
#q5.check()