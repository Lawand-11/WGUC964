import pandas as pd

def load_and_preprocess(file_path):
    """Loads and preprocesses the Apple stock dataset."""
    
    # Load CSV file
    apple_data = pd.read_csv(file_path)

    # Convert Date column to datetime format
    apple_data["Date"] = pd.to_datetime(apple_data["Date"])
    apple_data = apple_data.sort_values(by="Date")

    if "Adj Close" in apple_data.columns:
        apple_data.drop(columns=["Adj Close"], inplace=True)

    
    apple_data["Prev_Close"] = apple_data["Close"].shift(1)
    apple_data["MA_10"] = apple_data["Close"].rolling(window=10).mean()
    apple_data["MA_50"] = apple_data["Close"].rolling(window=50).mean()

    # Drop NaN values caused by rolling averages
    apple_data.dropna(inplace=True)

    return apple_data

if __name__ == "__main__":
    file_path = "data/apple_stock.csv" 
    processed_data = load_and_preprocess(file_path)
    
    # Save the cleaned dataset
    processed_data.to_csv("data/processed_stock.csv", index=False)
    print("Preprocessing complete. File saved as 'processed_stock.csv'")
