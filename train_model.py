import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load processed stock data
file_path = "data/processed_stock.csv"
apple_data = pd.read_csv(file_path)


X = apple_data[["Prev_Close", "MA_10", "MA_50", "Volume"]]
y = apple_data["Close"].shift(-1)  

# Drop last row since it has no target value
X = X[:-1]
y = y[:-1]

# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)


models = {
    "OLS Regression": LinearRegression(),
    "Support Vector Machine": SVR(kernel="rbf"),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}


performance_results = {}


for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)

    performance_results[name] = {"R² Score": r2, "RMSE": rmse, "MAE": mae}

    print(f"{name} Performance:")
    print(f"  R² Score: {r2:.4f}")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  MAE: {mae:.4f}\n")

# Select the best model (lowest RMSE)
best_model_name = min(performance_results, key=lambda k: performance_results[k]["RMSE"])
best_model = models[best_model_name]

# Save the best model
joblib.dump(best_model, "models/best_stock_model.pkl")
print(f"Best Model: {best_model_name} saved as 'best_stock_model.pkl'")
