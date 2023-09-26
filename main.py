import requests
import pandas as pd
import numpy as np

def get_weather_forecast(api_key: str, location: str) -> dict:
    """
    Returns a dictionary containing the weather forecast for the specified location.
    """
    # Construct the API request URL
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={api_key}"
    
    # Send the API request
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()

    # Extract and return the weather forecast
    return data

# Replace 'YOUR_API_KEY' with your actual Visual Crossing Weather API key
api_key = "2ZMGNAT7CGAMAV9LKDMLUM2ZZ"

# Replace 'LOCATION' with the desired location (e.g., 'London,UK')
location = input("Enter a location: ")

# Call the get_weather_forecast function with the provided API key and location
data = get_weather_forecast(api_key, location)

# Convert the weather forecast data to a pandas DataFrame
df = pd.DataFrame(data["days"])

# Analyze the data using pandas and numpy
average_temp_max = np.mean(df["tempmax"])
average_temp_min = np.mean(df["tempmin"])
max_temp = np.max(df["tempmax"])
min_temp = np.min(df["tempmin"])

print("Weather forecast Analysis:")
print("=================")
print(f"Average maximum temperature: {average_temp_max:.2f}°C")
print(f"Average minimum temperature: {average_temp_min:.2f}°C")
print(f"Maximum temperature: {max_temp:.2f}°C")
print(f"Minimum temperature: {min_temp:.2f}°C")
