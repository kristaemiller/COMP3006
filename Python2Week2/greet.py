import sys
#sys gives us access to various system details

def main():
    #sys.argv is a list containing the arguments given to
    #our script
    vals= []
    for val in sys.argv:
        vals.append(val)
    print(vals)
    punctuation= ''
    if '-q' in vals:
        punctuation = '?'
    elif '-Q' in vals:
        punctuation = '!?'
    else:
        punctuation = '!'

    if '-n' in vals:
        flagIndex= vals.index('-n')
        num= vals[flagIndex +1]

        print(f'Hello, {vals[-1]}{punctuation*int(num)}')
    else:
        print(f'Hello, {vals[-1]}{punctuation}')

main()

#tested with this in the command >python greet.py -Q -n 5  krista

