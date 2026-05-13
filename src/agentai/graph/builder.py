from langgraph.graph import StateGraph, START, END
from src.agentai.state.state import State
from src.agentai.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(
        self,
        model,
    ):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def build_basic_chatbot(self):
        """
        Builds a basic chatbot.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase):
        """
        Setup the graph based on usecase
        """
        if usecase == "Basic Chatbot":
            self.build_basic_chatbot()
