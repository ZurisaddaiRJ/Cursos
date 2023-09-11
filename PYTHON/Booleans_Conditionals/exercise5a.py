def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    wants_all_toppings = (
    ketchup 
    and ((mustard == True) and onion) 
)
    return wants_all_toppings

# Check your answer
#q5.a.check()