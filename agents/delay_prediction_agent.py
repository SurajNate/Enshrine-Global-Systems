class DelayPredictionAgent:
    def run(self, data):
        weather = data.get("weather")
        if not isinstance(weather, dict):
            return {"delay_prediction": "Cannot determine delay – invalid weather data."}

        # Enhanced weather criteria
        wind_speed = weather.get("wind", {}).get("speed", 0)
        condition = weather.get("weather", [{}])[0].get("main", "")
        visibility = weather.get("visibility", 10000)
        rain = weather.get("rain", {}).get("3h", 0)
        
        delay_reasons = []
        
        if wind_speed > 15:
            delay_reasons.append("high winds")
        if any(cond in condition.lower() for cond in ["storm", "rain", "snow", "thunderstorm"]):
            delay_reasons.append("severe weather conditions")
        if visibility < 5000:
            delay_reasons.append("poor visibility")
        if rain > 5:
            delay_reasons.append("heavy precipitation")

        if delay_reasons:
            return {
                "delay_prediction": "Delay likely",
                "delay_possible": True,
                "delay_reasons": delay_reasons
            }
        
        return {
            "delay_prediction": "No delay expected",
            "delay_possible": False,
            "delay_reasons": []
        }
