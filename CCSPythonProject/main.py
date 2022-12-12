from ConsoleColor import ConsoleColor
from Menu import Menu
from NaturalLanguageAPI import NaturalLanguageAPI
from StorageAPI import StorageAPI

if __name__ == '__main__':
    while True:
        try:
            dataset_name: str
            input_value: int

            menu: Menu = Menu()
            naturalLanguageAPI = NaturalLanguageAPI()
            storageAPI = StorageAPI()

            menu.display()

            try:
                input_value = int(input(">"))
            except TypeError:
                input_value = -1

            if input_value == 1:
                naturalLanguageAPI.create_dataset(
                    input(f"Enter the new dataset's display name: "),
                    input("Enter the existing blob's name: ")
                )

            elif input_value == 2:
                naturalLanguageAPI.display_datasets()

            elif input_value == 3:
                naturalLanguageAPI.remove_dataset(input(f"Enter id: "))

            elif input_value == 4:
                storageAPI.create_blob(
                    input("Enter the new blob's name: "),
                    input("Enter the existing file's name: ")
                )

            elif input_value == 5:
                storageAPI.list_blobs()

            elif input_value == 6:
                storageAPI.remove_blob(input(f"Enter blob's name: "))

            elif input_value == 7:
                quit(0)

            else:
                print(f"\n{ConsoleColor.FAIL}Incorrect input value{ConsoleColor.ENDC}\n")

        except Exception as ex:
            print(f"{ConsoleColor.FAIL}{ex}{ConsoleColor.ENDC}\n")
