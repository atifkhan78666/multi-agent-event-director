from llm import client
from state import EventState


def sponsorship_agent(state: EventState):

    prompt = f"""
    You are a Sponsorship Expert.

    Event Plan:

    {state['event_plan']}

    Generate:

    - Sponsor categories
    - Sponsorship packages
    - Expected revenue
    - Outreach strategy
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
        "sponsorship_plan":
        response.choices[0].message.content
    }