def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    loser_team=teams[-1]
    loser_team_captain=loser_team[1]
    return loser_team_captain

# Check your answer
# q2.check()