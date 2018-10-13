import os
import argparse
import sys

def create_attr_list(dictionary):
    return [ value for key, value in dictionary.items()]

parser = argparse.ArgumentParser(prog='someday2todo.txt')
parser.add_argument("--folder", help="The folder that todo and someday are both in. Leave blank if they are in different locations")
parser.add_argument("todo", help="The name of the todo file. Input full path if --folder is blank.")
parser.add_argument("someday", help="The name of the someday file. Input full path if --folder is blank.")
parser.add_argument("--locatorstring", help="The string used to find where the date is to move the task. Defaults to 'redirect:'", default="redirect:")
args = parser.parse_args()
print(args)

script = os.path.realpath(__file__)
scriptlocation = os.path.dirname(script)
executable = sys.executable
batchlocation = os.path.join(scriptlocation, 'someday2todo.bat')

with open(batchlocation, 'w+') as batchfile:
    batchfile.write('@echo off' + '\n' + 'python ' + script)
command = "schtasks /Create /SC DAILY /TN Someday2todo /TR " + batchlocation +  " /ST 00:00"
# o = os.popen(command).read()
# print(o)
os.system(command)  

with open('settings.txt', 'w+') as settingsfile:
    settings = create_attr_list(vars(args))
    settingsfile.writelines('\n'.join(settings))





