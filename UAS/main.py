import sys
import os 
 
from data.data import Data
from view.view import View
from process.process import Process

if __name__ == "__main__":
    data = Data()
    view = View()
    process = Process(data, view)

    while True:
        view.display_menu()
        choice = view.get_input("Choose an option (1-3): ")

        if choice == "1":
            process.add_item()
        elif choice == "2":
            process.view_items()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
