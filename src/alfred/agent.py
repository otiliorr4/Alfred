from alfred.llm import OpenAIModel
from alfred.prompts import ALFRED_SYSTEM_PROMPT


class AlfredAgent:
    def __init__(self, name="Alfred"):
        self.name = name
        self.system_prompt = ALFRED_SYSTEM_PROMPT
        self.model = OpenAIModel()

    def process_message(self, message):
        return self.model.generate_response(
            instructions=self.system_prompt,
            message=message,
        )