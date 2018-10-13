import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--folder", help="The folder that todo and someday are both in. Leave blank if they are in different locations")
parser.add_argument("todo", help="The name of the todo file. Input full path if --folder is blank. Defaults to todo.txt")
parser.add_argument("someday", help="The name of the someday file. Input full path if --folder is blank. Defaults to someday.txt")
args = parser.parse_args()
print(args)
script = os.path.realpath(__file__)

command = "schtasks /Create /SC DAILY /TN Someday2todo /TR \"python " + script + "\" /ST 00:00 "
# o = os.popen(command).read()
# print(o)
os.system(command)    





