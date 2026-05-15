import streamlit as st
from src.agentai.ui.streamlit.load_ui import LoadStreamlitUI
from src.agentai.llms.llm import LLM
from src.agentai.graph.builder import GraphBuilder
from src.agentai.ui.streamlit.display_result import DisplayResultStreamlit


def load_app():
    """
    Loads and runs the application. This function initialize the UI,
    handles user inputs, configures the LLM model,
    sets up the graph based on the selected use case,
    and displays the output while implementing exception handling for the robustness
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return

    if st.session_state.is_fetch_button_clicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message: ")

    if user_message:
        try:
            obj_llm_config = LLM(user_controls_input=user_input).get_llm()
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM Model could not be initialized")
                return

            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected")
                return

            graph_builder = GraphBuilder(model=model)
            graph = graph_builder.setup_graph(usecase)
            DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
        except Exception as e:
            st.error(f"Error: Graph setup failed - {e}")
            return
