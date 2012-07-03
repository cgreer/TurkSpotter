#!/usr/bin/env python
import cgi

#log = open('log.txt', 'w')


#get current titles
myData = cgi.FieldStorage()
aData = myData['tText[]']
tTitles = [fStorage.value for fStorage in aData]

newTitles = []
with open('titles.txt', 'r') as tFile:
    knownTitles = tFile.readlines()
    knownTitles = [x.strip() for x in knownTitles]
    
    for title in tTitles:
        if title not in knownTitles:
            newTitles.append(title)


with open('titles.txt', 'a') as tFile:
    [tFile.write(x + '\n') for x in newTitles]
            


     

print "Content-type: text/html"
print aData
