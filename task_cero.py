# Task 0
from pandas.io.json import json_normalize
import json
import pandas as pd


# 1
neos = pd.read_csv(
    "/Users/mikhaildiazandrade/Documents/Courses/Udacity/Intermediate_Python/nd303-c1-advanced-python-techniques-project-starter/data/neos.csv")
print("How many NEOs are in the `neos.csv` data set", neos.shape[0])
print("\n")

n = 5
for val in neos:
    n -= 1
    if n == 0:
        break
    print(val)

# 2
pdes = neos['pdes'].iloc[0]
print("What is the primary designation of the first Near Earth Object in the neos.csv data set", pdes)
print("\n")

# 3
apollo = neos[neos["name"] == "Apollo"]
apollo = apollo["diameter"].iloc[0]
print("What is the diameter of the NEO whose name is Apollo?", apollo, "kilometers")
print("\n")

# 4
iau = neos["name"].count()
print("How many NEOs have IAU names in the data set?", iau)
print("\n")

# 5
diameters = neos["diameter"].count()
print("How many NEOs have diameters in the data set?", diameters)
print("\n")

# 6
with open("/Users/mikhaildiazandrade/Documents/Courses/Udacity/Intermediate_Python/nd303-c1-advanced-python-techniques-project-starter/data/cad.json", "r") as read_file:
    json_ = json.load(read_file)
json_len = len(json_["data"])
print("How many close approaches are in the `cad.json` data set?", json_len)
print("\n")

# 7
new_df = pd.DataFrame.from_records(json_['data'])
new_df.columns = ["des", "orbit_id", "jd", "cd", "dist",
                  "dist_min", "dist_max", "v_rel", "v_inf", "t_sigma_f", "h"]
close_neo = new_df[new_df['cd'].str.match('2000-Jan-01')]
close_neo = close_neo[close_neo["des"] == "2015 CL"]
neo = close_neo["dist"].min()
print("On January 1st, 2000, how close did the NEO whose primary designation is 2015 CL pass by Earth?", neo)
print("\n")

# 8
close_neo2 = new_df[new_df['cd'].str.match('2000-Jan-01')]
close_neo2 = close_neo2[close_neo2["des"] == "2002 PB"]
neo2 = close_neo2["v_rel"].values[0]
print("On January 1st, 2000, how fast did the NEO whose primary designation is 2002 PB pass by Earth?,", neo2)
