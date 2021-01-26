import sys

def main():
    for i in range(1,len(sys.argv)):
        name= sys.argv[i]
        if '-n' in sys.argv:
            print(name)
        if name != '-n':
            file= open(str(name), mode= 'r', encoding= 'ASCII')
            print(file.read())
main()
