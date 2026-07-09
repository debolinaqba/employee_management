from operations import *
from utils import menu

while True:

    menu()

    choice = input("Enter Choice : ")

    if choice == "1":

        add_employee()

    elif choice == "2":

        display_all()

    elif choice == "3":

        search_employee()

    elif choice == "4":

        delete_employee()

    elif choice == "5":

        print("Thank You")

        break

    else:

        print("Invalid Choice")