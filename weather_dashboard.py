import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Your API key here
API_KEY = "b1c185f372d70d013ea5ce4e96b3d7ae"

# List of cities to fetch data for
cities = ["London", "New York", "Delhi", "Tokyo", "Paris"]

# Base URL for API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Lists to store data
temperatures = []
humidities = []
wind_speeds = []

# Fetch weather data
for city in cities:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        temperatures.append(data["main"]["temp"])
        humidities.append(data["main"]["humidity"])
        wind_speeds.append(data["wind"]["speed"])
    else:
        print(f"Failed to get data for {city}")
        temperatures.append(None)
        humidities.append(None)
        wind_speeds.append(None)

# Visualization
sns.set(style="whitegrid")

plt.figure(figsize=(15, 5))

# Temperature
plt.subplot(1, 3, 1)
sns.barplot(x=cities, y=temperatures, palette="coolwarm")
plt.title("Temperature (°C)")
plt.ylabel("Temp (°C)")

# Humidity
plt.subplot(1, 3, 2)
sns.barplot(x=cities, y=humidities, palette="Blues")
plt.title("Humidity (%)")
plt.ylabel("Humidity (%)")

# Wind Speed
plt.subplot(1, 3, 3)
sns.barplot(x=cities, y=wind_speeds, palette="Greens")
plt.title("Wind Speed (m/s)")
plt.ylabel("Wind Speed (m/s)")

plt.suptitle("Weather Dashboard - Current Data", fontsize=16)
plt.tight_layout()
plt.show()
