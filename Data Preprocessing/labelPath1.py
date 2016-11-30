import pandas as pd
import numpy as np

# to limit the display of rows of data set
from pandas import set_option

set_option("display.max.rows", 20)

# read from vehicle telemetric data set
vtele = pd.read_csv('/Users/jiaminglow/Desktop/FYP Part II/Unprocessed Path I Files/torqueTrackLogCZC1.csv')

# delete the extra columns in the data set
if len(vtele.columns) > 18:
    count = len(vtele.columns) - 18
    for i in range(18, len(vtele.columns)):
        vtele.drop(vtele.columns[[18]], axis=1, inplace=True)


# delete the first h rows from data set
h = 0
print(len(vtele.index))
for j in range(0, h):
   vtele.drop(vtele.head(1).index, axis=0, inplace=True)
   vtele.reset_index(drop=True)

# delete the last t rows from data set
# t = 0
# for k in range(0, t):
#    vtele.drop(vtele.head(1).index, axis=0, inplace=True)
#    vtele.reset_index(drop=True)

# add Road Structure column to Data Frame
vtele['Road Structure'] = "empty"
print(vtele['Road Structure'].dtype)



# add values to Road Structure column
for index, tele in vtele.iterrows():
    if (tele[' Longitude'] <= 103.32459 and tele[' Longitude'] >= 103.3244 and
        tele[' Latitude'] <= 2.02621 and tele[' Latitude'] >= 2.0259):
       print(index)
       vtele.set_value(index, 'Road Structure', 'Corner')
    elif (tele[' Longitude'] <= 103.32516 and tele[' Longitude'] >= 103.3245 and tele[' Latitude'] <= 2.02571 and
                tele[' Latitude'] >= 2.02363):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Curve Road')
    elif (tele[' Longitude'] <= 103.32592 and tele[' Longitude'] >= 103.32569 and tele[' Latitude'] <= 2.0231 and
                tele[' Latitude'] >= 2.023):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif(tele[' Longitude'] <= 103.33255 and tele[' Longitude'] >= 103.33206 and tele[' Latitude'] <= 2.02932 and
                tele[' Latitude'] >= 2.02901):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Corner')
    elif(tele[' Longitude'] <= 103.329092 and tele[' Longitude'] >= 103.32874 and tele[' Latitude'] <= 2.028515 and
                tele[' Latitude'] >= 2.02838):
        print(index)
        print(tele[' Latitude'])
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif(tele[' Longitude'] >= 103.32699 and tele[' Latitude'] >= 2.03074 and tele[' Longitude'] <= 103.32722 and
                tele[' Latitude'] <= 2.030815):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif (tele[' Longitude'] >= 103.32639 and tele[' Latitude'] >= 2.0289 and tele[' Longitude'] <= 103.32649 and
                tele[' Latitude'] <= 2.02932):
        print(index)
        vtele.set_value(index, 'Road Structure', "Curve Road")
    else:
        vtele.set_value(index, 'Road Structure', "Straight Road")

#print(vtele.sort_values(['Road Structure']))

vtele.to_csv("/Users/jiaminglow/Desktop/FYP Part II/Process Step I/CZCPath1.csv", sep='\t', encoding='utf-8')