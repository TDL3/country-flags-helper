#!/usr/bin/env python 

import re
import os

# parse ISO country codes table
codes_dict = {}
with open("iso.txt", "r") as codes:
    country_name_regex = r"^.*\t\t"
    country_code_regex = r"\t\w{2}"
    for line in codes.readlines():
        country_name = re.findall(country_name_regex, line)[0].strip()
        country_code = re.findall(country_code_regex, line)[0].strip()
        codes_dict[country_code] = country_name

# Convert country names to capitalized names
# For instance, UNITED STATES OF AMERICA --> United States of America
for key, value in codes_dict.items():
    elements = value.split()
    capitalized_name = ""
    for e in elements:
        if e == "AND":
            e = "and"
        elif e == "OF":
            e = "of"
        else:
            e = e.capitalize()
        capitalized_name += e + " "
    codes_dict[key] = capitalized_name

# Rename
flag_path = "./svg/"
flags = [f for f in os.listdir(flag_path) if os.path.isfile(os.path.join(flag_path, f))]
for flag in flags:
    country_code = flag.split(".")[0].upper()
    new_name = codes_dict[country_code] + " " + country_code + ".svg"
    os.rename(flag_path + flag, flag_path + new_name)
    print("Renamed: " + flag + " --> " + new_name)
    