#!/usr/bin/env python3
## Max Roschke
## Data Science 2, Project 02, Counting Characters -- Reference Implementation
import sys
import string

## function to do the counting
def add_frequencies(d, f, remove_case):
   '''Adds the character frequencies of the given text file to the given
   dictionary.

   Arguments:
      d (dict): map from characters (str) to frequency counts (int)
      f (file): text file to read characters from
      remove_case (bool): if true, runs .lower() on chars before mapping
   '''
   ## iterate through the file, char-by-char
   for line in f:
      line = line.strip('\n')
      for c in line:
         ## convert c to key (use 'remove_case' to check for lower-casing)
         key = c.lower() if remove_case else c

         ## increment that char in the dictionary
         if key in d:
            d[key] += 1
         else:
            d[key] = 1

   ## return that dictionary (unnecessary, but matches intuition when calling)
   return d

## main function
def main():
   '''Prints out the frequencies of various characters in input files. Uses
   sys.argv to determine what those characters are, and which input files to
   read from.'''
   ## default settings
   output_chars = string.ascii_letters
   remove_case = True
   print_zeroes = False
   inOutput = False

   ## get "real arguments".  that is, ignore the script name
   args = sys.argv[1:]

   ## process the leading flags
   while args and args[0].startswith('-'):
      ## remove the next flag from the list
      arg = args.pop(0)

      ## handle that flag
      if arg == '-c':
         remove_case = False
      elif arg == '-l':
         inOutput = True
         output_chars = args.pop(0)
      elif arg == '-z':
         print_zeroes = True
      elif arg == '--':
         break
      else:
         ## unknown argument!
         print(f'unknown argument: \'{arg}\'', file=sys.stderr)

   ## if we have to remove the case, remove it from the output_chars first!
   if remove_case:
      output_chars = ''.join(c for c in output_chars if c.islower())

   ## the remaining arguments must all be files... process them!
   d = {}

   for filename in args:
      if filename.endswith(".txt"):
         with open(filename, 'r') as f:
            add_frequencies(d, f, remove_case)

#need to carry out the data of the dictionary from count.py to
#count_to_csv.py.  Therefore, need to filter/modify the data in
#the dictionary based on the argument on the command line before
#returning it
   d_temp = d.copy()
   for i in d_temp.keys():
         if i == ' ':
            del d[i]
            break
#for example, for argument -l, we need to remove all entries
#after the -l option.  Therefore, iterate through the keys
#in temp keys, and remove key that is not in the list "output_chars":

   if inOutput:
      for i in d_temp.keys():
         if i not in output_chars:
            del d[i]

   if print_zeroes:
      for c in output_chars:
         d[c] = d[c] if c in d else 0

   return d

## when to run the main function
if __name__ == '__main__':
   main()
