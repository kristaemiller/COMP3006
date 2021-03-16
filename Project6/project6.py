#Krista Miller
#COMP 3006

import random
import numpy as np
import pandas as pd

#Part 1 File Generation:
b = []

for i in range(10000):
    r = random.randint(1, 50)
    b.append(r)

na = np.array(b).reshape(1000, 10)
panda_df = pd.DataFrame(data=na, columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
pd.DataFrame(na).to_csv("proj6.csv", header=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])

#Part 2 Loading in a file via Pandas:
nuggets = pd.read_csv("DENVER NUGGETS PRESEASON STATS.csv")
threerows = pd.read_csv("DENVER NUGGETS PRESEASON STATS.csv", nrows=3)
trows = threerows.replace('\n', ' ', regex=True)
data = nuggets.replace('\n', ' ', regex=True)
nuggets_list = list(data.columns)

#Part 3 Statistics:
maxnug = nuggets[data.columns[1:16]].max()
meannug = nuggets[data.columns[1:16]].mean()
stdnug = nuggets[nuggets.columns[1:16]].std()

# Part 4 Generate Summary File:
f = open("summary.txt", "w")
f.write(f'statistics summary: \n')
f.write(f'\ncolumn headers: \n{str(nuggets_list)} \n')
f.write(f'\nfirst three rows of data: \n{trows} \n')
f.write(f'\nmax values for each column= \n{str(maxnug)} \n')
f.write(f'\nmean values for each column= \n{str(meannug)} \n')
f.write(f'\nstandard deviation values for each column= \n{str(stdnug)}')
f.close()
