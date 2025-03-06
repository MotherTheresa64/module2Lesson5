# Lesson 5: Managing Favorite Foods and TV Shows

# ============================
# Engage and Apply -----------> Exercise 1 (Pre-provided)
# ============================

"""
Task: Create a simple Python program that:
- Allows the user to add favorite foods to a list.
- Stores the data in a file.
- Lets the user view or remove items from the list.
"""

def write_foods(foods):
    with open('foods.txt', 'w') as file:
        for food in foods:
            file.write(food + '\n')

def read_foods():
    foods_list = []
    with open('foods.txt', 'r') as file:
        for line in file:
            foods_list.append(line.strip())
    return foods_list

def main():
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove Food, 4 - Quit\n")
        if action == '1':
            new_food = input("Enter the name of the food: ")
            foods.append(new_food)
            write_foods(foods)
        elif action == '2':
            print("Your favorite foods:")
            for food in foods:
                print(food)
        elif action == '3':
            idx = int(input("Which food to remove? "))
            foods.pop(idx - 1)
            write_foods(foods)
        elif action == '4':
            break

main()

# ============================
# Engage and Apply -----------> Exercise 1 (My Interpretation Applied)
# ============================

"""
Task: Create a simple Python program that:
- Allows the user to add favorite foods to a list.
- Stores the data in a file.
- Lets the user view or remove items from the list.

This is my applied version:
- Allows more detailed interaction, with confirmation messages.
- File handling for appending and reading is simplified for clarity.
- Added an extra feature to check for file existence before attempting to read it.
"""

import os

def write_foods(foods):
    with open('foods.txt', 'w') as file:
        for food in foods:
            file.write(food + '\n')

def read_foods():
    # Check if file exists before trying to read it
    if not os.path.exists('foods.txt'):
        return []
    
    foods_list = []
    with open('foods.txt', 'r') as file:
        for line in file:
            foods_list.append(line.strip())
    return foods_list

def main():
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove Food, 4 - Quit\n")
        if action == '1':
            new_food = input("Enter the name of the food: ")
            foods.append(new_food)
            write_foods(foods)
            print(f"{new_food} added to your list!")
        elif action == '2':
            if foods:
                print("Your favorite foods:")
                for idx, food in enumerate(foods, 1):
                    print(f"{idx}. {food}")
            else:
                print("No foods in the list yet.")
        elif action == '3':
            if foods:
                idx = int(input("Which food to remove? "))
                removed_food = foods.pop(idx - 1)
                write_foods(foods)
                print(f"{removed_food} has been removed from your list.")
            else:
                print("No foods to remove.")
        elif action == '4':
            print("Goodbye! Your changes have been saved.")
            break

main()

# ============================
# Final Challenge -----------> Final Challenge (Pre-provided)
# ============================

"""
Scenario: Modify the TV show manager program to allow the user to edit the platform or genre of an existing TV show.
"""

# Function to write TV shows to a file
def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

# Function to add a show to our shows list in dictionary format
def add_show(shows):
    title = input("What is the title of the show? ")
    platform = input("Where can we watch it? ")
    genre = input("What is the genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)

# Function to read TV shows from a file
def read_shows():
    shows_list = []
    with open('shows_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list

# Function to print the list of shows for the user in a formatted way
def view(shows):
    print("Shows List")
    print('-----------------------')
    for idx, show in enumerate(shows):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")

# Function to remove a TV show
def remove_show(shows):
    view(shows)
    option = int(input("\n\nChoose a number for the show you'd like to remove: "))
    show = shows.pop(option - 1)  # index - 1
    print(f"\n{show['Title']} was successfully removed!")
    write_show(shows)

# Function to edit platform or genre of a show
def edit_show(shows):
    view(shows)
    option = int(input("Choose a number to edit: "))
    field = input("Do you want to edit the platform or genre? (Enter 'platform' or 'genre'): ").lower()
    if field == 'platform':
        new_platform = input("Enter new platform: ")
        shows[option - 1]['Platform'] = new_platform
    elif field == 'genre':
        new_genre = input("Enter new genre: ")
        shows[option - 1]['Genre'] = new_genre
    write_show(shows)
    print(f"Show updated: {shows[option - 1]}")

# Main function to run the TV show manager
def main():
    while True:
        shows_list = read_shows()
        action = input('''Options:
        1 - Add a TV Show
        2 - Remove a TV Show
        3 - View List of TV Shows
        4 - Edit a TV Show
        5 - Quit
        ''')
        if action == '1':
            add_show(shows_list)
        elif action == '2':
            remove_show(shows_list)
        elif action == '3':
            view(shows_list)
        elif action == '4':
            edit_show(shows_list)  # Allow user to edit a show
        elif action == '5':
            print("Thanks for using the app!")
            break

# Call main() to start the program
if __name__ == '__main__':
    main()

# ============================
# Final Challenge -----------> Final Challenge (My Interpretation Applied)
# ============================

"""
Scenario: Modify the TV show manager program to allow the user to edit the platform or genre of an existing TV show.

My applied version includes the following enhancements:
- Users can now edit either the genre or platform.
- Confirmations are provided after edits.
- Streamlined file handling to ensure data is updated correctly after edits.
- Added functionality for editing both fields (platform or genre).
"""

import re

# Function to write TV shows to a file
def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

# Function to add a show to our shows list in dictionary format
def add_show(shows):
    title = input("What is the title of the show? ")
    platform = input("Where can we watch it? ")
    genre = input("What is the genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)

# Function to read TV shows from a file
def read_shows():
    shows_list = []
    with open('shows_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list

# Function to print the list of shows for the user in a formatted way
def view(shows):
    print("Shows List")
    print('-----------------------')
    for idx, show in enumerate(shows):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")

# Function to remove a TV show
def remove_show(shows):
    view(shows)
    option = int(input("\n\nChoose a number for the show you'd like to remove: "))
