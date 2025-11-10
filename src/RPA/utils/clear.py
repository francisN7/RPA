import os


def clear_terminal() -> None:  # Limpa o terminal
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para Mac e Linux
    else:
        os.system("clear")
