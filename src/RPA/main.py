from time import sleep

from core import Cutter, Merger
from utils import clear_terminal


# cli incial para interação com a automação:
class Menu:
    def __init__(self):
        # Opcões para o menu:
        self.options = ["Recortar Dataframes", "Mesclar Dataframes"]

    def run(self) -> None:
        # Loop de exibição do menu:
        while True:
            clear_terminal()
            for i, option in enumerate(self.options):
                print(f"{i + 1}. {option}")
            print("0. Sair")
            option = self.__validate_option(input("Escolha uma opção: "))
            if option is (None):
                continue
            elif option == 0:
                break
            else:
                self.__call_core(option)

    def __validate_option(self, option: str) -> int:
        try:
            option = int(option)
            if option < 0 or option > len(self.options):
                print(f"\n\nA opção deve estar entre 0 e, {len(self.options)}.")
                sleep(2)
                return None
            else:
                return option
        except ValueError:
            print("\n\nA opção deve ser um número inteiro!")
            sleep(2)
            return None

    def __call_core(self, option: int) -> None:
        if option == 1:
            cutter = Cutter()
            cutter.cut()
        elif option == 2:
            merger = Merger()
            merger.run()


if __name__ == "__main__":
    menu = Menu()
    menu.run()
