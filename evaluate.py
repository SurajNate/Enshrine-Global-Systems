import json
from main import main
from agents.planner_agent import PlannerAgent

def evaluate(file_path):
    with open(file_path, "r") as f:
        eval_data = json.load(f)

    user_goal = eval_data["user_goal"]
    expected_agents = eval_data["expected_agents"]
    expected_keys = eval_data["expected_keys"]

    planner = PlannerAgent()
    plan = planner.plan(user_goal)

    print("✅ Checking Planner Routing...")
    print("Expected:", expected_agents)
    print("Actual  :", plan)
    assert plan == expected_agents, "Planner failed to generate correct agent sequence."

    print("\n🔁 Running system...")
    result = main(user_goal, return_data=True)

    print("\n✅ Checking Output Keys...")
    for key in expected_keys:
        assert key in result, f"Missing key in output: {key}"

    print("\n🎉 Evaluation Passed!")

if __name__ == "__main__":
    evaluate("evaluations/eval1.json")
