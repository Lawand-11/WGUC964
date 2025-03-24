# 📈 Apple Stock Price Predictor

This project uses historical Apple stock data and machine learning to predict the next day’s closing price. Built with Python and Streamlit, it allows users to:

- Predict the next Apple stock closing price using the latest inputs
- Test the model on historical dates and see prediction accuracy
- View visual comparisons of actual vs. predicted prices
- Understand model performance metrics and algorithm choices

---

## 🚀 Features

- 📊 Predict closing prices with input features (Prev Close, MA10, MA50, Volume)
- 🔎 Historical date testing with visual comparisons and prediction accuracy
- 📉 Actual vs. Predicted closing prices over time (line graph)
- 🧠 Machine learning model (OLS Regression)
- ✅ Persist results across button clicks

---

## 📁 Project Structure

```
.
├── data/
│   ├── apple_stock.csv             # Raw data
│   └── processed_stock.csv         # Cleaned & feature-engineered data
│
├── models/
│   └── best_stock_model.pkl        # Final trained model (OLS Regression)
│
├── main.py                         # Streamlit app
├── train_model.py                  # Script to train and evaluate models
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
```

---

## 🧪 Requirements

- Python 3.10+
- Streamlit
- Pandas
- NumPy
- scikit-learn
- matplotlib
- yfinance

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🖥️ Run the App Locally

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/apple-stock-predictor.git
   cd apple-stock-predictor
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

---

## 🧠 Train Your Own Model

If you want to retrain the model:
```bash
python train_model.py
```
This script compares:
- OLS Regression
- Support Vector Machine
- Random Forest

The best model (based on RMSE and R² score) is saved as `best_stock_model.pkl`.

---

## 📊 Example Visuals

- Line chart: Actual vs. Predicted prices (last 100 days)
- Bar chart: Actual vs. Predicted on selected date
- Pie chart: Model accuracy on selected historical date

---

## 📦 Deployment

You can deploy the app on [Streamlit Cloud](https://streamlit.io/cloud). Just upload the code and dependencies.

---

## 🔐 Disclaimer
This tool is for educational purposes and should not be used for financial decisions.

---


