# Import the train_test_split function and uncomment
# from _ import _
from sklearn.model_selection import train_test_split

# fill in and uncomment
# train_X, val_X, train_y, val_y = ____
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

iowa_model = DecisionTreeRegressor()
# Fit model
iowa_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = iowa_model.predict(val_X)

# Check your answer
step_1.check()