from llm import client
from dotenv import load_dotenv
import os

from state import EventState

load_dotenv()

def planner_agent(state: EventState):
    prompt = f"""
    You are an Event Planning Expert.
    Create an event plan for:

    {state['event_details']}

    Include:

    - Theme
    - Major Events
    - Timeline
    - Expected Audience
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "event_plan":
        response.choices[0].message.content
    }