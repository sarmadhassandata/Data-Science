# 📈 Time Series Analysis & Forecasting

A structured collection of 9 Jupyter Notebooks covering temporal data manipulation, seasonality decomposition, stationarity testing (ADF/KPSS), classical statistical models (AR / MA / ARIMA / SARIMAX), machine learning feature engineering for time series, and real-world epidemiological timeline analytics using Python.

---

## 📂 Sequenced Project Index

### ⏰ 1. Datetime Preprocessing & Temporal Visualization
- **`01_Time_Series_Data_Manipulation_and_Indexing.ipynb`** — Datetime indexing, resampling frequencies (daily, monthly, quarterly), window rolling, and lag generation.
- **`02_Time_Series_Data_Visualization.ipynb`** — Plotting time-series trajectories, seasonal sub-series plots, autocorrelation (ACF), and partial autocorrelation (PACF) graphics.

---

### 🔬 2. Statistical Analysis, Decomposition & Stationarity
- **`03_Introduction_to_Time_Series_Analysis_and_Forecasting.ipynb`** — Fundamental components of temporal data: trend, seasonality, cyclicality, and residual noise.
- **`04_Statistical_Time_Series_Analysis_and_Stationarity.ipynb`** — Testing stationarity via Augmented Dickey-Fuller (ADF) tests, differencing operations, and variance stabilization.
- **`05_Time_Series_Decomposition_and_Trend_Analysis.ipynb`** — Additive and multiplicative time-series decomposition pipelines using `statsmodels`.

---

### 🎯 3. Classical Statistical Forecasting (ARIMA & SARIMAX)
- **`06_ARIMA_and_SARIMAX_Statistical_Forecasting.ipynb`** — AutoRegressive Integrated Moving Average parameter selection $(p, d, q) \times (P, D, Q)_s$, model diagnostics, and confidence intervals.
- **`07_Time_Series_Forecasting_Methods_and_Validation.ipynb`** — Exponential smoothing (Holt-Winters), rolling window backtesting, and error metrics (RMSE, MAE, MAPE).

---

### 🤖 4. Machine Learning & Real-World Case Studies
- **`08_Machine_Learning_for_Time_Series_Forecasting.ipynb`** — Transforming time-series into supervised learning problems using lag features, rolling statistics, and tree-based ensemble models.
- **`09_Covid19_Epidemiological_Timeline_Analysis_Case_Study.ipynb`** — Real-world timeline tracking, growth rate calculations, and impact curve analytics during the COVID-19 pandemic.

---

## 🛠️ Stack & Libraries
* **Language:** Python 3.x
* **Time Series Modeling:** `statsmodels`, `pmdarima`
* **Data Manipulation:** `Pandas`, `NumPy`
* **Visualization:** `Matplotlib`, `Seaborn`
* **Machine Learning:** `Scikit-Learn`
