from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Return list of tools
    """
    web_search = TavilySearchResults(
        k=1,
        max_results=1,
        search_depth="basic",
        include_answer=False,
        include_raw_content=False,
    )

    tools = [web_search]
    return tools


def create_tool_node(tools):
    """
    Creates and return tool node for a graph
    """
    return ToolNode(tools=tools)
