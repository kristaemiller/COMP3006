# Krista Miller
# Student ID: 873554131
# Program description: This script will implement two functions that count
# frequencies of characters in a text file.

import sys

def add_frequencies(d, file, remove_case):
    '''This function takes in three parameters: a dictionary
    d, a file object file, and a boolean remove_case.  The dictionary
    maps characters to frequencies. The function adds the frequency
    counts of the characters in the file to the dictionary d.
    If remove case is false, then each character is the key into the dictionary.
    If remove case is true, then the lowercase of each character is the key into
    the dictionary.'''

    # open file and read lines:
    with open(file) as f:
        content = f.readlines()

    # read characters in each line and add to a dictionary
        for line in content:
            for char in line:
                if remove_case == True:  # checks the content of remove_case
                    if char in d:
                        d[char] += 1
                    else:
                        if char != '\n' and char != ' ':
                            d[char] = 1  # adds new character to the dictionary
                else:  # if remove_case is True, convert characters to lower
                    low = char.lower()
                    if low in d:
                        d[low] += 1
                    else:
                        if low != '\n' and low != ' ':
                            d[low] = 1


def main():
    '''this function handles parsing the arguments, and calling add_frequencies(...)
    It parses the command line arguments -c, -l, -z; creates
    an empty dictionary, adds the frequencies for each file in the
    argument list to that dictionary, and prints out the elements
    of that dictionary in CSV format.'''

    d = {}  # creates empty dictionary
    cmdLineArgs = sys.argv  # returns a list of command line arguments

    if '-c' in cmdLineArgs:
        # -c: an optional flag that distinguishes between upper and lower case.
        # For example, the file 'aA' would count one 'a' and one 'A
        files = cmdLineArgs[2:]
        for file in files:
            add_frequencies(d, file, True)

    if '-l' in cmdLineArgs:
        # -l: an optional flag with an argument, that only prints out the frequencies
        # of the characters in the argument letters. For example, '-l aeiou' counts only vowels.
        specialChars = cmdLineArgs[2]
        # specialChars = 'aeiou'
        files = cmdLineArgs[3:]
        for file in files:
            add_frequencies(d, file, False)

        d_2 = {}
        for char in d:
            if char in specialChars:
                d_2[char] = d[char]
        d = d_2

    if '-z' in cmdLineArgs:
        # -z: : an optional flag that prints a row for every character, even when it occurs zero times.
        files = cmdLineArgs[2:]
        for file in files:
            add_frequencies(d, file, False)
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for letter in alpha:
            if letter not in d:
                d[letter] = 0  # assigns 0 if letter not present

    with open('Me.txt', 'w') as f:  # write a text file with letters and frequencies
        for letter in d:
            freq = d[letter]
            f.write(letter + ',' + str(freq) + '\n')  # ',' separates into CSV format '\n' gives new line for each character

main()
