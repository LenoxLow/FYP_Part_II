import pandas as pd

from pandas import set_option

set_option("display.max.rows", 20)

# Data pre-set 1)GCW 2)LJM 3)KKG 4)LHS 5)CZC 6)NJB 7)KMH 8)OYC 9)NSK 10)TWT 11)CFN
name = "CFN"

# variables
road = 0

# Path 1 Overspeeding Script
# read from vehicle telemetric data set
pathname1 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step III/" + name + "Path1.csv"
vtele = pd.read_csv(pathname1, sep='\t')

vtele['Overspeeding'] = 0
vtele['Overspeeding'] = vtele['Overspeeding'].apply(pd.to_numeric)

print(vtele['Overspeeding'].dtype)

for index, tele in vtele.iterrows():

    if (tele['Road Structure'] == "Straight Road"):
        road = 60
    elif (tele['Road Structure'] == "Curve Road"):
        road = 40
    elif (tele['Road Structure'] == "Corner"):
        road = 35
    elif (tele['Road Structure'] == "Intersection"):
        road = 30
    elif (tele['Road Structure'] == "Traffic Light Intersection"):
        road = 35

    if (tele['Speed (GPS)(km/h)'] > road):
        vtele.iloc[index, vtele.columns.get_loc('Overspeeding')] = 1
        # vtele.set_value(index, 'Overspeeding', 1)
    else:
        vtele.iloc[index, vtele.columns.get_loc('Overspeeding')] = 0
        # vtele.set_value(index, 'Overspeeding', 0)

output = "/Users/jiaminglow/Desktop/FYP Part II/Process Step IV/" + name + "Path1.csv"
vtele.to_csv(output, sep='\t', encoding='utf-8')

#####################################################################################

# Path 2 Overspeeding Script
# read from vehicle telemetric data set
pathname2 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step III/" + name + "Path2.csv"
vtele2 = pd.read_csv(pathname2, sep='\t')

vtele2['Overspeeding'] = 0
vtele2['Overspeeding'] = vtele2['Overspeeding'].apply(pd.to_numeric)

for index2, tele2 in vtele2.iterrows():

    if (tele2['Road Structure'] == "Straight Road"):
        road = 60
    elif (tele2['Road Structure'] == "Curve Road"):
        road = 40
    elif (tele2['Road Structure'] == "Corner"):
        road = 35
    elif (tele2['Road Structure'] == "Intersection"):
        road = 30
    elif (tele2['Road Structure'] == "Traffic Light Intersection"):
        road = 35

    if (tele2['Speed (GPS)(km/h)'] > road):
        vtele2.iloc[index2, vtele2.columns.get_loc('Overspeeding')] = 1
    else:
        vtele2.iloc[index2, vtele2.columns.get_loc('Overspeeding')] = 0

output2 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step IV/" + name + "Path2.csv"
vtele2.to_csv(output2, sep='\t', encoding='utf-8')


#####################################################################################

# Path 3 Overspeeding Script
# read from vehicle telemetric data set
pathname3 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step III/" + name + "Path3.csv"
vtele3 = pd.read_csv(pathname3, sep='\t')

vtele3['Overspeeding'] = 0
vtele3['Overspeeding'] = vtele3['Overspeeding'].apply(pd.to_numeric)

for index3, tele3 in vtele3.iterrows():

    if (tele3['Road Structure'] == "Straight Road"):
        road = 60
    elif (tele3['Road Structure'] == "Curve Road"):
        road = 40
    elif (tele3['Road Structure'] == "Corner"):
        road = 35
    elif (tele3['Road Structure'] == "Intersection"):
        road = 30
    elif (tele3['Road Structure'] == "Traffic Light Intersection"):
        road = 35


    if (tele3['Speed (GPS)(km/h)'] > road):
        vtele3.iloc[index3, vtele3.columns.get_loc('Overspeeding')] = 1
    else:
        vtele3.iloc[index3, vtele3.columns.get_loc('Overspeeding')] = 0

output3 = "/Users/jiaminglow/Desktop/FYP Part II/Process Step IV/" + name + "Path3.csv"
vtele3.to_csv(output3, sep='\t', encoding='utf-8')

print(name)