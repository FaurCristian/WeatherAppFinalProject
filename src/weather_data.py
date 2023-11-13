from geopy.geocoders import Photon
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz


class WeatherData:
    def __init__(self):
        print("Initializing WeatherData...")
        self.long_lat = None
        self.timezone = None
        print("WeatherData initialization complete.")

    def get_weather(self, city):
        print(f"Getting weather data for city: {city}...")
        geolocator = Photon(user_agent="measurements")
        location = geolocator.geocode(city)
        self.obj = TimezoneFinder()
        result = self.obj.timezone_at(lng=location.longitude, lat=location.latitude)
        self.timezone = result
        self.long_lat = f"Latitude: {round(location.latitude, 4)} / Longitude: {round(location.longitude, 4)}"
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        print("Weather data retrieval complete.")
        return current_time, self.timezone, self.long_lat
