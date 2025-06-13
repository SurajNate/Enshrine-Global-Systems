# main.py
import os
from dotenv import load_dotenv
from routing_logic import Router
from agents.planner_agent import PlannerAgent

load_dotenv()

def main(user_goal="Check if the next SpaceX launch will be delayed", return_data=False):
    try:
        if not user_goal:
            raise ValueError("User goal cannot be empty")
            
        print("🧠 User Goal:", user_goal)
        
        planner = PlannerAgent()
        plan = planner.plan(user_goal)
        
        if not plan:
            raise ValueError("No valid plan generated")
            
        print("📌 Agent Plan:", plan)

        router = Router(plan)
        final_data = router.execute_plan()

        if not final_data:
            raise ValueError("No data generated from agents")

        print("\n--- Final Output ---")
        print(final_data.get("summary", "No summary generated."))

        if return_data:
            return final_data

    except Exception as e:
        error_message = f"❌ Error occurred in main(): {str(e)}"
        print(error_message)
        if return_data:
            return {"error": error_message}

if __name__ == "__main__":
    main()
