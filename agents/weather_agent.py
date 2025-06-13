import requests
import os
from datetime import datetime, timedelta

class WeatherAgent:
    def run(self, data):
        try:
            launch_data = data.get("launch_data", {})
            latitude = launch_data.get("latitude")
            longitude = launch_data.get("longitude")
            launch_date_str = data.get("date_utc")

            if not all([latitude, longitude, launch_date_str]):
                return {"weather": {
                    "main": {"temp": None},
                    "weather": [{"main": "Unknown", "description": "Missing location or date information"}]
                }}

            api_key = os.getenv("OPENWEATHER_API_KEY")
            if not api_key:
                return {"weather": {
                    "main": {"temp": None},
                    "weather": [{"main": "Error", "description": "Weather API key not found"}]
                }}

            launch_date = datetime.strptime(launch_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            current_date = datetime.utcnow()
            
            # Calculate days difference
            days_difference = (launch_date - current_date).days
            
            if days_difference <= 5:  # Within 5 days - use detailed forecast
                url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
                response = requests.get(url)
                response.raise_for_status()
                forecast_data = response.json()
                
                # Find the closest forecast time to launch
                closest_forecast = None
                smallest_diff = timedelta(days=6)
                
                for forecast in forecast_data.get("list", []):
                    forecast_time = datetime.strptime(forecast["dt_txt"], "%Y-%m-%d %H:%M:%S")
                    time_diff = abs(launch_date - forecast_time)
                    
                    if time_diff < smallest_diff:
                        smallest_diff = time_diff
                        closest_forecast = forecast
                
                if closest_forecast:
                    return {"weather": closest_forecast}
                
                # Fallback if no forecast found
                return {"weather": forecast_data["list"][0] if forecast_data.get("list") else {
                    "main": {"temp": None},
                    "weather": [{"main": "Unknown", "description": "No forecast data available"}]
                }}
                    
            else:  # Beyond 5 days - use climate prediction
                url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
                response = requests.get(url)
                response.raise_for_status()
                forecast_data = response.json()
                
                # Use the last available forecast as an estimate
                if forecast_data.get("list"):
                    return {"weather": forecast_data["list"][-1]}
                
                # Fallback for long-term prediction
                return {"weather": {
                    "main": {"temp": None},
                    "weather": [{
                        "main": "Long-term Forecast",
                        "description": "Extended weather prediction"
                    }]
                }}
                
        except Exception as e:
            # Return a valid weather structure even in case of error
            return {"weather": {
                "main": {"temp": None},
                "weather": [{"main": "Error", "description": f"Weather data unavailable: {str(e)}"}]
            }}
