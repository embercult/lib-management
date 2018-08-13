#imports
import urllib.error , urllib.parse , urllib.request
import re
import sqlite3
import os
import json
from tkinter import *
import sys
import time
import random

###inits
window_size = os.get_terminal_size().columns



###SQL inits
conn = sqlite3.connect('MagzineDB.sqlite')
cur = conn.cursor()


##FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS##
##FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS##

##Type slow?
def slow_type(t):
    typing_speed = 20 #wpm
    for l in t.upper():
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*1.0/typing_speed)
    print ('')

##fancy input & print  |||KEEP ON TOP OR MIGHT BREAK OTHER STUFF|||
def fancy(text,operation):

    if operation.lower() == 'inpu':
        slow_type(text)
        inp = input('>>')
        return inp
        slow_type(text)
    elif operation.lower() == 'prin':
        slow_type(text)
    elif operation.lower() == 'plist':
        num = 0
        goodlist = ''
        for i in text:
            goodlist += str(i) + ' , '
        slow_type(goodlist)

##check for valid input from the list provided
def validinp(question,vlist):
    while True:
        inp = fancy(question, 'inpu')
        if inp.lower() == '?' or inp.lower() == 'help':
            fancy('YOU CAN DO THE FOLLOWING : ','prin')
            fancy(vlist, 'plist')
        elif inp.lower() in vlist:
            break
        elif inp.lower() not in vlist:
            fancy('!!INVALID CHOICE!!','prin')
            fancy('type help or ? to see valid commands','prin')
    return inp

##Get address from google geo api (returns input address + formatted_address + state + pincode)
def googlegeoapi():
    apiurl = 'https://maps.googleapis.com/maps/api/geocode/json?address'
    while True:
        try:
            address = fancy('ENTER THE ADDRESS','inpu')
            url = apiurl + urllib.parse.urlencode({'': address})
            urldata = urllib.request.urlopen(url)
            data = urldata.read()

            js = json.loads(data)
            if js['status'] == 'OK':

                #Set address
                for_address = js['results'][0]['formatted_address']

                #Set State
                ln = 0
                for i in js['results'][0]['address_components']:
                    if 'administrative_area_level_1' in js['results'][0]['address_components'][ln]['types']:
                        state = js['results'][0]['address_components'][ln]['long_name']
                        break
                    ln += 1

                #Set pincode
                ln = 0
                for i in js['results'][0]['address_components']:
                    if 'postal_code' in js['results'][0]['address_components'][ln]['types']:
                        pincode = js['results'][0]['address_components'][ln]['long_name']
                        break
                    ln += 1

            #Return address + state + pincode as list
                # fancy('did you mean','prin')
                # fancy(for_address,'prin')
                corr_addr = validinp('Did you mean : ' + for_address, ['yes','no'])

                if corr_addr == 'no':
                    continue
                elif corr_addr == 'yes':
                    return [address,for_address,state,pincode]

            elif js['status'] == 'ZERO_RESULTS' or js['status'] == 'INVALID_REQUEST' :
                print('INVALID ADDRESS')
                continue

        except:
            fancy('invalid address!','prin')
            continue


##Make a list with stuff to enter in database sentbymail,magno,datelist,
def newinput():

    #sentviapost or no
    sentbymail = validinp('Was this sent vai post?',['yes','no'])

    ##Number of magzines
    while True:
        magno = fancy('How many magzines were sent?','inpu')
        try:
            magno = int(magno)
            if magno >= 1:
                break

        except:
            fancy('invalid input , please enter valid values only', 'prin')
            continue

    ##Address
    fancy('Where were magzines sent?','prin')
    addresslist = googlegeoapi()

    ##Date
    while True:
        date = fancy('Date of sending? (Enter in dd/mm/yyyy)', 'inpu')
        datelist = date.split('/')
        dateok = False
        try:
            if len(datelist) == 3:
                if int(datelist[0]) < 31 and int(datelist[1]) < 12:
                    dateok = True
        except:
            dateok = False
        finally:
            if dateok == True:
                break
            elif dateok == False:
                fancy('Invalid date!', 'prin')
    return [sentbymail,magno] + addresslist + datelist
# def stampcost():








##FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS##
##FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS####FUNCTIONS##


fancy('WELCOME TO MAGZINE OR SOMETHING','prin')
adddddd = newinput()
print (adddddd)
#adds = googlegeoapi()
input('')
