import os
import streamlit as st

from src.agentai.ui.ui_config import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title="🤖 " + self.config.get_configs("PAGE_TITLE")[0], layout="wide"
        )
        st.header("🚀 " + self.config.get_configs("PAGE_TITLE")[0])

        with st.sidebar:
            llm_options = self.config.get_configs("LLM_OPTIONS")
            usecases = self.config.get_configs("USECASE_OPTIONS")

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_configs("GROQ_MODEL_OPTIONS")
            elif self.user_controls["selected_llm"] == "HuggingFace":
                model_options = self.config.get_configs("HF_MODEL_OPTIONS")

            # Model Selection
            self.user_controls["selected_model"] = st.selectbox(
                "Select Model", model_options
            )
            self.user_controls["api_key"] = st.session_state["api_key"] = st.text_input(
                "API Key", type="password"
            )
            if not self.user_controls["api_key"]:
                st.warning("Please enter your API Key to proceed")

            # Usecase Selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecase", usecases
            )

        return self.user_controls
