from ConsoleColor import ConsoleColor
from Menu import Menu
from NaturalLanguageAPI import NaturalLanguageAPI


if __name__ == '__main__':
    print(f"{ConsoleColor.HEADER}Review bombing validator{ConsoleColor.ENDC}\n")

    while True:
        try:
            menu: Menu = Menu()
            naturalLanguageAPI = NaturalLanguageAPI()
            dataset_name: str

            menu.display()

            input_value: int
            try:
                input_value = int(input(">"))
            except:
                input_value = -1

            if input_value == 1:
                naturalLanguageAPI.create_dataset(
                    input(f"{ConsoleColor.WARNING}Create a dataset{ConsoleColor.ENDC}, Enter the display name: ")
                )
            elif input_value == 2:
                naturalLanguageAPI.display_datasets()
            elif input_value == 3:
                naturalLanguageAPI.remove_dataset(
                    input(f"{ConsoleColor.WARNING}Remove a dataset{ConsoleColor.ENDC}, Enter id: ")
                )
            elif input_value == 4:
                quit(0)
            else:
                print(f"\n{ConsoleColor.FAIL}Incorrect input value{ConsoleColor.ENDC}\n")

        except Exception as ex:
            print(f"{ConsoleColor.FAIL}{ex}{ConsoleColor.ENDC}\n")


