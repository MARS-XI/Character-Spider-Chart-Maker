#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Creates pandas DataFrame for Player Chracters based on D&D like stast
"""

# third-party modules
import pandas as pd

# my modules
import data_checks


# MATRICE STATISTICHE PG = { pg_1: [STR, DEX, CON, INT, WIS, CHA], ..., pg_n: [STR, DEX, CON, INT, WIS, CHA] }

def make_dict_(index):
    """make dictionary taking as input lists of stats (1 list --> 1 character)"""
    do_repeat = True
    dict_ = {}  # Initializes empty dictionary

    # Name, stats, "continue?" loop
    while do_repeat:
        c_name = input("Insert character's name: ").title()    # Transforms name to title case

        # Takes input by splitting it into a list in the presence of spaces
        stat_list = input(f'Insert stats ({index}) separated by a space, surplus values will be ignored:').split()
        stat_list = stat_list[:len(index)]    # Drop surplus values

        # If not all the stats are numeric, the stats' request for the current character starts again
        if data_checks.check_stat_type(stat_list) is True:
            continue

        dict_[c_name] = stat_list  # Adds the list to the dict_ionary with key c_name

        while True:
            ask = input('Continue? (y/n): ')  # Asks if you want to insert another line

            if ask.lower() != 'n' and ask != 'y':
                print('ERROR: answer format not supported')
            elif ask.lower() == 'n':
                # Answer is NO, exit "continue?" loop AND character stats imput loop
                do_repeat = False
                break
            else:
                print()    # Print empty line to separate each characters input
                # Answer is YES, exit "continue?" loop
                break
    return dict_


def set_index():
    """asks if the user wants to change the default names of the stats"""

    index = None    # Base case, eventually changed by user

    while True:
        ask = input('Do you want to input your own stats names? (y/n): ')

        if ask.lower() != 'n' and ask.lower() != 'y':
            print('ERROR: answer format not supported')

        elif ask.lower() == 'n':
            break    # Answer is acceptable, exit loop

        else:
            print("The number of stats labels inserted will determine the number of stats values to insert later.")
            index = input('Insert stats names separated by spaces: ').split()

            break    # Answer is acceptable, exit loop

    return index


def make_dataframe():
    """transforms stats dictionary into DataFrame"""
    index = set_index()
    if index is None:    # If index is not modified uses default index
        index = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']    # default index

    dict_ = make_dict_(index)    # Asks character's name and stats
    data_checks.check_len(dict_, index)    # Fill empty values with zeroes

    return pd.DataFrame(dict_, index)    # Transform dictionary into DataFrame adding a line index


if __name__ == '__main__':
    character_stats = make_dataframe()
    print(character_stats)
