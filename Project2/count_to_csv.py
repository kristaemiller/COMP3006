#!/usr/bin/env python3
## Krista Miller
## Data Science 2, Project 02, Counting Characters -- Reference Implementation
import count as c
import sys
import csv

d = c.main()
args = sys.argv
CSV_name = None
for a in args:
	if a.endswith(".csv"):
		CSV_name = a
l=list(d.items())
with open(CSV_name, "w", encoding='utf8', newline="") as csvfile:
   writer = csv.writer(csvfile)
   writer.writerows(l)

