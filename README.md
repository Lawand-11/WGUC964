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
│   ├── apple_stock.csv             # Raw data (sourced from Kaggle)
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

## 🧭 User Guide

There are two ways to access and use the Apple Stock Price Predictor:

### ✅ Option 1: Use the Deployed Streamlit Dashboard
No setup required. Simply open the hosted application in your browser:

🔗 **[Streamlit App Link](https://wguc964-mmcyvzxbtvyujgjeutbxmx.streamlit.app/)** 

---

### 💻 Option 2: Run the Application Locally

#### Requirements
- Python 3.10+
- Git (if cloning from GitLab)
- Internet connection (for real-time data via yfinance)

#### Installation Steps

1. **Clone the repository:**
```bash
git clone https://gitlab.com/your-username/apple-stock-predictor.git
cd apple-stock-predictor
```

2. **Create and activate a virtual environment (recommended):**
```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
source .venv/bin/activate    # macOS/Linux
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app:**
```bash
streamlit run main.py
```

---

## 🧠 Train Your Own Model (Optional)

To retrain the model using the dataset:
```bash
python train_model.py
```
This will evaluate:
- OLS Regression
- Support Vector Machine (SVM)
- Random Forest

The best model is saved automatically as `models/best_stock_model.pkl`.

---

## 📊 Example Visuals

- Line chart: Actual vs. Predicted prices (last 100 days)
- Bar chart: Actual vs. Predicted on selected date
- Pie chart: Model accuracy on selected historical date

---

## 🔐 Disclaimer
This tool is for educational purposes and should not be used for financial decisions.

---

