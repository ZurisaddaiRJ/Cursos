# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again
from sklearn.tree import DecisionTreeRegressor

# Specify the model
iowa_model = DecisionTreeRegressor(random_state = 1)
# Fit model
iowa_model.fit(train_X, train_y)

# Fit iowa_model with the training data.
____
# Check your answer

step_2.check()