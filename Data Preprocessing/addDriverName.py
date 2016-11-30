import pandas as pd

# to limit the display of rows of data set
from pandas import set_option

set_option("display.max.rows", 20)

# Data pre-set
name = "TWT"
fullname = "Tan Wee Ther"

# read from vehicle telemetric data set
pathname1 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step I/" + name + "Path1.csv"
vtele = pd.read_csv(pathname1, sep='\t')

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

vtele3['Driver Name'] = fullname

output3 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step II/" + name + "Path3.csv"
vtele3.to_csv(output3, sep='\t', encoding='utf-8')
print(vtele3.tail(1))
