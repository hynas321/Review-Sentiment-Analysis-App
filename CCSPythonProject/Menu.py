from ConsoleColor import ConsoleColor


class Menu:

    def __init__(self):
        self.buttons = (
            "* Vertex AI operations (datasets)",
            f"{ConsoleColor.WARNING}1. Create a dataset{ConsoleColor.ENDC}",
            f"{ConsoleColor.WARNING}2. Display datasets{ConsoleColor.ENDC}",
            f"{ConsoleColor.WARNING}3. Remove a dataset{ConsoleColor.ENDC}",
            "* Google Storage operations (blobs)",
            f"{ConsoleColor.WARNING}4. Add a blob{ConsoleColor.ENDC}",
            f"{ConsoleColor.WARNING}5. Display blobs{ConsoleColor.ENDC}",
            f"{ConsoleColor.WARNING}6. Remove a blob{ConsoleColor.ENDC}",
            "* Other",
            f"{ConsoleColor.OKBLUE}7. Exit{ConsoleColor.ENDC}"
        )

    def display(self):
        print(f"Choose your action by typing a digit")
        for button in self.buttons:
            print(button)
