
**Note:** The `app.py` file references the model at `"Urban-traffic_optimisation\\finalized_model.pkl"`. Ensure the model file is placed correctly relative to where `app.py` is run, or adjust the path in `app.py`.

## Dataset

The primary dataset used is `Urban_traffic_complete.xlsx`. It contains time-series data for multiple intersections, including:

*   Timestamps
*   Intersection details (ID, name, coordinates)
*   Vehicle counts (total, car, bus, truck, motorcycle)
*   Average speed
*   Traffic signal timings (cycle, green, yellow, red)
*   Weather conditions
*   Day of the week, holiday status
*   Special events
*   Pollution levels

The target variable for prediction is `vehicle_count`.

## Methodology

1.  **Data Loading:** Load the dataset from the Excel file using Pandas.
2.  **Data Cleaning:**
    *   Address missing values using appropriate strategies (median for numerical, mode for categorical, interpolation for timestamp, ffill for record ID).
    *   Handle outliers in `average_speed` using the IQR method with capping and flooring.
3.  **Exploratory Data Analysis (EDA):**
    *   Analyze traffic volume and speed patterns across different intersections, times, days, and weather conditions.
    *   Investigate the impact of holidays and special events.
    *   Examine correlations between vehicle count, average speed, and pollution levels.
4.  **Feature Engineering:**
    *   Encode categorical features (`day_of_week`, `weather_condition`) using Label Encoding for model training.
    *   Extract features like `hour` from the timestamp.
    *   Calculate `total_vehicles` and percentage distributions.
5.  **Model Training:**
    *   Select relevant features for prediction.
    *   Split the data into training and testing sets.
    *   Train a `RandomForestRegressor` model to predict `vehicle_count`.
    *   Evaluate the model using MAE, MSE, and RMSE metrics.
6.  **Model Saving:** Serialize the trained model using `pickle` into `finalized_model.pkl`.
7.  **Web Application Development:** Create a Flask application that:
    *   Loads the saved model.
    *   Provides a web form (`index.html`) for user input.
    *   Preprocesses user input (encodes categorical features).
    *   Uses the model to predict `vehicle_count`.
    *   Displays the prediction back to the user.

## Technology Stack

*   **Programming Language:** Python 3
*   **Data Manipulation & Analysis:** Pandas, NumPy
*   **Machine Learning:** Scikit-learn
*   **Web Framework:** Flask
*   **Development Environment:** Jupyter Notebook
*   **Data Visualization:** Matplotlib/Seaborn (within notebook), Power BI
*   **Model Serialization:** Pickle
*   **Data Storage:** Excel (`.xlsx`)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```
2.  **(Recommended)** Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install pandas numpy scikit-learn Flask openpyxl
    ```
    *(Add any other specific libraries used if not covered)*
4.  **Dataset and Model:**
    *   Ensure the `Urban_traffic_complete.xlsx` file is available (you might need to place it in the root directory or update the path in `urban_traffic.ipynb`).
    *   Make sure the `finalized_model.pkl` file is located correctly based on the path specified in `app.py` (e.g., inside a subfolder named `Urban-traffic_optimisation` if running `app.py` from the root, or adjust the path in `app.py`).

## Usage

1.  **Run the Flask Web Application:**
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5000/index` (or the address provided in the terminal).
3.  Fill in the details in the form (Day of Week, Holiday Status, Average Speed, etc.).
4.  Click the "Submit" button.
5.  The predicted congestion level (as vehicle count) will be displayed on the page.

6.  **Explore the Analysis:** Open and run the `urban_traffic.ipynb` notebook in a Jupyter environment to see the detailed data analysis, cleaning, and model training steps.

7.  **View the Dashboard:** Open the `Urban_traffic_dashboard.pbix` file using Microsoft Power BI Desktop to interact with the visualizations.

## Key Findings (Example - based on notebook output)

*   Traffic volume (`vehicle_count`) shows a strong positive correlation with `pollution_level` (approx. 0.96).
*   Traffic volume shows a strong negative correlation with `average_speed` (approx. -0.79).
*   Peak traffic hours appear to be during morning (7-10 AM) and evening (5-8 PM) commutes.
*   Weather conditions significantly impact traffic: Heavy Rain and Fog conditions see considerably lower average vehicle counts and speeds compared to Clear conditions.
*   Holidays generally have lower traffic volume compared to regular weekdays, although specific 'Special Events' can cause significant increases.

## Future Work

*   Deploy the Flask application to a cloud platform (e.g., Heroku, AWS, Azure) for wider accessibility.
*   Integrate real-time data sources if available.
*   Experiment with other regression models (e.g., Gradient Boosting, XGBoost) or time-series models (e.g., ARIMA, LSTM) for potentially better predictions.
*   Expand the feature set (e.g., incorporate distance to city center, public transport availability).
*   Develop more sophisticated optimisation algorithms based on the predictions (e.g., dynamic traffic signal timing adjustments).