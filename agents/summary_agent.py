class SummaryAgent:
    def run(self, input_data):
        try:
            launch_data = input_data.get("launch_data", {})
            location = launch_data.get("location_name", "Unknown location")
            location_details = launch_data.get("location_details", "")
            
            # Basic launch information
            summary = f"Next SpaceX Launch Details:\n\n"
            summary += f"Mission: {input_data.get('launch_name')}\n"
            summary += f"Date: {input_data.get('formatted_date')}\n"
            summary += f"Location: {location}\n"
            summary += f"Flight Number: {input_data.get('flight_number')}\n\n"
            
            # Mission details
            if input_data.get("mission_details"):
                summary += f"Mission Details: {input_data.get('mission_details')}\n\n"
            
            # Weather and delay information
            weather = input_data.get("weather", {})
            if isinstance(weather, dict):
                weather_desc = weather.get("weather", [{}])[0].get("description", "")
                temp = weather.get("main", {}).get("temp")
                if weather_desc and temp:
                    summary += f"Current Weather: {weather_desc.capitalize()} with temperature of {temp}°C\n"
            
            if input_data.get("delay_possible"):
                reasons = ", ".join(input_data.get("delay_reasons", []))
                summary += f"⚠️ Launch may be delayed due to {reasons}.\n"
            else:
                summary += "✅ Weather conditions are favorable for launch. No delays expected.\n"

            return {"summary": summary}
        except Exception as e:
            return {"summary": f"Error generating summary: {str(e)}"}
