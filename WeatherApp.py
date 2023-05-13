import tkinter as tk
import requests
from PIL import ImageTk, Image

# OpenWeatherMap API endpoint and API key
weather_url = "https://api.openweathermap.org/data/2.5/weather"
geocoding_url = "https://api.openweathermap.org/geo/1.0/direct"
api_key = "9b78ace9af1be05aa689e8268dd9a445"

# Define a function to get the weather data for the given city name
def get_weather(city_name):
    # Build the query string parameters
    query_params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    # Make the API request and get the response
    response = requests.get(weather_url, params=query_params)
    # Parse the response JSON data
    data = response.json()
    print(data)
    # Extract the relevant weather data
    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
    # Return the weather data
    return weather

# Define a function to update the weather display
def update_weather_display():
    # Get the city name from the user input
    city_name = city_entry.get()
    # Get the weather data for the city
    weather = get_weather(city_name)
    # Update the weather display labels
    city_label.config(text=weather["city"])
    temperature_label.config(text=str(weather["temperature"]) + " °C")
    description_label.config(text=weather["description"])

# Create the main window
window = tk.Tk()
window.geometry('400x400')
window['background'] = '#49B8E7'
window.title("Weather App")

# Create the input frame and widgets
input_frame = tk.Frame(window)
input_frame.configure(background='#49B8E7')
input_frame.pack(side=tk.TOP, pady=10)

city_label = tk.Label(input_frame, text="City:")
city_label.configure(background='#49B8E7')
city_label.pack(side=tk.TOP)

city_entry = tk.Entry(input_frame, width=20)
city_entry.configure(background='#88DCFF')
city_entry.pack(side=tk.TOP)

get_weather_button = tk.Button(input_frame, text="Get Weather", command=update_weather_display)
get_weather_button.configure(background='#88DCFF')
get_weather_button.pack(side=tk.TOP, pady=10)

# Create the weather display frame and labels
weather_frame = tk.Frame(window)
weather_frame.configure(background='#49B8E7')
weather_frame.pack(side=tk.TOP, pady=10)

city_label = tk.Label(weather_frame, text="", font=("Frutiger", 16))
city_label.configure(background='#49B8E7')
city_label.pack(side=tk.TOP)

temperature_label = tk.Label(weather_frame, text="", font=("Frutiger", 24, "bold"))
temperature_label.configure(background='#49B8E7')
temperature_label.pack(side=tk.TOP)

description_label = tk.Label(weather_frame, text="", font=("Frutiger", 16))
description_label.configure(background='#49B8E7')
description_label.pack(side=tk.TOP)

icon_label = tk.Label(weather_frame, text="", font=("Frutiger", 16))
icon_label.configure(background='#49B8E7')
icon_label.pack(side=tk.TOP)


# Start the main event loop
window.mainloop()
