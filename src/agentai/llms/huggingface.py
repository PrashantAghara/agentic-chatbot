import os
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace


class HuggingFaceLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            hf_api_key = self.user_controls_input["api_key"]
            selected_hf_model = self.user_controls_input["selected_model"]
            if hf_api_key == "" and os.environ["HF_TOKEN"] == "":
                st.error("Please enter the HuggingFace API Key")

            endpoint = HuggingFaceEndpoint(
                repo_id=selected_hf_model, huggingfacehub_api_token=hf_api_key
            )

            llm = ChatHuggingFace(llm=endpoint)
        except Exception as e:
            raise ValueError(f"Error occurred with exception : {e}")

        return llm
