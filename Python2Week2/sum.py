import sys

def main():
    sum= 0.0 #this has to be initialized to 0.0 to handle float inputs
    for i in range(1, len(sys.argv)):
        sum= sum+float(sys.argv[i]) #so it can handle float inputs
    print(sum)
main()

#verified code with this in command line: python sum.py 5.4 4 3 7 9
