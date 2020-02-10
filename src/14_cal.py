"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

 # debug
arguments = len(sys.argv) - 1
for i in sys.argv:
    print (i)
print ("the script is called with %i arguments" % (arguments))
#debug
#going to assume first sys argv is always the name of the file being run




date =datetime.now()
month= date.month
year = date.year
if (arguments==0):
    print("no args supplied, using system values")
if (arguments==1):
    if(sys.argv[1].isnumeric()):
        print(f"{sys.argv[1]}first arg is numeric")
        month = sys.argv[1]
    else:
        print("non-numeric value supplied, please provide the months numeral value i.e 1-12 with no leading 0")
elif (arguments==2):
    if(sys.argv[2].isnumeric() & sys.argv[1].isnumeric()):
        print(f"{sys.argv[1]} first arg is numeric \n{sys.argv[2]} second arg is numeric")
        month = sys.argv[1]
        year = sys.argv[2]
    else:
        print("non-numeric value supplied, please provide the months numeral value i.e 1-12 with no leading 0 and the 4 digit year")


print(f"month = {month}")
print(f"year = {year}")

def printCal(month=month, year=year):
    cal = calendar.TextCalendar(calendar.MONDAY)
    printStr = cal.formatmonth(year,month)
    print(printStr)

printCal(int(month),int(year))


## the error checking could be better, lots of this could be more eloquent, but it's functional more or less now.
