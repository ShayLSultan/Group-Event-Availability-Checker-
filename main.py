import csv 
from datetime import datetime

with open("member_availability.csv") as mem_avail_csv_file:
    mem_avail_dict = csv.DictReader(mem_avail_csv_file)
    date_list = []
    for row in mem_avail_dict: 
        date_list.append(row["Available Date 1"])
        date_list.append(row["Available Date 2"])
date_dict = {}
for i in date_list:
    if i in date_dict.keys():
        date_dict[i] += 1
    else:
        date_dict[i] = 1
print("The best date for the majority of members is...")
print(max(date_dict, key=date_dict.get))

