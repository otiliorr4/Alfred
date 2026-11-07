import os
import json

from alfred.tools.registry import get_tool
from alfred.tools.tool_definitions import TOOL_DEFINITIONS
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
    def generate_response_with_tools(self, instructions, message):
        response = self.client.responses.create(
            model=self.model,
            instructions=instructions,
            input=message,
            tools=TOOL_DEFINITIONS,
            parallel_tool_calls=False,
        )

        llamadas = [
            item for item in response.output
            if item.type == "function_call"
        ]

        if not llamadas:
            return response.output_text

        llamada = llamadas[0]

        # Por ahora, solo autorizamos esta herramienta.
        if llamada.name != "obtener_estado_pc":
            return "La herramienta solicitada no está autorizada."

        try:
            argumentos = json.loads(llamada.arguments)
        except (json.JSONDecodeError, TypeError):
            return "El modelo generó argumentos inválidos."

        if argumentos != {}:
            return "La herramienta recibió argumentos no permitidos."

        funcion = get_tool(llamada.name)

        if funcion is None:
            return "No se encontró la herramienta solicitada."

        try:
            resultado = funcion()
        except Exception:
            return "Ocurrió un error al ejecutar la herramienta."

        respuesta_final = self.client.responses.create(
            model=self.model,
            instructions=instructions,
            previous_response_id=response.id,
            input=[{
                "type": "function_call_output",
                "call_id": llamada.call_id,
                "output": json.dumps(resultado),
            }],
            tools=TOOL_DEFINITIONS,
            parallel_tool_calls=False,
        )

        if any(
            item.type == "function_call"
            for item in respuesta_final.output
        ):
            return "El modelo solicitó otra herramienta; todavía no está permitido."

        return respuesta_final.output_text    

        return response.output_text