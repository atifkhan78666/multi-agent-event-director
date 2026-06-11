from llm import client


def finance_agent(state):

    prompt = f"""
    You are a Finance Manager.

    Event Plan:

    {state['event_plan']}

    Sponsorship Plan:

    {state['sponsorship_plan']}

    Generate:

    - Estimated Budget
    - Expense Breakdown
    - Revenue Sources
    - Profitability Analysis
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
        "finance_plan":
        response.choices[0].message.content
    }