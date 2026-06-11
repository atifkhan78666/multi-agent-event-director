from llm import client


def risk_agent(state):

    prompt = f"""
    You are a Risk Management Expert.

    Event Plan:
    {state['event_plan']}

    Sponsorship Plan:
    {state['sponsorship_plan']}

    Finance Plan:
    {state['finance_plan']}

    Marketing Plan:
    {state['marketing_plan']}

    Find:

    - Financial Risks
    - Operational Risks
    - Low Participation Risks
    - Sponsor Risks

    Suggest solutions.
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
        "risk_report":
        response.choices[0].message.content
    }