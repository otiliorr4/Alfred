import subprocess


PROGRAMAS_PERMITIDOS = {
    "bloc_de_notas": ["notepad.exe"],
}


def abrir_programa(nombre):
    comando = PROGRAMAS_PERMITIDOS.get(nombre.strip().lower())

    if comando is None:
        raise ValueError(f"Programa no permitido: {nombre}")

    subprocess.Popen(comando)

    return f"Se solicitó abrir: {nombre}"