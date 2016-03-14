#! python3

import os
import file_organize
import file_rename


def type_input(inputted_command):
    """
    type_input takes in a inputted_command and calls the functions that organize/rename the music files
    type_input: any of "run "organize" "quit" -> functions from FileOrganize FileRename
    :type inputted_command: any of "run "organize" "quit"
    """
    if inputted_command == "run":
        if "yes" == input("Are you sure? Make sure you back up your files first (yes/no):"):
            for dirname, dirnames, filenames in os.walk('.'):
                for subdirname in dirnames:
                    file_rename.rename_file(os.path.join(dirname, subdirname))
                for filename in filenames:
                    file_rename.rename_file(os.path.join(dirname, filename))
            print("Successful")
            type_input(input("organize - Organize all music files into folders for "
                             "their corresponding album/artist name" + os.linesep +
                             "quit - exit the program" + os.linesep +
                             "Type your command:"))
        else:
            type_input(input("run - Collapse all folders and rename music files" + os.linesep +
                             "organize - Organize all music files into folders for "
                             "their corresponding album/artist name" + os.linesep +
                             "quit - exit the program" + os.linesep +
                             "Type your command:"))
    if inputted_command == "organize":
        if "yes" == input("Are you sure? Make sure you back up your files first (yes/no):"):
            for dirname, dirnames, filenames in os.walk('.'):
                for subdirname in dirnames:
                    file_organize.organize_file(os.path.join(dirname, subdirname))
                for filename in filenames:
                    file_organize.organize_file(os.path.join(dirname, filename))
            print("Successful")
            type_input(input("run - Collapse all folders and rename music files" + os.linesep +
                             "quit - exit the program" + os.linesep +
                             "Type your command:"))
        else:
            type_input(input("run - Collapse all folders and rename music files" + os.linesep +
                             "organize - Organize all music files into folders for "
                             "their corresponding album/artist name" + os.linesep +
                             "quit - exit the program" + os.linesep +
                             "Type your command:"))
    elif inputted_command == "quit":
        pass

    else:
        type_input(input("Invalid Command" + ''' " ''' + inputted_command + ''' " :'''))
