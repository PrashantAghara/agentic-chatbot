from src.agentai.llms.groq import GroqLLM
from src.agentai.llms.huggingface import HuggingFaceLLM


class LLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm(self):
        selected_llm = self.user_controls_input["selected_llm"]

        llm_mapping = {"Groq": GroqLLM, "HuggingFace": HuggingFaceLLM}

        llm_class = llm_mapping.get(selected_llm)

        if not llm_class:
            raise ValueError(f"Unsupported LLM Provider : {selected_llm}")

        return llm_class(self.user_controls_input)
