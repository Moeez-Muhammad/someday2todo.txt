import os
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        return False

scriptlocation = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(scriptlocation, 'settings.txt'), 'r') as settings:
    lines = settings.readlines()
    todofolder = lines[0].rstrip()
    todo = os.path.join(todofolder, lines[1].rstrip())
    someday = os.path.join(todofolder, lines[2].rstrip())
    somedaycopy = os.path.join(todofolder, lines[2].rstrip()[:-4] + 'copy' + '.txt')
    locatorstring = lines[3].rstrip()

todaydate = datetime.datetime.today().strftime('%Y-%m-%d')

with open(todo, 'a+') as outfile, open(someday, 'r+') as infile, open(somedaycopy, 'a+') as someday2:
    for line in infile: # iterate over lines
        if locatorstring in line: # see if line has a redirect date
            redirectdate = line[line.index(locatorstring) + len(locatorstring):].rstrip() # get the date from the line
            if redirectdate == todaydate: # if the date is today
                task = line.split(locatorstring)[0] # get the task
                if validate(line[:9]) == False:
                    outfile.write(redirectdate + task + '\n') # write the task with the date at the front as a creation date
                else:
                    outfile.write(task + '\n')
            else:
                someday2.write(line) # if it is not today's date, write to someday2
        else:
            someday2.write(line) # if there is no redirect date, write to someday2

# remove old someday.txt and make somedaycopy the new someday.txt
if os.path.exists(someday):
    os.remove(someday)
    if os.path.exists(somedaycopy):
        os.rename(somedaycopy, someday)
                

