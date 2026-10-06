from alfred.prompts import ALFRED_SYSTEM_PROMPT


class AlfredAgent:
    def __init__(self, name="Alfred"):
        self.name = name
        self.system_prompt = ALFRED_SYSTEM_PROMPT

    def process_message(self, message):
        return f"He recibido: {message}"