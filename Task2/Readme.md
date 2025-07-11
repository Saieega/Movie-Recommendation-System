# 📈 INFY Stock Price Prediction Using Machine Learning and LSTM

**Author**: Saikumar Eega\
**Project**: Task 2 — Stock Price Prediction\
**Platform**: Google Colab

---

## 🧠 Objective

Predict the **closing price** of INFY (Infosys Limited) stock using:

- Linear Regression
- Random Forest
- LSTM (Long Short-Term Memory)

The goal is to compare traditional machine learning with deep learning for stock market forecasting using historical data.

---

## 📦 Libraries Used

- pandas, numpy
- matplotlib
- scikit-learn (`MinMaxScaler`, `LinearRegression`, `RandomForestRegressor`)
- yfinance (for downloading stock data)
- TensorFlow (for LSTM model)

---

## 📅 Data Source

Data is pulled from **Yahoo Finance** using the `yfinance` library:

```python
data = yf.download('INFY.NS', start='2015-01-01', end='2024-01-01')
```

---

## 🔄 Data Preprocessing

- Only the `Close` price is used.
- Data is scaled using `MinMaxScaler` (range [0, 1]).
- A sliding window of 10 days is used to predict the 11th day's closing price.

---

## 🔍 Models Used

### 🔹 1. Linear Regression

- Simple baseline model
- RMSE is calculated for evaluation

### 🔹 2. Random Forest

- Ensemble-based regression model
- Trained with 100 estimators
- Compared with Linear Regression using RMSE

### 🔹 3. LSTM (Deep Learning)

- Input reshaped to `(samples, timesteps, features)`
- 1 LSTM layer with 50 units and 1 Dense output layer
- Trained for 20 epochs
- Loss used: Mean Squared Error

---

## 📊 Evaluation Metrics

- **RMSE** (Root Mean Squared Error)
- **MSE** (Mean Squared Error Loss)
- All predictions and actual values are **inverse-transformed** to real INR prices before evaluation.

---

## 📈 Results & Visualization

- Plots show actual vs predicted prices for all three models.
- Linear Regression closely follows the actual prices.
- Random Forest shows more deviation.
- LSTM performs competitively with better trend-following.

---

## 📌 Conclusion

- **Linear Regression** outperforms Random Forest in this case.
- **LSTM** performs well and captures the trend effectively.
- Deep learning can be powerful, but preprocessing and tuning are crucial.

---

## 📁 File Structure

```
Stock price prediction.py   # Full code (Python, Colab-compatible)
README.md                   # This file
```

---

## 🙌 Author

**Saikumar Eega**\
Chaitanya Bharathi Institute of Technology\
Passionate about Data Science, AI, and Software Development.

---

## 🧠 Future Work

- Add hyperparameter tuning (GridSearchCV for RF)
- Try other models like SVR or XGBoost
- Experiment with longer look-back windows
- Deploy the best model using Streamlit or Flask

