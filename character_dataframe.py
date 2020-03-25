#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Creates pandas DataFrame for Player Chracters based on D&D like stast
"""

# third-party modules
import pandas as pd

__author__ = "Marcello Lamonaca"
__coptright__ = "Copyright 2019, Marcello Lamonaca"
__credits__ = ["Marcello Lamonaca"]
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Marcello Lamonaca"
__email__ = ""
__status__ = "Dev"


'''
MATRICE STATISTICHE PG
pg_1: [STR, DEX, CON, INT, WIS, CHA]
...
pg_n: [STR, DEX, CON, INT, WIS, CHA]
'''


def make_dict_(index):
    """make dictionary taking as input lists of stats (1 list --> 1 character)"""
    do_repeat = True
    dict_ = {}  # initializes empty dictionary

    while do_repeat:
        c_name = input("Insert character's name: ").title()    # transforms name to title case
        # takes input by splitting it into a list in the presence of spaces
        stat_list = input(f'Insert stats ({index}) separated by a space:').split()

        stat_input_error = check_stat_type(stat_list)
        # if not all the stats are numeric, the stats' request for the current character starts again
        if stat_input_error is True:
            continue

        dict_[c_name] = stat_list  # adds the list to the dict_ionary with key c_name

        is_wrong_answer = True
        while is_wrong_answer:
            ask = input('Continue? (y/n): ')  # asks if you want to insert another line
            if ask != 'n' and ask != 'y':
                print('ERROR: answer format not supported')
            elif ask == 'n':
                is_wrong_answer = False
                do_repeat = False
            else:
                is_wrong_answer = False
    return dict_


def check_stat_type(stat_list):
    """check that all the statistics are numerical"""
    stat_input_error = False
    for stat in stat_list:
        try:
            # tries to convert the input into float
            # (string type input containing numeric character does not cause errors)
            float(stat)
        except ValueError:   # trows an exception if float(stat) causes an error (non-numerical statistics)
            print('ERROR: one or more of the stats is invalid')
            print('insert only numbers')
            stat_input_error = True  # notification of exception (used to cause the new request for statistics)
            break  # exits the for loop since a non-numeric statistic is not acceptable
    return stat_input_error


def check_len(dict_, index):
    """controls which lines are shorter than index_len and fills in missing spaces with zeros
       (AIM: dictionary with equal-length lines)"""
    index_len = len(index)
    default_value = 0   # value to be replaced in missing spaces
    for row in dict_:
        if len(dict_[row]) < index_len:
            # adds zeroes to lists shorter than the longest one
            dict_[row] = dict_[row] + [default_value for i in range(0, (index_len - len(dict_[row])))]


def set_index():
    """asks if the user wants to change the default names of the stats"""
    is_wrong_answer = True
    index = None    # base state, eventually changed by user
    while is_wrong_answer:
        ask = input('Do you want to input your own stats names? (y/n): ')
        if ask != 'n' and ask != 'y':
            print('ERROR: answer format not supported')
        elif ask == 'n':
            is_wrong_answer = False
        else:
            index = input('Insert stats names separated by spaces '
                          '(the number of stats inserted will determine'
                          ' the number of stats to insert later): ').split()
            is_wrong_answer = False
    return index


def make_dataframe():
    """transforms stats dictionary into DataFrame"""
    index = set_index()
    if index is None:    # if index is not modified uses default index
        index = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']    # default index
    dict_ = make_dict_(index)
    check_len(dict_, index)
    return pd.DataFrame(dict_, index)    # transform dictionary into DataFrame adding a line index


if __name__ == '__main__':
    character_stats = make_dataframe()
    print(character_stats)
