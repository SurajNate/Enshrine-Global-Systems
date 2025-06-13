# 🚀 Multi-Agent AI System using Google ADK

This project implements a **multi-agent orchestration system** using the **Google Agent Developer Kit (ADK)**. It processes a user goal and routes it through intelligent agents such as SpaceX launch fetcher, weather predictor, delay estimator, and summarizer — all autonomously planned and executed.

## 🎯 Use Case

> **User Goal**: _"Check if the next SpaceX launch will be delayed"_

### 👇 The system performs:
1. **Launch Info Retrieval** (from SpaceX API)
   - Fetches next launch details
   - Gets launch site coordinates
   - Handles future launch scheduling
2. **Weather Forecast** (via OpenWeatherMap)
   - Retrieves weather data for launch location
   - Provides detailed forecast for launches within 5 days
   - Offers climate predictions for future launches
3. **Delay Prediction** (based on weather)
   - Analyzes weather conditions
   - Evaluates multiple factors (wind, visibility, precipitation)
   - Provides delay probability
4. **Summarization** (final user-readable output)
   - Combines all data into readable format
   - Highlights key information
   - Provides clear delay predictions

## 🛠️ Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Unix/MacOS
   ```

---

## 🧠 Architecture

```text
User Goal
   │
   ▼
Planner Agent ──> [Agent Plan]
   │
   ▼
Router executes each agent sequentially:
    ├─ SpaceXAgent
    ├─ WeatherAgent
    ├─ DelayPredictionAgent
    └─ SummaryAgent

#📁 Project Structure

multi_agent_adk_project/
├── agents/
│   ├── planner_agent.py              # Determines which agents to call
│   ├── spacex_agent.py               # Fetches next SpaceX launch
│   ├── weather_agent.py              # Gets weather data
│   ├── delay_prediction_agent.py     # Predicts delay based on weather
│   └── summary_agent.py              # Final summary response
├── evaluations/
│   └── eval1.json                    # Evaluation criteria
├── .env                              # Environment variables
├── evaluate.py                       # Evaluation script
├── main.py                           # Main execution entrypoint
├── routing_logic.py                  # Handles plan routing
├── requirements.txt                  # Project dependencies
└── README.md                         # Documentation