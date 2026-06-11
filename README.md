# AI Event Director

A multi-agent event planning system built using LangGraph and Groq.

## Features

* Event Planning Agent
* Sponsorship Agent
* Finance Agent
* Marketing Agent
* Risk Assessment Agent
* CEO Review Agent
* Final Report Generation

## Workflow

User Input
→ Planner Agent
→ Sponsorship Agent
→ Finance Agent
→ Marketing Agent
→ Risk Agent
→ CEO Agent
→ Final Report

## Tech Stack

* Python
* LangGraph
* Groq API
* Pydantic
* dotenv

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run:

```bash
python main.py
```

## Example Input

Tech Fest

3000 students

Budget 5 lakh

2 days

Hackathon

Gaming Tournament

Startup Pitch Competition

## Future Improvements

* PDF Export
* Email Reports
* Web Dashboard
* Agent Collaboration & Debate
