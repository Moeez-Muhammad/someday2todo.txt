import os
import argparse
import datetime

todaydate = datetime.datetime.today().strftime('%Y-%m-%d')
todofolder = "%USERPROFILE%\\todo"

todo = todofolder + '\\todo.txt'
someday = todofolder + '\\someday.txt'
somedaycopy = todofolder + '\\somedaycopy.txt'
string = 'redirect:'
with open(todo, 'a+') as outfile, open(someday, 'r+') as infile, open(somedaycopy, 'a+') as someday2:
    for line in infile: # iterate over lines
        if string in line: # see if line has a redirect date
            date = line[line.index(string) + len(string):] # get the date from the line
            if date == todaydate: # if the date is today
                task = line.split(string)[0] # get the task
                outfile.write(date, task + '\n') # write the task with the date at the front as a creation date
            else:
                someday2.write(line) # if it is not today's date, write to someday2
        else:
            someday2.write(line) # if there is no redirect date, write to someday2

# remove old someday.txt and make somedaycopy the new someday.txt
if os.path.exists(someday):
    os.remove(someday)
    if os.path.exists(somedaycopy):
        os.rename(somedaycopy, someday)
                

