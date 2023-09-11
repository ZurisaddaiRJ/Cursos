def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    days_meal = None
    for meal in meals:
        if days_meal == meal:
            return True
        days_meal = meal
    
    return False

# Check your answer
#q3.check()