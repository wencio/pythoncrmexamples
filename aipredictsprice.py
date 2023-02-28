import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
df = pd.read_csv('real_estate_data.csv')

# Explore the data
print(df.head())

# Feature engineering
df['age_years'] = df['age'] / 12

# Split the data into train and test sets
X = df[['house_size', 'age_years', 'num_rooms']].values
y = df['price'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('MSE:', mse)
print('R2:', r2)

# Predict the price of a new property
new_house = np.array([1500, 5, 3])
new_house = new_house.reshape(1, -1)
new_price = model.predict(new_house)[0]
print('Predicted price:', new_price)
