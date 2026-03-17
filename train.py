import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("salary.csv")

X = data[["Experience"]]
y = data["Salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved")
