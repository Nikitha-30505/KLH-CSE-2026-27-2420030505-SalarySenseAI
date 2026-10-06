import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv("dataset/salary_data.csv")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("=" * 60)
print("MISSING VALUES")
print("=" * 60)
print(df.isnull().sum())

# Categorical columns
categorical_columns = [
    "Gender",
    "Education_Level",
    "Job_Title",
    "Industry",
    "Location",
    "Company_Size"
]

# Create separate encoder for each column
encoders = {}

for column in categorical_columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    encoders[column] = encoder

print("\nEncoding Completed Successfully!")

# Features and target
X = df.drop("Salary", axis=1)
y = df["Salary"]

print("\n" + "=" * 60)
print("FEATURES")
print("=" * 60)
print(X.head())

print("\n" + "=" * 60)
print("TARGET")
print("=" * 60)
print(y.head())

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data :", X_train.shape)
print("Testing Data :", X_test.shape)

# Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

print("\nLinear Regression Model Trained Successfully!")

# Prediction
y_pred = model.predict(X_test)

print("\nFirst 10 Predictions")
print(y_pred[:10])

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print("Mean Absolute Error (MAE):", round(mae, 2))
print("Root Mean Squared Error (RMSE):", round(rmse, 2))
print("R2 Score:", round(r2, 4))

# Save model and encoders
model_data = {
    "model": model,
    "encoders": encoders,
    "features": list(X.columns)
}

joblib.dump(model_data, "models/best_model.pkl")

print("\nModel saved successfully!")
print("Location: models/best_model.pkl")