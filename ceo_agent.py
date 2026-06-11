from llm import client


def ceo_agent(state):

    prompt = f"""
    You are the CEO.

    Review:

    Event Plan:
    {state['event_plan']}

    Sponsorship:
    {state['sponsorship_plan']}

    Finance:
    {state['finance_plan']}

    Marketing:
    {state['marketing_plan']}

    Risk Report:
    {state['risk_report']}

    Decide:

    APPROVED
    or
    REJECTED

    Explain why.
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
        "ceo_decision":
        response.choices[0].message.content
    }