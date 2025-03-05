# Python File Handling Notes

# 📌 Overview

"""
This lesson covers the fundamentals of Python file handling. By the end, you'll be able to interact with files (open, read, write, append) 
and handle structured data like lists and dictionaries. Additionally, you'll build interactive programs that allow data management through file operations.

Learning Objectives:
- Open, read, write, and append to files.
- Store and retrieve structured data using text files.
- Build interactive programs for data management.
- Practice advanced file handling using real-world examples.
"""

# 1. **Opening and Writing to Files**
# To write to a file in Python, use the open() function with the mode 'w' (write) or 'a' (append). 
# Always close the file after writing.

# Example:
def write_file():
    # Writing to a file (Overwrites the file)
    with open('new_file.txt', 'w') as file:
        file.write('Writing to a file from Python!\n')

    # Appending to the file (does not overwrite)
    with open('new_file.txt', 'a') as file:
        file.write('Adding more content with "a" mode\n')

# The 'w' Mode: Overwrites the file if it exists.
# The 'a' Mode: Appends data to the end without overwriting.

# 2. **Reading Files**
# To read files, use methods like read(), readline(), and readlines(). 
# Always use a with open() statement to ensure the file is properly closed.

def read_file():
    with open('new_file.txt', 'r') as file:
        content = file.read()  # Read the entire file content
        print(content)

# 3. **Storing and Extracting Data (Lists & Dictionaries)**

# Storing and Extracting Lists:
def store_and_extract_lists():
    flowers = ["Wysteria", "Sunflowers", "Orchids", "Marigolds"]
    
    # Storing a list in a file
    with open('garden.txt', 'w') as file:
        for flower in flowers:
            file.write(flower + '\n')
    
    # Extracting a list from a file
    flowers = []
    with open('garden.txt', 'r') as file:
        for line in file:
            flowers.append(line.strip())  # Removes extra spaces/newlines
    print(flowers)

# Storing and Extracting Dictionaries:
def store_and_extract_dicts():
    clubs = {'Driver': 'Cobra', 'Irons': 'Sirixion', 'Hybrid': 'Callaway', 'Putter': 'Ping'}
    
    # Storing a dictionary in a file
    with open('golf_bag.txt', 'w') as file:
        for club, brand in clubs.items():
            file.write(f"{club}: {brand}\n")
    
    # Extracting a dictionary from a file
    golf_clubs = {}
    with open('golf_bag.txt', 'r') as file:
        for line in file:
            club, brand = line.strip().split(': ')
            golf_clubs[club] = brand
    print(golf_clubs)

# 4. **Managing Data Interactively: TV Show Manager** ----------------------------------------- Exercise 1
# This advanced exercise builds a TV show manager using structured data and file handling. 
# We'll be writing, reading, and removing data about TV shows, including their title, platform, and genre.

import re

def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

def read_shows():
    shows_list = []
    with open('shows_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list

def add_show(shows):
    title = input("Enter the show title: ")
    platform = input("Where can we watch it? ")
    genre = input("What is the genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)

def remove_show(shows):
    view(shows)
    option = int(input("Choose a number to remove: "))
    show = shows.pop(option - 1)
    print(f"{show['Title']} was successfully removed!")
    write_show(shows)

def view(shows):
    print("Shows List")
    for idx, show in enumerate(shows):
        a_or_an = 'an' if show['Genre'][0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'
        print(f"{idx + 1}. {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")

def main():
    while True:
        shows_list = read_shows()
        action = input('''Options:
        1 - Add a TV Show
        2 - Remove a TV Show
        3 - View List of TV Shows
        4 - Quit
        ''')
        if action == '1':
            add_show(shows_list)
        elif action == '2':
            remove_show(shows_list)
        elif action == '3':
            view(shows_list)
        elif action == '4':
            print("Thanks for using the app!")
            break

# Call main() to start the program
if __name__ == '__main__':
    main()

# 5. **Final Challenge** ----------------------------------------- Final Challenge
# Modify the TV show manager program to allow users to edit the platform or genre of an existing TV show.
