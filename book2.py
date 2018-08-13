##Imports
import re


##Vars
Books = dict()
Details = ['Serial no','Catagory','Shelf','Author name','Publisher name','Publishing year','Copies','Lent','Lent to','Lent on','Lent till']
DetailsDic = {'serial no' : 0,'catagory' : 1,'shelf' : 2,'author name': 3 ,'publisher name': 4 ,'publishing year': 5 ,'copies': 6 ,'lent': 7 , 'lent to' : 8 ,'lent on': 9 ,'lent till': 10 }


##Book Functions

def addbook(name):

    lenten = False
    if name in Books:
        print ('Book with that name already exists!')
    else:
        Books[name.lower()] = list()
        for i in Details:
            if i == 'Lent to':
                lenten = True

            if lenten == True and Books[name][7] == 'no' and (i == 'Lent to' or i == 'Lent on' or i == 'Lent till'):
                Books[name].append('N/A')
                continue
            else:
                inp = input('Enter ' + i + '\n\r>>')
                Books[name].append(inp.lower())
    print ('Book added to list, please exit using "close" to save it!')

def modifybook(name):
    lenten = False
    if name not in Books:
        print ('Book with that name does not exist!')
    else:
        print('Edit details of book')
        inp = inputcheck(['All','No'] + Details)
        if inp.lower() == 'no':
            print('Nothing changed')
        elif inp.lower() == 'all':
            Books[name] = list()
            for i in Details:
                if i == 'Lent to':
                    lenten = True

                if lenten == True and Books[name][7] == 'no' and (i == 'Lent to' or i == 'Lent on' or i == 'Lent till'):
                    Books[name].append('N/A')
                    continue
                else:
                    inp = input('Enter ' + i + '\n\r>>')
                    Books[name].append(inp.lower())
            print ('New values added, please exit using "close" to save it!')
        else:
            changed = input('What do you want ' + str(inp) + ' to be changed to?\n\r>>')
            Books[name][DetailsDic[inp.lower()]] = changed
            print ('Value of ' + str(inp) + ' changed, please exit using "close" to save it!')

def inputcheck(validlist):
    while True:
        inp = input('Type "?" for help\n\r>>')
        if inp == '?':
            print (validlist)
            continue
        if inp.capitalize() in validlist:
            return inp
        print('Invalid input!\n\r>>')

def search():
    print ('What parameter you want to search the book with?')
    typechoice = inputcheck(['Name'] + Details)
    result = input('What is the value of ' + typechoice + ' you are searching for? \n\r >>')
    print ('Books matching the specifications are')
    if typechoice == 'name':
        for i in Books:
            if i.lower() == result.lower():
                printbook(i)
    else:
        for i in Books:
            if Books[i][DetailsDic[typechoice.lower()]] == result.lower():
                printbook(i)

def printbook(name):
    print ('__________________________________')
    print ('Name: ' + name)
    z = 0
    for i in Books[name]:
        print (Details[z] + ': ' + i)
        z += 1
    print ('__________________________________')

def openfile(filename):

    try:
        fileread = open(filename, 'r')
    except:
        return False
    for line in fileread:
        if re.search('^\S', line):
            line = line.strip()
            things = line.split()
            listitems = list()
            for i in things[1:]:
                listitems.append(i)
        Books[things[0]] = listitems
    fileread.close()
    return True

#Opening or creating file and overwriting all data from Books dictionary
def writefile(filename):
    filewirte = open(filename,'w+')
    for i,v in Books.items():
        stuff = ''
        for j in v:
            stuff += str(j) + ' '
        filewirte.write(str(i) + ' ' + stuff + '\r\n')

#calling stuff
filename = input('Please enter a file name to read from?\r\n>>')
exist = openfile(filename)
if not exist:
    print ('''File doesn't exist New file will be created upon exit''')
while True:

    print('What will you like to do with file?')
    operation = inputcheck(['Add','Modify','Search','View', "Close" ])
    if operation == 'add':
        addbook(input('Enter book name \n\r>>'))
    elif operation == 'modify':
        modifybook(input('Enter book name \n\r>>'))
    elif operation == 'search':
        search()
    elif operation == 'close' :
        break
    elif operation == 'view' :
        for i in Books:
            printbook(i)
writefile(filename)
