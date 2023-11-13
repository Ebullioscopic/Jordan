# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv("C:\Socks\modules\student_extended_ml_dataset2.csv")

# Basic EDA
print("Basic EDA:")
print(data.info()) # Get general info about the dataset
print(data.describe()) # Get summary statistics of numerical columns
print(data.head()) # Display first few rows of the dataset

# Univariate Analysis
print("\nUnivariate Analysis:")
# Histogram for Age
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.show()

# Bivariate Analysis
print("\nBivariate Analysis:")
# Scatter plot between Hours_Studied and Physics_Marks
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Hours_Studied', y='Physics_Marks', data=data)
plt.title('Scatter Plot: Hours Studied vs Physics Marks')
plt.show()

# Multivariate Analysis
print("\nMultivariate Analysis:")
# Pairplot for numerical columns
sns.pairplot(data[['Age', 'Hours_Studied', 'IQ', 'Physics_Marks', 'Math_Marks', 'Chemistry_Marks']])
plt.suptitle('Pairplot of Numerical Variables')
plt.show()

# Correlation Matrix
print("\nCorrelation Matrix:")
correlation_matrix = data.corr()
print(correlation_matrix)

# Linear Regression
print("\nLinear Regression:")

# Prepare data for Linear Regression
X = data[['Age', 'Hours_Studied', 'IQ', 'Math_Marks', 'Chemistry_Marks']]
y = data['Physics_Marks']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualize predictions vs actual values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Physics Marks")
plt.ylabel("Predicted Physics Marks")
plt.title("Actual vs Predicted Physics Marks")
plt.show()
