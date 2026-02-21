import os
import json
import webbrowser
import requests
from bs4 import BeautifulSoup

files = {}

try:
    with open("files.json", "r") as f:
        files = json.load(f)
except FileNotFoundError:
    files = {}

LOCAL_VERSION = "Beta 1.0.0"

def load():
    global files
    try:
        with open("files.json", "r") as f:
            files = json.load(f)
    except FileNotFoundError:
        files = {}
def save():
    with open("files.json", "w") as f:
        json.dump(files, f, indent=4)

def make_file(filename):
    if not filename.endswith(".nxa"):
        filename += ".nxa"
    if filename in files:
        print(f"File '{filename}' already exists.")
    else:
        files[filename] = ""
        save()
        print(f"File '{filename}' created successfully.")

def preview_file(filedata):
    content = filedata.split("\n")
    for line in content:
        # Breaks
        if line.startswith("break "):
            print("-" * int(line[6:]))
        elif line.startswith("dbreak "):
            print("=" * int(line[7:]))
        elif line.startswith("hbreak "):
            print("#" * int(line[7:]))
        elif line.startswith("lbreak "):
            print("~" * int(line[7:]))
        elif line.startswith("sbreak "):
            print("*" * int(line[7:]))
        # Lists
        elif line.startswith("list: "):
            items = line[6:].split(",")
            for item in items:
                print(f"- {item.strip()}")
        elif line.startswith("nlist: "):
            items = line[7:].split(",")
            for i, item in enumerate(items, start=1):
                print(f"{i}. {item.strip()}")
        elif line.startswith("tlist: "):
            items = line[7:].split(",")
            for i, item in enumerate(items, start=1):
                print(f"{i}) {item.strip()}")
        elif line.startswith("dlist: "):
            items = line[7:].split(",")
            for i, item in enumerate(items, start=1):
                print(f"{i}. {item.strip()}")
        elif line.startswith("ulist: "):
            items = line[7:].split(",")
            for item in items:
                print(f"* {item.strip()}")
        # Default
        else:
            print(line)
        
def read_file(filename):
    if not filename.endswith(".nxa"):
        filename += ".nxa"
    if filename in files:
        print(f"Contents of '{filename}':")
        preview_file(files[filename])
    else:
        print(f"File '{filename}' does not exist.")

def delete_file(filename):
    if not filename.endswith(".nxa"):
        filename += ".nxa"
    if filename in files:
        del files[filename]
        save()
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' does not exist.")

def write_file(filename, content):
    if not filename.endswith(".nxa"):
        filename += ".nxa"
    files[filename] = content
    save()
    print(f"Content written to '{filename}' successfully.")

def list_files():
    if files:
        print("NXA Files:")
        for filename in files:
            print(f"- {filename}")
    else:
        print("No .nxa files found.")

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
    except Exception as e:
        return "You are offline or there was an error retrieving the data."

def console():
    load()
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
            print(" - mkf [filename]: Create an empty .nxa file with the given name")
            print(" - read [filename]: Read and display the contents of a .nxa file")
            print(" - delete [filename]: Delete a .nxa file")
            print(" - write [filename] [content]: Write content to a .nxa file")
            print(" - list: List all .nxa files in the current directory")
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
        elif command.lower().startswith("mkf "):
            filename = command[4:]
            make_file(filename)
        elif command.lower().startswith("read "):
            filename = command[5:]
            read_file(filename)
        elif command.lower().startswith("delete "):
            filename = command[7:]
            delete_file(filename)
        elif command.lower().startswith("write "):
            parts = command.split(" ", 2)
            if len(parts) < 3:
                print("Usage: write [filename] [content]")
            else:
                filename = parts[1]
                content = parts[2]
                write_file(filename, content)
        elif command.lower() == "list":
            list_files()
        else:
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")
        save()


if __name__ == "__main__":
    console()
