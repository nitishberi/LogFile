#! /usr/bin/env python3

import subprocess
import collections
from collections import OrderedDict
import re
import operator
import csv

def error csv():
    errors = {}
    with open("syslog.log", 'r') as file:
        for line in file.readlines():
            val = re.search(r"ERROR\s([\w\s\']*)", line)
            if val:
                val = val.group (1) [:-1]
            if val == None:
                continue
            if val not in errors:
                errors[val] = 1
            else:
                errors[val] = errors.get(val)+1
                
    sorted_errors = OrderedDict(sorted(errors.items(), key=operator.itemgetter(1), reverse=True) )
    with open ("error message.csv", ‘w') as f:
        writer = csv.DictWriter(f, fieldnames =["Error", "Count"])
        writer.writeheader ()
        (f.write("{0},{1}\n". format(key, value)) for key,value in sorted_errors.items()]

return sorted_errors

print (error csv())

def user csv():
    userData = {}
    with open("syslog.log", 'r') as file:
        for line in file.readlines():
            val = line[line. find("(")+1:line.find(")")]
            if val not in userData:
                userData[val] = [0]*2
            if "ERROR" in line:
                errVal = userData.get(val)[1] + 1
                userData[val][1] = errVal
            if "INFO" in line:
                infVal = userData.get(val)[(0] + 1
                userData[val][0] = infVal
    sorted_userData = OrderedDict (sorted(userData.items(), key=operator.itemgetter(0)))
    with open("user_statistics.csv", 'w') as f:
        header = "Username" + "," + "Info" + "," + "Error" + "\n"
        f.write(header)
        for key, value in sorted_userData.items():
            f.write("{0},{1},{2}\n". format (key, value[0],value[1]))

    return sorted_userData

print(user_csv())
