# agents/planner_agent.py

class PlannerAgent:
    def plan(self, user_goal):
        if not user_goal:
            return ["summary_agent"]
            
        goal = user_goal.lower()

        include_spacex = "launch" in goal or "spacex" in goal
        include_delay = "delay" in goal or "postpone" in goal or "cancel" in goal
        include_weather = "weather" in goal or "forecast" in goal or include_delay

        plan = []

        if include_spacex:
            plan.append("spacex_agent")
        if include_weather:
            plan.append("weather_agent")
        if include_delay:
            plan.append("delay_prediction_agent")

        # Always include summary agent at the end
        if "summary_agent" not in plan:
            plan.append("summary_agent")

        # Return default plan if empty
        if not plan:
            return ["spacex_agent", "weather_agent", "delay_prediction_agent", "summary_agent"]

        return plan
