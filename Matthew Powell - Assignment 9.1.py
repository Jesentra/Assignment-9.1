'''
Investment Schedule
07 August, 2022
Matthew Powell
CIS245
A script that will put a user in a desired directory, then store personal details.
'''

import os # Importing the OS function so that we can make OS commands

'''Creating the functions for the program'''
def manage_dir(req_dir): # The function that will attempt to create the requested directory in CWD
    try: # First, try to create the directory
        os.mkdir(req_dir)
    except FileExistsError: # If the directory exists already, move on.
        pass # Fails silently and moves to next line.
    answers() # Moves to next step either way

def answers(): # Create a list from questions
    name = input('What is your name?: ').title() #Ask questions and put them into the info list
    address = input('What is your address?: ').title()
    phone = input('What is your phone number?: ')
    global info # Creates a variable that can be accessed outside the function
    info = f'Name: {name}, Address: {address}, Phone Number: {phone}' # Consolidating all information into one string
    scribe() #Calls next function

def scribe(): #Creates and writes the info list to a file in the requested directory, then print them
    filename = os.path.join(req_dir, 'personal_info.txt') # Establishes the directory and the text file name to be created
    with open(filename, 'w') as f: # Creates the personal_info.txt file and fills it with the info from the answers() function
        f.write(str(info)) 
    with open(filename) as f: # Reads the contents of the personal_info.txt file and stores them into a variable.
        contents = f.read()
    print(contents) # Displays the contents of the personal_info.txt

"""Beginning of the program"""
req_dir = input("Which directory do you want to save your information in?: ")
manage_dir(req_dir)