from ConsoleColor import ConsoleColor


class Menu:

    def __init__(self):
        self.buttons = (
            f"{ConsoleColor.OKGREEN}1. Create a dataset{ConsoleColor.ENDC}",
            f"{ConsoleColor.OKGREEN}2. Display datasets{ConsoleColor.ENDC}",
            f"{ConsoleColor.OKGREEN}3. Remove a dataset{ConsoleColor.ENDC}",
            f"{ConsoleColor.OKBLUE}4. Exit{ConsoleColor.ENDC}"
        )

    def display(self) -> None:
        print(f"{ConsoleColor.UNDERLINE}Choose your action by typing a digit{ConsoleColor.ENDC}")
        print(self.buttons[0])
        print(self.buttons[1])
        print(self.buttons[2])
        print(self.buttons[3])
