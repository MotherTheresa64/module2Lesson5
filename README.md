# Module 2: Lesson 5 - Python File Handling

## Overview
In this lesson, we explore Python file handling, covering how to work with files for reading and writing data. We demonstrate how to open files, read from them, write to them, and manage structured data like lists and dictionaries within files. By the end of this lesson, you'll be able to create interactive programs that save data to and load data from files.

## File Summaries

1. **notes.py**
   - Contains summarized notes for the lesson, covering key concepts in Python file handling, including how to open and read files, write to them, store structured data, and build interactive programs that manage data in files.
   - **Sections**:
     - **Opening and Writing to Files**: Shows how to use `open()` with different modes (`'w'` for writing, `'a'` for appending).
     - **Reading Files**: Demonstrates reading files using `read()`, `readline()`, and `readlines()`.
     - **Storing and Extracting Data**: Shows how to store structured data like lists and dictionaries into a file, and how to read them back.
     - **Interactive Programs**: Covers creating an interactive menu to manage lists and dictionaries, providing a practical example of file handling in action.

2. **lessonFiveProject.py**
   - **Engage and Apply**: 
     - A simple Python program to manage a list of favorite foods. The program allows the user to add, view, and remove foods from a list, which is saved to a file (`foods.txt`).
     - The program demonstrates file handling with basic operations such as writing to and reading from a file.
   
   - **Final Challenge**: 
     - A TV show manager program where the user can add, remove, view, and now **edit** TV show details (platform or genre) in a file (`shows_list.txt`).
     - The challenge was extended to allow editing features and dynamic updates based on user interaction.

   - **Enhancements**:
     - For **Engage and Apply**, I added functionality to check if the file exists before reading and added more informative print statements.
     - For the **Final Challenge**, I modified the program to include the option to edit the platform or genre of existing TV shows.
