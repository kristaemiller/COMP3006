def main():
    tab= table(10)
    print('    |    1   2   3   4   5   6   7   8   9   10')
    print('----+------------------------------------------')
    for row in tab:
        print(f'    {row[0]}  |', end='\t')
        for val in row:
            print(val, end= '\t')
        print()

def table(n):
    rows=[]
    for i in range(1, n+1):
        col= []
        for j in range(1, n+1):
            col.append(j*i)
        rows.append(col)
    return rows
main()
