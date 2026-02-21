import os
import webbrowser
from nxaconsole import console

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

header = "=" * 44
print(header)
print("|| NXA Developer Portal || Version: 1.0.0")
print(header)
print("|| User:")
print("|| Role:")
print(header)
print("|| Enter your data")
print(header)

isLoggedIn = False

while not isLoggedIn:
    username = input("|| Username: ")
    password = input("|| Password: ")
    print(header)

    if len(username) == 0 or len(password) == 0:
        print("Username and password cannot be empty")
    else:
        clear_screen()
        print("Login successful")
        isLoggedIn = True
while True:
    print(header)
    print("|| Welcome to the NXA Developer Portal")
    print(header)
    print("|| Please select an option:")
    print("|| 1. NXA Developer Console")
    print("|| 2. NXA GitHub Repository")
    print("|| 3. Exit")
    print(header)
    option = input("|| Enter your choice: ")
    if option == "1" or option.lower() == "nxa developer console":
        print("Opening NXA Developer Console...")
        console()
        clear_screen()
    elif option == "2" or option.lower() == "nxa github repository":
        print("Opening NXA GitHub Repository...")
        webbrowser.open("https://github.com/Notxnorand73/NXA-Developer-Portal")
        clear_screen()
    elif option == "3" or option.lower() == "exit":
        print("Exiting...")
        clear_screen()
        quit()
    else:
        print("Invalid option. Please try again.")
