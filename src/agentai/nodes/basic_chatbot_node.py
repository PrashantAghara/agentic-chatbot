from src.agentai.state.state import State


class BasicChatbotNode:
    """
    Basic chatbot node implementation
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        return {"messages": self.llm.invoke(state["messages"])}
