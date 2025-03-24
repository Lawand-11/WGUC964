import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import yfinance as yf

# Load the trained model
model = joblib.load("models/best_stock_model.pkl")

# Load stock data
file_path = "data/processed_stock.csv"
apple_data = pd.read_csv(file_path)
apple_data["Date"] = pd.to_datetime(apple_data["Date"])

# Fetch real-time stock data for Apple (AAPL)
stock_symbol = "AAPL"
stock = yf.Ticker(stock_symbol)
latest_stock_data = stock.history(period="1d")

# Extract latest values for default values
latest_close = latest_stock_data["Close"].iloc[-1]
latest_ma_10 = stock.history(period="10d")["Close"].mean()
latest_ma_50 = stock.history(period="50d")["Close"].mean()
latest_volume = latest_stock_data["Volume"].iloc[-1]


if "next_close_prediction" not in st.session_state:
    st.session_state.next_close_prediction = None
if "historical_prediction" not in st.session_state:
    st.session_state.historical_prediction = None


st.markdown(
    """
    <style>
        /* Fixed Top Bar */
        .top-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 60px;
            background-color: #0E1117;
            padding: 15px;
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            color: white;
            z-index: 1000;
            border-bottom: 2px solid #2A2B2E;
        }

        /* Push the content below the fixed bar */
        .block-container {
            padding-top: 80px !important;  /* Adjusts space to prevent overlap */
        }

        /* Hide Streamlit header and footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    <div class="top-bar">📈 Apple Stock Price Predictor</div>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 style='text-align: center;'>📈 Apple Stock Price Predictor</h1>", unsafe_allow_html=True)



st.sidebar.header("Enter Stock Features")

prev_close = st.sidebar.number_input("Previous Close Price", min_value=0.0, format="%.2f", value=latest_close)
ma_10 = st.sidebar.number_input("10-Day Moving Average", min_value=0.0, format="%.2f", value=latest_ma_10)
ma_50 = st.sidebar.number_input("50-Day Moving Average", min_value=0.0, format="%.2f", value=latest_ma_50)
volume = st.sidebar.number_input("Trading Volume", min_value=0, step=1000, value=int(latest_volume))


if st.sidebar.button("Predict Next Close Price"):
    input_data = pd.DataFrame([[prev_close, ma_10, ma_50, volume]], columns=["Prev_Close", "MA_10", "MA_50", "Volume"])
    prediction = model.predict(input_data)[0]
    st.session_state.next_close_prediction = prediction  


if st.session_state.next_close_prediction is not None:
    st.sidebar.success(f"📊 Predicted Closing Price: **${st.session_state.next_close_prediction:.2f}**")


st.subheader("🔍 Historical Prediction Accuracy")
selected_date = st.date_input("Select a past date to test model accuracy", min_value=apple_data["Date"].min(), max_value=apple_data["Date"].max())

if st.button("Test Model on Selected Date"):
    selected_date = pd.to_datetime(selected_date)  # Ensure datetime format

    if selected_date in apple_data["Date"].dt.normalize().values:
        selected_data = apple_data[apple_data["Date"] == selected_date]
        actual_close = selected_data["Close"].values[0]

        
        test_input = selected_data[["Prev_Close", "MA_10", "MA_50", "Volume"]]
        predicted_close = model.predict(test_input)[0]

        
        st.session_state.historical_prediction = {
            "date": selected_date,
            "actual": actual_close,
            "predicted": predicted_close
        }


if st.session_state.historical_prediction is not None:
    pred_data = st.session_state.historical_prediction
    st.write(f"📅 **Date:** {pred_data['date'].strftime('%Y-%m-%d')}")
    st.write(f"✅ **Actual Close Price:** ${pred_data['actual']:.2f}")
    st.write(f"🔮 **Predicted Close Price:** ${pred_data['predicted']:.2f}")

    # Bar Chart: Actual vs. Predicted
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(["Actual Price", "Predicted Price"], [pred_data['actual'], pred_data['predicted']], color=["blue", "red"])
    ax.set_ylabel("Price (USD)")
    ax.set_title(f"Actual vs. Predicted Price for {pred_data['date'].strftime('%Y-%m-%d')}")
    st.pyplot(fig)

    # Pie Chart: Prediction Accuracy
    accuracy = 100 - abs(pred_data['actual'] - pred_data['predicted']) / pred_data['actual'] * 100
    fig_pie, ax_pie = plt.subplots(figsize=(3, 3))
    ax_pie.pie([accuracy, 100 - accuracy], labels=[f"Accuracy: {accuracy:.2f}%", "Error"], colors=["green", "red"], autopct='%1.1f%%', startangle=90)
    ax_pie.set_title("Model Prediction Accuracy")
    st.pyplot(fig_pie)

# Select the last 100 days in data set to compare
st.subheader("📈 Actual vs. Predicted Closing Prices")

apple_data["Predicted"] = model.predict(apple_data[["Prev_Close", "MA_10", "MA_50", "Volume"]])
comparison_data = apple_data.tail(100)

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(comparison_data["Date"], comparison_data["Close"], label="Actual Close Price", color="blue")
ax2.plot(comparison_data["Date"], comparison_data["Predicted"], label="Predicted Close Price", linestyle="dashed", color="red")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price (USD)")
ax2.set_title("Actual vs. Predicted Closing Prices (Last 100 Days)")
ax2.legend()
st.pyplot(fig2)
