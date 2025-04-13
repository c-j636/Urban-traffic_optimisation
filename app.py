import pickle
import os
from flask import Flask, render_template, request
import numpy as np

app=Flask(__name__)


filename="Urban-traffic_optimisation\\finalized_model.pkl"
loaded_model = pickle.load(open(filename, 'rb'))

@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Fetch form data
        day_of_week = request.form['day_of_week']
        is_holiday = int(request.form['is_holiday']) if request.form['is_holiday'] else 0
        avg_speed = float(request.form['average_speed'] or 0)
        signal_cycle = float(request.form['signal_cycle_time'] or 0)
        green_time = float(request.form['green_time'] or 0)
        yellow_time = float(request.form['yellow_time'] or 0)
        red_time = float(request.form['red_time'] or 0)
        weather = request.form['weather_condition']
        pollution = float(request.form['pollution_level'] or 0)
        car_count = int(request.form['car_count'] or 0)
        bus_count = int(request.form['bus_count'] or 0)
        truck_count = int(request.form['truck_count'] or 0)
        motorcycle_count = int(request.form['motorcycle_count'] or 0)

        # Preprocessing: Example encodings
        day_map = {
            'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
            'Friday': 4, 'Saturday': 5, 'Sunday': 6
        }
        weather_map = {
            'Clear': 0, 'Light Rain': 1, 'Heatwave': 2,
            'Cold Wave': 3, 'Heavy Rain': 4, 'Fog': 5
        }

        day_encoded = day_map.get(day_of_week, 0)
        weather_encoded = weather_map.get(weather, 0)


        input_features = np.array([[day_encoded, is_holiday, avg_speed, signal_cycle,
                                    green_time, yellow_time, red_time, weather_encoded,
                                    pollution, car_count, bus_count, truck_count,
                                    motorcycle_count]])

        prediction = loaded_model.predict(input_features)[0]


        return render_template("index.html", prediction_text=f"Predicted Congestion Level: {prediction}")
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)