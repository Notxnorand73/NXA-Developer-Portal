import os
import webbrowser
import requests
from bs4 import BeautifulSoup

LOCAL_VERSION = "Beta 1.0.0"

def retrieve(part):
    try:
        # Use raw GitHub URL for direct text access
        url = "https://raw.githubusercontent.com/Notxnorand73/NXA-Developer-Portal/main/data.txt"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Parse
        if part == "Releases":
            # get everything after the "Releases:" line
            lines = response.text.strip().split('\n')
            for i, line in enumerate(lines):
                if line.startswith("Releases:"):
                    return "\n".join(lines[i+1:])  # Return everything after "Releases:"
        else:
            lines = response.text.strip().split('\n')
            for line in lines:
                if line.startswith(f"{part}: "):
                    remote = line.split(': ')[1]  # Extract "Beta 1.0.0"
        
        if part == "Version":
            if remote == LOCAL_VERSION:
                return f"You have {LOCAL_VERSION}. You're up to date!"
            else:
                return f"You have {LOCAL_VERSION}. A new version {remote} is available!"
        elif part == "Publisher":
            return f"Publisher: {remote}"
        elif part == "Releases":
            pass
    except Exception as e:
        return f"You have {LOCAL_VERSION}. (Couldn't check for updates: {e})"

def console():
    while True:
        command = input("NXA Console> ")
        if command.lower() == "exit":
            print("Exiting NXA Console...")
            break
        elif command.lower() == "help":
            print("Available commands:")
            print(" - help: Show this help message")
            print(" - exit: Exit the console")
            print(" - clear: Clear the console")
            print(" - version: Show the console version")
            print(" - publisher: Show the publisher information")
            print(" - releases: Show the latest releases")
            print(" - about: Show information about the console")
            print(" - echo [message]: Echo the message back to the console")
            print(" - open [url]: Open the url in the default web browser")
        elif command.lower() == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command.lower() == "version":
            print(retrieve("Version"))
        elif command.lower() == "about":
            print("NXA Console is a simple command-line interface for developers to interact with the NXA Developer Portal.")
        elif command.lower() == "publisher":
            print(retrieve("Publisher"))
        elif command.lower() == "releases":
            print(retrieve("Releases"))
        elif command.lower().startswith("echo "):
            message = command[5:]
            print(message)
        elif command.lower().startswith("open "):
            url = command[5:]
            os.system(f"start {url}" if os.name == 'nt' else f"xdg-open {url}")
        else:
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")


if __name__ == "__main__":
    console()