import pandas as pd
import numpy as np

# to limit the display of rows of data set
from pandas import set_option

set_option("display.max.rows", 20)

# Data pre-set
name = 'CFN'
h = 5
t = 0

# read from vehicle telemetric data set
pathname = '/Users/jiaminglow/Desktop/FYP Part II/Unprocessed Path I Files/torqueTrackLog' + name + '3.csv'
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
    if (tele[' Longitude'] >= 103.3219 and tele[' Latitude'] >= 2.0303 and tele[' Longitude'] <= 103.3224 and
                tele[' Latitude'] <= 2.0307):
       print(index)
       vtele.set_value(index, 'Road Structure', 'Intersection')
    elif (tele[' Longitude'] >= 103.3214 and tele[' Latitude'] >= 2.0307 and tele[' Longitude'] <= 103.3221 and
                tele[' Latitude'] <= 2.0312 and index < 100):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif (tele[' Longitude'] >= 103.3199 and tele[' Latitude'] >= 2.0303 and tele[' Longitude'] <= 103.3205 and
                tele[' Latitude'] <= 2.0308 ):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif (tele[' Longitude'] >= 103.3206 and tele[' Latitude'] >= 2.0305 and tele[' Longitude'] <= 103.321 and
                  tele[' Latitude'] <= 2.0309):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Traffic Light Intersection')
    elif(tele[' Longitude'] >= 103.3195 and tele[' Latitude'] >= 2.0322 and tele[' Longitude'] <= 103.3198 and
                tele[' Latitude'] <= 2.0327):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Corner')
    elif (tele[' Longitude'] >= 103.3197 and tele[' Latitude'] >= 2.0324 and tele[' Longitude'] <= 103.3202 and
                  tele[' Latitude'] <= 2.0328):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif(tele[' Longitude'] >= 103.3205 and tele[' Latitude'] >= 2.0308 and tele[' Longitude'] <= 103.321 and
                tele[' Latitude'] <= 2.0312):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Traffic Light Intersection')
    elif (tele[' Longitude'] >= 103.3268 and tele[' Latitude'] >= 2.0329 and tele[' Longitude'] <= 103.3278 and
              tele[' Latitude'] <= 2.0338):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Roundabout')
    elif (tele[' Longitude'] >= 103.3233 and tele[' Latitude'] >= 2.0314 and tele[' Longitude'] <= 103.3236 and
              tele[' Latitude'] <= 2.0319 and index > 600):
        print("Corner")
        print(index)
        vtele.set_value(index, 'Road Structure', 'Corner')
    elif (tele[' Longitude'] >= 103.3234 and tele[' Latitude'] >= 2.0308 and tele[' Longitude'] <= 103.3238 and
              tele[' Latitude'] <= 2.0314):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    else:
        vtele.set_value(index, 'Road Structure', "Straight Road")

#print(vtele.sort_values(['Road Structure']))

output = "/Users/jiaminglow/Desktop/FYP Part II/Process Step I/" + name + "Path3.csv"
vtele.to_csv(output, sep='\t', encoding='utf-8')