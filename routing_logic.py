# routing_logic.py

from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.delay_prediction_agent import DelayPredictionAgent
from agents.summary_agent import SummaryAgent

class Router:
    def __init__(self, plan):
        if not plan or not isinstance(plan, list):
            self.plan = ["summary_agent"]
        else:
            self.plan = plan
            
        self.agent_map = {
            "spacex_agent": SpaceXAgent(),
            "weather_agent": WeatherAgent(),
            "delay_prediction_agent": DelayPredictionAgent(),
            "summary_agent": SummaryAgent()
        }

    def execute_plan(self):
        data = {}
        try:
            for agent_name in self.plan:
                agent = self.agent_map.get(agent_name)
                if agent:
                    agent_data = agent.run(data)
                    if isinstance(agent_data, dict):
                        data.update(agent_data)
                    else:
                        print(f"Warning: {agent_name} returned invalid data")
            return data
        except Exception as e:
            print(f"Error in execute_plan: {str(e)}")
            return {"summary": f"An error occurred while processing: {str(e)}"}
