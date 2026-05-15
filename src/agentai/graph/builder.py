from langgraph.graph import StateGraph, START, END
from src.agentai.state.state import State
from src.agentai.nodes.basic_chatbot_node import BasicChatbotNode
from src.agentai.tools.search_tool import create_tool_node, get_tools
from langgraph.prebuilt import tools_condition
from src.agentai.nodes.chatbot_with_tool_node import ChatbotToolNode
from src.agentai.nodes.ai_news_node import AINewsNode


class GraphBuilder:
    def __init__(self, model):
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

    def build_chatbot_with_web(self):
        """
        Builds a chatbot with tavily web search
        """
        tools = get_tools()
        tool_node = create_tool_node(tools=tools)
        llm = self.llm
        chatbot_node = ChatbotToolNode(llm)

        self.graph_builder.add_node("chatbot", chatbot_node.create_chatbot(tools))
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    def ai_news_builder(self):
        """
        Builds a AI News with Tavily Web search & summerizers.
        """
        node = AINewsNode(llm=self.llm)
        self.graph_builder.add_node("fetch_news", node.fetch_news)
        self.graph_builder.add_node("summarize", node.summarize)
        self.graph_builder.add_node("writer", node.save_results)

        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize")
        self.graph_builder.add_edge("summarize", "writer")
        self.graph_builder.add_edge("writer", END)

    def setup_graph(self, usecase):
        """
        Setup the graph based on usecase
        """
        if usecase == "Basic Chatbot":
            self.build_basic_chatbot()
        if usecase == "Chatbot with Web":
            self.build_chatbot_with_web()
        if usecase == "AI News":
            self.build_chatbot_with_web()

        return self.graph_builder.compile()
