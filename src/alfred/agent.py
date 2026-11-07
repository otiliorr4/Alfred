from alfred.llm import OpenAIModel
from alfred.prompts import ALFRED_SYSTEM_PROMPT
from alfred.tools import register_default_tools

class AlfredAgent:
    def __init__(self, name="Alfred"):
        self.name = name
        self.system_prompt = ALFRED_SYSTEM_PROMPT
        self.model = OpenAIModel()
        register_default_tools()

    def process_message(self, message):
        return self.model.generate_response_with_tools(
            instructions=self.system_prompt,
            message=message,
        )