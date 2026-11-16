import json

from alfred.tools.tool_definitions import TOOL_DEFINITIONS


def validar_argumentos(nombre, argumentos_json):
    definicion = next(
        (tool for tool in TOOL_DEFINITIONS if tool["name"] == nombre),
        None,
    )

    if definicion is None:
        raise ValueError("Herramienta no autorizada.")

    try:
        argumentos = json.loads(argumentos_json)
    except (json.JSONDecodeError, TypeError) as error:
        raise ValueError("Argumentos JSON inválidos.") from error

    if not isinstance(argumentos, dict):
        raise ValueError("Los argumentos deben ser un objeto JSON.")

    parametros = definicion["parameters"]
    propiedades = parametros.get("properties", {})
    requeridos = set(parametros.get("required", []))
    recibidos = set(argumentos)

    if not requeridos.issubset(recibidos):
        raise ValueError("Faltan argumentos obligatorios.")

    if not recibidos.issubset(propiedades):
        raise ValueError("Se recibieron argumentos no autorizados.")

    for clave, valor in argumentos.items():
        especificacion = propiedades[clave]

        if especificacion.get("type") != "string":
            raise ValueError("Tipo de argumento aún no compatible.")

        if not isinstance(valor, str):
            raise ValueError(f"El argumento {clave} debe ser texto.")

        if "enum" in especificacion:
            if valor not in especificacion["enum"]:
                raise ValueError(f"Valor no permitido para {clave}.")

    return argumentos