#Create a simple personal diary application where users can write and save their daily thoughts or experiences to a text file. 
# The program should allow users to view their previous entries and handle exceptions in a controlled manner 
# (e.g., file not found errors and permission issues).

import datetime
import sys

#the diary entry function opens the file and writes the entry to the file.
def new_diary_entry():

    try:
        data_to_write = input("\nWrite experiences to diary" +'\n- ')
        entry_timestamp = datetime.datetime.now().date()
        diary_file = open("DiaryEntry.txt","a") #the file is uploaded on github
        log_entry = f"[{entry_timestamp}] {data_to_write}\n"
        diary_file.write(log_entry + '\n')        
        print("\nDiary entry successfully saved to the file.\n")
    except PermissionError:
        print("Error: Permission denied to access the file")

#previous entries of the diary allows the user to view the enteries 
def previous_entries():
    try:
        data_to_read = open("DiaryEntry.txt","r")
        entries = data_to_read.read()
        print(entries)
    except FileNotFoundError:
        print("Diary file not found.\n")

def main():

    print("Select options to entry or view the diary entries")
    print("Option 1: New diary entry")
    print("Option 2: View previous diary entries")
    print("Option 3 Exit")

    Option_selection = input("Choose option 1 or option 2 or option 3: ")
    
    if Option_selection == "1":
        new_diary_entry()
    elif Option_selection == "2":
        previous_entries()
    elif Option_selection == "3":
        print("Exiting the diary application")
        sys.exit()

main()