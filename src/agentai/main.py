import streamlit as st
from src.agentai.ui.streamlit.load_ui import LoadStreamlitUI
from src.agentai.llms.llm import LLM


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

    user_message = st.chat_input("Enter your message: ")

    # if user_message:
    #     try:
    #         obj_llm_config = LLM(user_controls_input=user_input).get_llm()
    #         model = obj_llm_config.get_llm_model()

    #         if not model:
    #             st.error("Error: LLM Model could not be initialized")
    #             return

    #         usecase = user_input.get("selected_usecase")
    #         if not usecase:
    #             st.error("Error: No use case selected")
    #             return
