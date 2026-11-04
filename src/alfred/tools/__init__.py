from alfred.tools.registry import register_tool
from alfred.tools.programs import abrir_programa
from alfred.tools.web_pages import abrir_pagina_web
from alfred.tools.system_info import obtener_estado_pc


def register_default_tools():
    register_tool("abrir_programa", abrir_programa)
    register_tool("abrir_pagina_web", abrir_pagina_web)
    register_tool("obtener_estado_pc", obtener_estado_pc)