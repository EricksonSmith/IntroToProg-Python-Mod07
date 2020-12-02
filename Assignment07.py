# ---------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate exception handling and
#              pickling
# Change Log: (Who, When, What):
# ESmith,12.01.2020,Created Script
# ---------------------------------------- #
# Exception Handling Resources:
# https://www.datacamp.com/community/tutorials/exception-handling-python

# Pickling Resources:
# https://docs.python.org/3/library/pickle.html#module-pickle

import pickle

# Data
# Declare Variables

file_name = "Gamelist.txt"
menu_choice = None
video_game = ""  # element in game rating dictionary
game_rating = ""  # element in game rating dictionary
dict_row = {}  # game row (Title and Rating)
lst_table = []  # list of games and their ratings

class NotValidChoice(Exception): # Exception that reminds the user to choose option 1-4
    def __str__(self):
        return "Please enter valid option: (1 - 4)"

# Processing
class Processor:
    """Contains Process Functions"""

    @staticmethod
    def add_game_rating(game, rating, list_of_rows):
        """ Adds video game and rating to dictionary as a row.
            Then adds dictionary to list (table).
        """

        row = {"Game": game.strip().capitalize(), "Rating": rating.strip().capitalize()}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def pickle_to_file(lst_table, file_name):
        """Function for pickling a list of dictionary key / value
           pairs to a file."""
        file = open(file_name, "ab+")
        pickle.dump(lst_table, file)
        file.close()

    @staticmethod
    def unpickle_from_file(file_name):
        """Function for unpickling a list of dictionary key / value
           pairs from a file."""
        file = open(file_name, "rb")
        list_of_data = pickle.load(file)
        file.close()
        return list_of_data


# Presentation (Input/Output)
class IO:
    """Input and Output Functions"""

    @staticmethod
    def print_menu_option():
        print("""
        Main Menu:
        1.) Add Favorite Games
        2.) Save Data
        3.) Load Data
        4.) Exit
        """)

    @staticmethod
    def input_video_game():
        """ Gets video game and rating from user """

        game = input("Enter Video Game: ")
        rating = input("Enter Video Game's rating (Great, Good, Bad): ")
        return game, rating

    @staticmethod
    def input_menu_choice():
        """Gets user menu choice"""

        choice = str(input("Choose a menu option(1-4): ")).strip()
        return choice

# Main
while(True):
    IO.print_menu_option()
    menu_choice = IO.input_menu_choice()

    try:
        if menu_choice == "1":  # Add Game/Rating to list
            video_game, game_rating = IO.input_video_game()
            Processor.add_game_rating(video_game, game_rating, lst_table)
            input("Press [Enter] to continue")
            continue

        elif menu_choice == "2": # Save list Data to Binary File
            Processor.pickle_to_file(lst_table, file_name)
            input("Data saved! Press [Enter] to continue")
            continue

        elif menu_choice == "3": # Loads Data from Binary File
            Processor.unpickle_from_file(file_name)
            print(lst_table)
            continue

        elif menu_choice == "4": # Exits the program
            break

        else:
            raise NotValidChoice()

    except ValueError as e:
        print("Please enter a number (1-4)")
        print(e, "\n")

    except FileNotFoundError as e:
        print("File was not found.")
        print(e, "\n")

    except Exception as e:
        print(e, "\n")