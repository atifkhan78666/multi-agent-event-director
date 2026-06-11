from llm import client
from state import EventState
import state
import state


def report_agent(state: EventState):

    prompt = f"""
        Create a professional event proposal.

        Event Plan:
        {state['event_plan']}

        Sponsorship Plan:
        {state['sponsorship_plan']}

        Finance Plan:
        {state['finance_plan']}

        Marketing Plan:
        {state['marketing_plan']}

        Risk Report:
        {state['risk_report']}

        CEO Decision:
        {state['ceo_decision']}

        Generate:

        1. Executive Summary
        2. Event Plan
        3. Sponsorship Strategy
        4. Finance Plan
        5. Marketing Plan
        6. Risk Analysis
        7. CEO Decision
        8. Final Recommendation
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
        "final_report":
        response.choices[0].message.content
    }