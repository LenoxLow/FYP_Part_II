import pandas as pd
import numpy as np

# to limit the display of rows of data set
from pandas import set_option

set_option("display.max.rows", 20)
# Data pre-set
name = 'KKG'
h = 10
t = 5

# read from vehicle telemetric data set
pathname = '/Users/jiaminglow/Desktop/FYP Part II/Unprocessed Path I Files/torqueTrackLog' + name + '1.csv'
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
print(vtele['Road Structure'].dtype)



# add values to Road Structure column
for index, tele in vtele.iterrows():
    if (tele[' Longitude'] >= 103.3243 and tele[' Latitude'] >= 2.0257 and tele[' Longitude'] <= 103.3249 and
                tele[' Latitude'] <= 2.0264):
       #print(index)
       vtele.set_value(index, 'Road Structure', 'Corner')
    elif (tele[' Longitude'] >= 103.3244 and tele[' Latitude'] >= 2.0234 and tele[' Longitude'] <= 103.3253 and
                tele[' Latitude'] <= 2.0254):
        #print(index)
        vtele.set_value(index, 'Road Structure', 'Curve Road')
    elif (tele[' Longitude'] >= 103.325 and tele[' Latitude'] >= 2.0228 and tele[' Longitude'] <= 103.3265 and
                tele[' Latitude'] <= 2.0232):
        #print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif(tele[' Longitude'] >= 103.3318 and tele[' Latitude'] >= 2.0287 and tele[' Longitude'] <= 103.3325 and
                tele[' Latitude'] <= 2.0295):
        print(index)
        vtele.set_value(index, 'Road Structure', 'Corner')
    elif(tele[' Longitude'] >= 103.3283 and tele[' Latitude'] >= 2.0283 and tele[' Longitude'] <= 103.3291 and
                tele[' Latitude'] <= 2.0289):
        #print(index)
        #print(tele[' Latitude'])
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif(tele[' Longitude'] >= 103.3266 and tele[' Latitude'] >= 2.0305 and tele[' Longitude'] <= 103.3273 and
                tele[' Latitude'] <= 2.0311):
        #print(index)
        vtele.set_value(index, 'Road Structure', 'Intersection')
    elif (tele[' Longitude'] >= 103.3264 and tele[' Latitude'] >= 2.0293 and tele[' Longitude'] <= 103.3268 and
                tele[' Latitude'] <= 2.0301):
        #print(index)
        vtele.set_value(index, 'Road Structure', "Curve Road")
    else:
        vtele.set_value(index, 'Road Structure', "Straight Road")

#print(vtele.sort_values(['Road Structure']))

output = "/Users/jiaminglow/Desktop/FYP Part II/Process Step I/" + name + "Path1.csv"
vtele.to_csv(output, sep='\t', encoding='utf-8')