#!/usr/bin/env python3

import os

def non_bold(string):
    return string.replace("**", "")


def h4toh3(string):
    return string.replace("####", "###")


def remove_none_from_extra_field(string):
    if string[:6] == "None. ":
        return string[6:]
    elif string[:8] == "**None. ":
        return "**"+string[8:]
    else:
        return string

def cursive_extra_fields(string):
    if string.startswith("Alert!"):
        return "*Alert!* "+string[7:]
    elif string.startswith("Tip!"):
        return "*Tip!*"+string[4:]
    # Make it work if non_bold is not used
    elif string.startswith("**Alert!"):
        return "***Alert!* "+string[9:]
    elif string.startswith("Tip!"):
        return "***Tip!*"+string[6:]
    else:
        return string


def main():
    for filename in os.listdir('src'):
        os.makedirs(os.path.dirname("dst/"+filename), exist_ok=True)
        with open("src/"+filename, "r") as f_in:
            lines = f_in.readlines()
            f_out = open("dst/"+filename, "w")

            for i, line in enumerate(lines):

                # Remove credits in the beginning and end
                if "Made" in line and "with Scribe": 
                    continue

                new_line = line 
                new_line = non_bold(new_line)
                new_line = h4toh3(new_line)
                new_line = remove_none_from_extra_field(new_line)
                new_line = cursive_extra_fields(new_line)
                f_out.write(new_line)
        f_out.close()

if __name__ == "__main__":
    main()