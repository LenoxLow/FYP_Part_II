import pandas as pd

# to limit the display of rows of data set
from pandas import set_option

set_option("display.max.rows", 20)

# Data pre-set
name = "OYC"
h1 = 0
h3 = 5
fullname = "Ooi Yong Cheng"

# read from vehicle telemetric data set
pathname1 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step I/" + name + "Path1.csv"
vtele = pd.read_csv(pathname1, sep='\t')


# delete the first h rows from data set
print(len(vtele.index))
for j in range(0, h1):
   vtele.drop(vtele.head(1).index, axis=0, inplace=True)
   vtele.reset_index(drop=True)

vtele['Driver Name'] = fullname

output1 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step II/" + name + "Path1.csv"
vtele.to_csv(output1, sep='\t', encoding='utf-8')
print(vtele.tail(1))

# Path 2 Add on Driver Name
pathname2 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step I/" + name + "Path2.csv"
vtele2 = pd.read_csv(pathname2, sep='\t')

vtele2['Driver Name'] = fullname

output2 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step II/" + name + "Path2.csv"
vtele2.to_csv(output2, sep='\t', encoding='utf-8')
print(vtele2.tail(1))


# Path 3 Add on Driver Name
pathname3 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step I/" + name + "Path3.csv"
vtele3 = pd.read_csv(pathname3, sep='\t')

print(len(vtele3.index))
for j in range(0, h3):
   vtele3.drop(vtele3.head(1).index, axis=0, inplace=True)
   vtele3.reset_index(drop=True)

vtele3['Driver Name'] = fullname

output3 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step II/" + name + "Path3.csv"
vtele3.to_csv(output3, sep='\t', encoding='utf-8')
print(vtele3.tail(1))
