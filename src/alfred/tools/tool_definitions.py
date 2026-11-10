TOOL_DEFINITIONS = [
    {
        "type": "function",
        "name": "obtener_estado_pc",
        "description": (
            "Consulta el estado actual de la computadora, "
            "incluyendo uso de CPU, memoria RAM y batería."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        "strict": True,
    },
        {
        "type": "function",
        "name": "abrir_programa",
        "description": (
            "Abre una aplicación autorizada de Windows. "
            "Actualmente solo puede abrir Notepad "
            "(Bloc de notas), usando el nombre bloc_de_notas."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "nombre": {
                    "type": "string",
                    "enum": ["bloc_de_notas"],
                    "description": "Nombre interno del programa autorizado.",
                }
            },
            "required": ["nombre"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]
