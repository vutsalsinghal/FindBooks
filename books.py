############################################################################################
# -FindBooks-
#
# Tool which shows a list of books in alphabetical ascending by author's last name
#
# Author: Vutsal Singhal <vutsalsinghal@{gmail.com/nyu.edu}>
#
# last updated: Tue Apr 04 2018 01:51:15 EDT
# compiler   : GCC 5.4.0 20160609
# system     : Linux     release: 4.13.0-38-generic
# machine    : x86_64
# processor  : x86_64
# CPU cores  : 8
# interpreter: 64bit

# Python     : 3.5.2 (default, Nov 23 2017, 16:37:01)
#############################################################################################

# Import libraries
import os
import argparse

# Collect command-line arguments
ap = argparse.ArgumentParser(
    description="Tool which shows a list of books in alphabetical ascending by author's last name")
ap.add_argument("--filter", required=False,
                help="Show a subset of books, looks for the argument as a substring of any of the fields")
ap.add_argument("--year", action='store_true', required=False,
                help="sort the books by year, ascending instead of default sort")
ap.add_argument("--reverse", action='store_true',
                required=False, help="reverse sort")
ap.add_argument('--version', action='version', version='v.1.0.0')
args = vars(ap.parse_args())

output = []
# Can add other types if required
valid_fileTypes = {'csv': ',', 'pipe': '|', 'slash': '/'}


def genralForm(fType, lines, valid_fileTypes):
    for line in map(lambda x: [x.strip() for x in x.split(valid_fileTypes[fType])], lines):
        if fType == 'csv':
            output.append([x for _, x in sorted(zip([2, 0, 1, 3], line))])
        elif fType == 'pipe':
            output.append([x for _, x in sorted(zip([1, 0, 2, 3], line))])
        elif fType == 'slash':
            output.append([x for _, x in sorted(zip([3, 1, 0, 2], line))])


for fName in [x for x in os.listdir(os.getcwd()) if x in valid_fileTypes]:
    f = open(fName, 'r')
    lines = f.readlines()
    genralForm(fName, lines, valid_fileTypes)

if args['filter'] != None:
    filterElement = args['filter']
    for line in sorted(output, key=lambda x: x[0] if not args['year'] else x[3], reverse=args['reverse']):
        if any([True for x in line if filterElement in x]):
            print(', '.join(line))
else:
    for line in sorted(output, key=lambda x: x[0] if not args['year'] else x[3], reverse=args['reverse']):
        print(', '.join(line))