import pandas as pd
import numpy as np

# to limit the display of rows of data set
from pandas import set_option

set_option("display.max.rows", 20)

# Data pre-set
name = 'GCW'
h = 10
t = 10

# read from vehicle telemetric data set
pathname = '/Users/jiaminglow/Desktop/FYP Part II/Unprocessed Path I Files/torqueTrackLog' + name + '2.csv'
vtele = pd.read_csv(pathname)

# delete the extra columns in the data set
if len(vtele.columns) > 18:
    count = len(vtele.columns) - 18
    for i in range(18, len(vtele.columns)):
        vtele.drop(vtele.columns[[18]], axis=1, inplace=True)


# delete the first h rows from data set
print(len(vtele.index))
for j in range(0, h):
   vtele.drop(vtele.head(1).index, axis=0, inplace=True)
   vtele.reset_index(drop=True)

# delete the last t rows from data set
for k in range(0, t):
   vtele.drop(vtele.tail(1).index, axis=0, inplace=True)
   vtele.reset_index(drop=True)

# add Road Structure column to Data Frame
vtele['Road Structure'] = "empty"
# print(vtele['Road Structure'].dtype)



# add values to Road Structure column
for index, tele in vtele.iterrows():
    if (tele[' Longitude'] >= 103.3268 and tele[' Latitude'] >= 2.0327 and tele[' Longitude'] <= 103.3275 and
                tele[' Latitude'] <= 2.0332):
       print(index)
       vtele.set_value(index, 'Road Structure', 'Roundabout')
    elif (tele[' Longitude'] >= 103.3216 and tele[' Latitude'] >= 2.0308 and tele[' Longitude'] <= 103.3220 and
                tele[' Latitude'] <= 2.0312):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Corner')
    elif (tele[' Longitude'] >= 103.3218 and tele[' Latitude'] >= 2.0304 and tele[' Longitude'] <= 103.32214 and
                tele[' Latitude'] <= 2.0306):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif(tele[' Longitude'] >= 103.3234 and tele[' Latitude'] >= 2.0309 and tele[' Longitude'] <= 103.3238 and
                tele[' Latitude'] <= 2.0312):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif (tele[' Longitude'] >= 103.3239 and tele[' Latitude'] >= 2.0298 and tele[' Longitude'] <= 103.3250 and
                  tele[' Latitude'] <= 2.0305):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Curve Road')
    elif(tele[' Longitude'] >= 103.3266 and tele[' Latitude'] >= 2.0298 and tele[' Longitude'] <= 103.3269 and
                tele[' Latitude'] <= 2.0301 and index > 100):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    else:
        vtele.set_value(index, 'Road Structure', "Straight Road")

#print(vtele.sort_values(['Road Structure']))

output = "/Users/jiaminglow/Desktop/FYP Part II/Process Step I/" + name + "Path2.csv"
vtele.to_csv(output, sep='\t', encoding='utf-8')