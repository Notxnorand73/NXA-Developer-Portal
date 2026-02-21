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
    elif username == "admin" and password == "admin":
        clear_screen()
        print("Admin login successful")
        isLoggedIn = True
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
    if option == "1":
        print("Opening NXA Developer Console...")
        console()
    elif option == "2":
        print("Opening NXA GitHub Repository...")
        webbrowser.open("https://github.com/Notxnorand73/NXA-Developer-Portal")
    elif option == "3":
        print("Exiting...")
        quit()
    else:
        print("Invalid option. Please try again.")
