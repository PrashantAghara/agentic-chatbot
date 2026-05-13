from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    Represent the structure of the state in graph
    """

    messages: Annotated[list, add_messages]
