def to_smash(total_candy):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candy evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candy, "candy")
    return total_candy % 3

to_smash(91)
to_smash(1)