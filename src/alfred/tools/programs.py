import subprocess


PROGRAMAS_PERMITIDOS = {
    "bloc_de_notas": ["notepad.exe"],
}


def abrir_programa(nombre):
    comando = PROGRAMAS_PERMITIDOS.get(nombre.strip().lower())

    if comando is None:
        return f"Programa no permitido: {nombre}"

    try:
        subprocess.Popen(comando)
        return f"Se solicitó abrir: {nombre}"

    except OSError as error:
        return f"No se pudo abrir {nombre}: {error}"