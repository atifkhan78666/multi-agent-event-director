from llm import client


def marketing_agent(state):

    prompt = f"""
    You are a Marketing Head.

    Event Plan:
    {state['event_plan']}

    Create:

    - Promotion Strategy
    - Social Media Campaign
    - Influencer Outreach
    - Student Engagement Plan
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
        "marketing_plan":
        response.choices[0].message.content
    }