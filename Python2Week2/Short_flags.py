import sys

def main():
    flags= ''
    reverse= False
    for i in range (1, len(sys.argv)):
        if sys.argv[i]== '-r':
            reverse= True
        elif '-' in sys.argv[i]:
            flags += str(sys.argv[i][1:])

    if reverse:
        print(flags[-1:])
    else:
        print(flags)
main()
