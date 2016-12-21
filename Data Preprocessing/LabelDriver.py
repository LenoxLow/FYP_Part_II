import pandas as pd

from pandas import set_option
set_option("display.max.rows", 20)

# Data pre-set
name = "GCW"
be1 = "Good"
be2 = "Good"
be3 = "Good"

# read from vehicle telemetric data set
pathname1 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step II/" + name + "Path1.csv"
vtele = pd.read_csv(pathname1, sep='\t')

vtele['Behaviour'] = be1

output1 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step III/" + name + "Path1.csv"
vtele.to_csv(output1, sep='\t', encoding='utf-8')

# Path 2 Add on Driver Name
pathname2 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step II/" + name + "Path2.csv"
vtele2 = pd.read_csv(pathname2, sep='\t')

vtele2['Behaviour'] = be2

output2 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step III/" + name + "Path2.csv"
vtele2.to_csv(output2, sep='\t', encoding='utf-8')
print(vtele2.tail(1))


# Path 3 Add on Driver Name
pathname3 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step II/" + name + "Path3.csv"
vtele3 = pd.read_csv(pathname3, sep='\t')

vtele3['Behaviour'] = be3

output3 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step III/" + name + "Path3.csv"
vtele3.to_csv(output3, sep='\t', encoding='utf-8')
print(vtele3.tail(1))