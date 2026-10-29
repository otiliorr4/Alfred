import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class OpenAIModel:
    def __init__(self):
        self.model = os.getenv("OPENAI_MODEL", "gpt-6-luna")
        self.client = OpenAI()

    def generate_response(self, instructions, message):
        response = self.client.responses.create(
            model=self.model,
            instructions=instructions,
            input=message,
        )

        return response.output_text