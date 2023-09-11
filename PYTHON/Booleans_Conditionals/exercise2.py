def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies ==1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(1)
to_smash(91)