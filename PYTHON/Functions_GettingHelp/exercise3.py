def to_smash(total_candies, number_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    >>>to_smash(900,number_friends=8)
    0
    """
    return total_candies % number_friends

# Check your answer