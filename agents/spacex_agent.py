import requests
import os
from datetime import datetime

class SpaceXAgent:
    def run(self, _input):
        try:
            # Use environment variable for API URL
            spacex_api = os.getenv("SPACEX_API", "https://api.spacexdata.com/v5/launches/next")
            response = requests.get(spacex_api)
            data = response.json()
            
            # Get launch date and ensure it's in the future
            launch_date = datetime.strptime(data["date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ")
            current_date = datetime.utcnow()
            
            if launch_date < current_date:
                # If the next launch is in the past, fetch upcoming launches
                upcoming_url = "https://api.spacexdata.com/v5/launches/upcoming"
                upcoming_response = requests.get(upcoming_url)
                upcoming_launches = upcoming_response.json()
                
                # Get the first future launch
                for launch in upcoming_launches:
                    launch_date = datetime.strptime(launch["date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ")
                    if launch_date > current_date:
                        data = launch
                        break
            
            # Get launchpad details
            launchpad_id = data.get("launchpad")
            launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
            launchpad_data = requests.get(launchpad_url).json()
            
            # Format launch date
            launch_datetime = datetime.strptime(data["date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ")
            formatted_date = launch_datetime.strftime("%B %d, %Y at %H:%M UTC")
            
            return {
                "launch_name": data["name"],
                "date_utc": data["date_utc"],
                "formatted_date": formatted_date,
                "mission_details": data.get("details", "No mission details available."),
                "rocket": data.get("rocket", "Unknown rocket"),
                "flight_number": data.get("flight_number", "N/A"),
                "launch_data": {
                    "latitude": launchpad_data.get("latitude"),
                    "longitude": launchpad_data.get("longitude"),
                    "location_name": launchpad_data.get("name"),
                    "location_details": launchpad_data.get("details", "No location details available.")
                }
            }
        except Exception as e:
            return {
                "error": f"Failed to fetch SpaceX launch data: {str(e)}",
                "launch_name": "Unknown",
                "date_utc": None,
                "launch_data": {}
            }
