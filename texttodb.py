import re
import sqlite3

handle = open('subs.txt','r')
allstuff = dict()
for line in handle:
    #check if line starts with a number accompnied with a . (1. or 2. etc)
    if re.search('^[0-9]{1,3}\.', line) :
        print (line)




input("")
