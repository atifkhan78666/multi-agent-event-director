from langgraph.graph import StateGraph, END

from ceo_agent import ceo_agent
from marketing_agent import marketing_agent
from risk_agent import risk_agent
from state import EventState

from planner_agent import planner_agent
from sponsorship_agent import sponsorship_agent
from finance_agent import finance_agent
from report_agent import report_agent


graph = StateGraph(EventState)

graph.add_node(
    "planner",
    planner_agent
)

graph.add_node(
    "sponsorship",
    sponsorship_agent
)

graph.add_node(
    "finance",
    finance_agent
)

graph.add_node(
    "report",
    report_agent
)

graph.add_node(
    "marketing",
    marketing_agent
)

graph.add_node(
    "risk",
    risk_agent
)

graph.add_node(
    "ceo",
    ceo_agent
)

graph.set_entry_point("planner")

graph.add_edge("planner", "sponsorship")
graph.add_edge("sponsorship", "finance")
graph.add_edge("finance", "marketing")
graph.add_edge("marketing", "risk")
graph.add_edge("risk", "ceo")
graph.add_edge("ceo", "report")
graph.add_edge("report", END)

app = graph.compile()