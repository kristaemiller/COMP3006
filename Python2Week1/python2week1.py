'''The code below is supposed to do a Fahrenheit to Celsius
temperature conversion (subtract 32 then multiply by 5 over 9). However, it is
producing the wrong answer in its current form. Fix the code so it performs the
calculation correctly.'''
# f = 72
# c = f - (32 * 5) // 9 #added () around 32*5
# print(c)

'''What does the following code segment output:'''
# score = 80
# if score > 90:
#     print("A")
# elif score < 90 and score > 80:
#     print("B")
# elif score < 80 and score > 70:
#     print("C")
# elif score < 70 and score > 60:
#     print("D")
# else:
#     print("F")
#output is "F" because score = 80 is not >80 or <80

'''What does the following code output:'''
# def mystery (x,y):
#     r=1
#     while y>0:
#         if y%2==1:  #5%2==1 so continue
#             r= r*x   #now r is 2
#         y=y//2   #floor division of 5 is 2, now y is 2
#         x=x*x #now x is 4
#     return r
# #
# m= mystery(2,5)
# print (m) #output is 32

'''Fill in the missing lines of code to find and output the smallest
value in the list. The given list, a, is there for testing purposes, but your code
should work for any length list with any numbers in it. You may not change my
code.'''
# a = [4, 2, 6, 3, 5]
# smallest=0
# def smallest(a):
#     for i in range(len(a)):
#       a[i]<a[smallest]
#     smallest=i
#
# print(a[smallest])
#

'''What does the following code output:'''
# def one(x, b):
#     c = []
#     for y in b:
#         c.append([x,y])
#     return c   #returns a single list of ordered pairs
# def two(a, b):
#     c = []
#     for x in a:  #for each element in list a- this for loop runs 3 times, for value 1,2,and 3
#         d = one(x, b)
#         c.extend(d) #extend is like append but it changes the list
#     return c
# print(two([1,2,3],[4,5])) #returns a single list of lists

'''Write a function that takes a list of tuples representing points. 
A point is a pair of numbers representing the x and y coordinates. 
The method should return the distance of the pair of points that have the smallest distance between them.  
Hint: you will want to compare every point to every other point, which often involves a double loop.  
An example call for your :

print(closestDist([(1,2), (4,3), (3,6), (5,7), (0,4)]) # should return 2.236...

You probably want to first write (and test) a distance function 
that takes two point tuples and returns the distance between 
them to use as a helper function.  
Note that Python has a square root function, 
but it is in the math library which you will need to import.  
So you must include the line:

import math

and then you can use the square root function like:

math.sqrt(16)  # returns 4'''

#47 minutes of recording #1
import math
def distFormula(tup1, tup2):
    return math.sqrt((tup2[0]-tup1[0])**2 + (tup2[1]-tup1[1])**2)

def closestDist(listofTuples):
    '''this function takes in a list of tuples representing x, y coordinates,
    and returns the smallest distance between the two tuples'''

    minDist= 99999999 #non-ideal, but assuming the min distance will be less than this number

    for tup1Index in range(len(listofTuples)):
        for tup2Index in range(len(listofTuples)):
            if tup1Index != tup2Index:
                dist= distFormula(listofTuples[tup1Index], listofTuples[tup2Index])
                if dist < minDist:
                    minDist = dist
        return minDist

print(closestDist([(1,2), (4,3), (3,6), (5,7), (0,4)]))








#
# '''This problem involves reading in a file of data and
# computing a few statistics on that data.
# The first thing you will need to do is to create a file
# of data to read.
# You should call this file "scores.txt" and it should
# have the following information in it.
# Note that there should be a "header" line with the names
# of the exams.  Following this first line,
# there should be 1 line of scores for each student
# taking the class (we will not include the names of
# the students in this problem).
# Try to make the file human readable.
# You may use spaces or tabs (\t) to separate each of
# the entires.  Both spaces and tabs are treated as
# whitespace when we process it later.
# You do not need to create this file from Python
# by having it write data, but can simply just type
# in the data in your text favorite code editor
# (Atom/Notepad/etc -- try to avoid editors like MSWord
# as they often add extra things to the file beyond the data)
# and save it with a .txt extension.
#
# exam1    exam2    final
# 87             85              90
# 90             95              89
# 73             81              85
# 98             93              94
# 78             76              82
#
# The next step is to open the file for reading.
# Instead of hard-coding the filename,
# I would like you to ask the user to enter the name of the file.
# If they type in an incorrect filename that doesn't exist,
# then you should tell them about the error and repeatedly
# ask them to keep entering the filename until they get it right.
#
# Hints to open the file: You will have to use exception handling.
#
# Once the file is open, it is now time to read it.
# Note that the way we read from files is line by line.
# However, for the statistics we want to compute later
# (things like mean of exam2), we will want our data organized
# by columns, one for each exam.
# For the file above, we want to produce the following list
# of columns:
#
# [['exam1', 87, 90, 73, 98, 78], ['exam2', 85, 95, 81, 93, 76], ['final', 90, 89, 85, 94, 82]]
#
# Hints to turn rows into columns: Since the first line is
# different than the rest of the lines (header info),
# that line will need to be read first and processed separately.  In particular, you should try and create the initial list of exam names [['exam1'], ['exam2'], ['final']].  After your list of lists is created, you can process each of the remaining lines by simply appending the values onto the correct list.  Recall that the string method split() will form a list of elements from a string, splitting it on whitespace.  Your code should work for any number of exams and any number of students scores for those exams.
#
# Lastly, create a function that will print statistics for
# single exam.  That is, you would call it like:
# printStats(['exam2', 85, 95, 81, 93, 76])
#
# You will call this function for each of the exams columns.
# The function doesn't return anything, but instead prints out
# the min, max, mean, and median in the following format:
#
# exam2 min: 76
# exam2 max: 95
# exam2 mean: 86
# exam2 median: 85
#
# Hints for printing statistics: You may use the min and max
# functions to find the min and max of a list of scores.
# For mean and median, you will have to import the statistics
# module:
#
# import statistics
#
# And then you can call the functions statistics.mean(someList)
# or statistics.median(someList).
#
# Note that the list being passed to this printing function
# contains the name as the 0th item and the scores as the rest
# of the items.'''
#
# #TODO

