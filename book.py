#catagory , details , shelf , serial no , lend , sold , no of books , time left till return
import re


Books = dict()
Details = ['Serial no','Catagory','Shelf','Author name','Publisher name','Publishing year','Copies','Lent','Lent to','Lent on','Lent till']
DetailsDic = {'serial no' : 1,'catagory' : 2,'shelf' : 3,'author name': 4 ,'publisher name': 5 ,'publishing year': 6 ,'copies':7,'lent':8, 'lent to' : 9 ,'lent on':10,'lent till':11}

#Open a existing file ,reading it , and putting data in Books dictionary
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

#Opening or creating file and overwriting all data from Books dictionary
def writefile(filename):
    filewirte = open(filename,'w+')
    for i,v in Books.items():
        stuff = ''
        for j in v:
            stuff += str(j) + ' '
        filewirte.write(str(i) + ' ' + stuff + '\r\n')

#add book and details to Books dictionary
def addbook(book):

##if book is not in Books dictionary add it!
    temp = []
    if book not in Books:
        Books[book] = list()
        for i in Details:
            inp = input('Enter ' + i + '\n\r>>')
            temp.append(inp)
        Books[book] = temp

##if book is in book as to change value
    elif book in Books:
        print('Edit details of book')
        inp = inputcheck(['All','No'] + Details)
        if inp.lower() == 'no':
            print('Nothing changed')
        elif inp.lower() == 'all':
            for i in Details:
                inp = input('Enter ' + i + '\n\r>>')
                temp.append(inp)
            Books[book] = temp
        else:
            changed = input('What do you want ' + str(inp) + ' to be changed to?\n\r>>')
            Books[book][DetailsDic[inp.lower()]] = changed

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
    print('value')

lol = input('Enter file name\n\r>>')
exist = openfile(lol)
if not exist:
    print ('New file will be created upon exit')

while True:
    sd = input('Enter book name\n\r>>')
    if sd == 'end':
        break
    addbook(sd)
writefile(lol)
print (Books)
