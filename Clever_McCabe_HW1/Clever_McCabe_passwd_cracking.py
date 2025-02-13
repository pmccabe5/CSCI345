#!/usr/bin/python3
#Clever, Clare & McCabe, Patrick
#HW1, Spring 2020

# libraries needed for execution: hashlib, threading, and termcolor (for aesthetic purpose)
import hashlib
from threading import *
from termcolor import colored

# dictionaries for rules one, two, and three
ruleOneDictionary = {}
ruleTwoDictionary = {}
ruleThreeDictionary = {}

# individual dictionaries for rule four based on length of the password before hashing
ruleFourDictionary1to3 = {}
ruleFourDictionary4 = {}
ruleFourDictionary5 = {}
ruleFourDictionary6 = {}
ruleFourDictionary7_0 = {}
ruleFourDictionary7_1 = {}
ruleFourDictionary7_2 = {}
ruleFourDictionary7_3 = {}
ruleFourDictionary7_4 = {}
ruleFourDictionary7_5 = {}
ruleFourDictionary7_6 = {}
ruleFourDictionary7_7 = {}
ruleFourDictionary7_8 = {}
ruleFourDictionary7_9 = {}

# dictionary specifically for rule five
ruleFiveDictionary = {}

# booleans to keep track of whether or not the hash tables are done generating
waitUntilDoneBuilding = [True, True, True, True, True, True, True, True, 
True, True, True, True, True, True, True]

# symbols that are included in rule four
symbols = ["*", "~", "!", "#"]

passwordHashes = []

# files needed for the operation of the program
wordlist = open('words.txt', 'r')
passwordDump = open('passwordDump.txt', 'r')
outfile = open('cracked-passwords-Clever-McCabe.txt', 'w')
passwordsCracked = 0

'''
This method generates the hashed passords in the form of 
a hash table, usng the dictionary data type for rules one, 
three, and five. These rules are generated at the same time
due to the word file, /usr/share/dict/words, being open and being used
in all three of the rules. 
'''

def ruleOneAndThreeAndFivePasswords():

    # iterates through /usr/share/dict/words
    for line in wordlist:

        # fulltext is an alias for line so it can be used without capitalization
        # or a number added on for rule one. fulltext is used for both rules three 
        # and five. New line character is stripped with the .strip('\n')

        fulltext = line.strip('\n')

        # rule5Sha256 is the process of hashing fulltext before insertion into
        # the hash table
        rule5Sha256 = hashlib.sha256()
        rule5Sha256.update(fulltext.encode())
        rule5Sha256 = rule5Sha256.hexdigest()
        ruleFiveDictionary[rule5Sha256] = fulltext     
        if len(fulltext) == 7:

            # line is taken from the general file iterator and is only used for rule 
            # three due to the capitalization and number appending to satisfy rule one
            line = line.capitalize()
            line = line.strip('\n')

            # appending of single digit to line before hashing and storage 
            # into the dictionary
            for count in range(10):
                temp = line.strip('\n')
                temp = temp + str(count)
                sha256 = hashlib.sha256()
                sha256.update(temp.encode())
                sha256 = sha256.hexdigest()
                ruleOneDictionary[sha256] = temp

        # if statement used to satisfy rule three. fulltext is used in order to have 
        # a clean input for the SHA256 hashing and replacement of 'a' to '@' as well
        # as 'l' to '1'   
        elif len(fulltext) == 5 and (('a' in fulltext) or (('l' in fulltext))):
            fulltext = fulltext.replace('a', '@')
            fulltext = fulltext.replace('l', '1')
            rule3Sha256 = hashlib.sha256()
            rule3Sha256.update(fulltext.encode())
            rule3Sha256 = rule3Sha256.hexdigest()
            ruleThreeDictionary[rule3Sha256] = fulltext
    print(colored('DONE: Rule One, Three and Five hash tables created', 'blue'))
    waitUntilDoneBuilding[3] = False
    
'''
This method generates the hashes for rules two and four, as they are 
numeric based passwords up to four digits in length. 
Rule two specifies the location of a special character
defined as one of the following characters ["*", "~", "!", "#"] and a number of
four digits in length. Rule four generates passwords of numbers up to seven
digits in length without any special characters added. Also, the generation of 
hashes is split up into smaller functions of varying length to improve on the
efficiency of the program.
'''

def ruleTwoAndRuleFourLength4():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(4):
                        word = symbols[e] + str(a) + str(b) + str(c) + str(d)
                        rule2Sha256 = hashlib.sha256()
                        rule2Sha256.update(word.encode())
                        rule2Sha256 = rule2Sha256.hexdigest()
                        ruleTwoDictionary[rule2Sha256] = word
                    number = str(a) + str(b) + str(c) + str(d)
                    rule4For4Sha256 = hashlib.sha256()
                    rule4For4Sha256.update(number.encode())
                    rule4For4Sha256 = rule4For4Sha256.hexdigest()
                    ruleFourDictionary4[rule4For4Sha256] = number
    print(colored('DONE: Rule Two hash table created', 'blue'))
    waitUntilDoneBuilding[4] = False

'''
This method continues from the previous method for rule four
and generates hashes from one to 3 digits in length for rule four, 
without any of the special characters from rule two.
'''

def ruleFourLength1to3():
    for a in range(10):
        number = str(a)
        rule4For1to3Sha256 = hashlib.sha256()
        rule4For1to3Sha256.update(number.encode())
        rule4For1to3Sha256 = rule4For1to3Sha256.hexdigest()
        ruleFourDictionary1to3[rule4For1to3Sha256] = number
    for a in range(10):
        for b in range(10):
            number = str(a) + str(b)
            rule4For1to3Sha256 = hashlib.sha256()
            rule4For1to3Sha256.update(number.encode())
            rule4For1to3Sha256 = rule4For1to3Sha256.hexdigest()
            ruleFourDictionary1to3[rule4For1to3Sha256] = number
    for a in range(10):
        for b in range(10):
            for c in range(10):
                number = str(a) + str(b) + str(c)
                rule4For1to3Sha256 = hashlib.sha256()
                rule4For1to3Sha256.update(number.encode())
                rule4For1to3Sha256 = rule4For1to3Sha256.hexdigest()
                ruleFourDictionary1to3[rule4For1to3Sha256] = number
    waitUntilDoneBuilding[5] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length five for rule four, 
without any of the special characters from rule two.
'''

def ruleFourLength5():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        number = str(a) + str(b) + str(c) + str(d) + str(e)
                        rule4For5Sha256 = hashlib.sha256()
                        rule4For5Sha256.update(number.encode())
                        rule4For5Sha256 = rule4For5Sha256.hexdigest()
                        ruleFourDictionary5[rule4For5Sha256] = number
    waitUntilDoneBuilding[2] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two.
The method also lets the user see the current status of the
list generation. This method also prints out updates for the user
in order to see where the program is currently.
=======

'''

def ruleFourLength6andLength7Start0():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                            rule4For6Sha256 = hashlib.sha256()
                            rule4For6Sha256.update(number.encode())
                            rule4For6Sha256 = rule4For6Sha256.hexdigest()
                            ruleFourDictionary6[rule4For6Sha256] = number

                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(0)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_0[rule4For7Sha256] = number

                            if(number == '1000000'):
                                print(colored("Current Status:", 'magenta'))
                                print(colored("8,999,999 Left . . .", 'magenta'))
                            elif(number == '2000000'):
                                print(colored("7,999,999 Left . . .", 'magenta'))
                            elif(number == '3000000'):
                                print(colored("6,999,999 Left . . .", 'magenta'))
                            elif(number == '4000000'):
                                print(colored("5,999,999 Left . . .", 'magenta'))
                            elif(number == '5000000'):
                                print(colored("4,999,999 Left . . .", 'magenta'))
                            elif(number == '6000000'):
                                print(colored("3,999,999 Left . . .", 'magenta'))
                            elif(number == '7000000'):
                                print(colored("2,999,999 Left . . .", 'magenta'))
                            elif(number == '8000000'):
                                print(colored("1,999,999 Left . . .", 'magenta'))
                            elif(number == '9000000'):
                                print(colored("999,999 Left . . .", 'magenta'))
    waitUntilDoneBuilding[1] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two.
'''

def ruleFourLength7Start1():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(1)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_1[rule4For7Sha256] = number
    waitUntilDoneBuilding[0] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two. 
This method is segmented to improve on runtime
'''

def ruleFourLength7Start2():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(2)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_2[rule4For7Sha256] = number
    waitUntilDoneBuilding[6] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two. 
This method is segmented to improve on runtime
'''

def ruleFourLength7Start3():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(3)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_3[rule4For7Sha256] = number
    waitUntilDoneBuilding[7] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two. 
This method is segmented to improve on runtime
'''

def ruleFourLength7Start4():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(4)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_4[rule4For7Sha256] = number
    waitUntilDoneBuilding[8] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two. 
This method is segmented to improve on runtime
'''

def ruleFourLength7Start5():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(5)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_5[rule4For7Sha256] = number
    waitUntilDoneBuilding[9] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two. 
This method is segmented to improve on runtime
'''

def ruleFourLength7Start6():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(6)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_6[rule4For7Sha256] = number
    waitUntilDoneBuilding[10] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two. 
This method is segmented to improve on runtime
'''

def ruleFourLength7Start7():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(7)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_7[rule4For7Sha256] = number
    waitUntilDoneBuilding[11] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two. 
This method is segmented to improve on runtime
'''

def ruleFourLength7Start8():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(8)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_8[rule4For7Sha256] = number
    waitUntilDoneBuilding[12] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two. 
This method is segmented to improve on runtime
'''

def ruleFourLength7Start9():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(9)
                            rule4For7Sha256 = hashlib.sha256()
                            rule4For7Sha256.update(number.encode())
                            rule4For7Sha256 = rule4For7Sha256.hexdigest()
                            ruleFourDictionary7_9[rule4For7Sha256] = number
    waitUntilDoneBuilding[13] = False

def readInPasswords():
    for line in passwordDump.readlines():
       password = line.split(':')[1].strip('\n')
       passwordHashes.append(password)
    waitUntilDoneBuilding[14] = False
    print(colored('DONE: All password hashes have been read into an array', 'blue'))

'''
Main method is designed to initiate all the threads for the program as well as read in the passwords from 
the specified hash file in the README. The other functionality of the main method is to compare the hashes
that have been loaded into the program to the hashes stored in the hashtables.
'''   


def main():
    print(colored('The program will begin by creating all the threads to build the hash table rule sets.', 'yellow'))

    threadZero = Thread(target = ruleFourLength7Start1)
    threadZero.start()

    threadSix = Thread(target = ruleFourLength7Start2)
    threadSix.start()

    threadSeven = Thread(target = ruleFourLength7Start3)
    threadSeven.start()

    threadEight = Thread(target = ruleFourLength7Start4)
    threadEight.start()

    threadNine = Thread(target = ruleFourLength7Start5)
    threadNine.start()

    threadTen = Thread(target = ruleFourLength7Start6)
    threadTen.start()

    threadEleven = Thread(target = ruleFourLength7Start7)
    threadEleven.start()

    threadTwelve = Thread(target = ruleFourLength7Start8)
    threadTwelve.start()

    threadThirteen = Thread(target = ruleFourLength7Start9)
    threadThirteen.start()

    threadOne = Thread(target = ruleFourLength6andLength7Start0)
    threadOne.start()

    threadTwo = Thread(target = ruleFourLength5)
    threadTwo.start()

    threadThree = Thread(target = ruleOneAndThreeAndFivePasswords)
    threadThree.start()

    threadFour = Thread(target = ruleTwoAndRuleFourLength4)
    threadFour.start()

    threadFive = Thread(target = ruleFourLength1to3)
    threadFive.start()

    threadFourteen = Thread(target = readInPasswords)
    threadFourteen.start()

    print(colored('DONE: All threads have been created', 'blue'))

    print(colored('Please wait. . . The program is currently generating the hash table rule sets.', 'yellow'))
    print(colored('Periodic updates will be given along the way displaying the programs progress.', 'yellow'))
    
    while(waitUntilDoneBuilding[0] == True or waitUntilDoneBuilding[1] == True or waitUntilDoneBuilding[2] == True 
          or waitUntilDoneBuilding[3] == True or waitUntilDoneBuilding[4] == True 
          or waitUntilDoneBuilding[5] == True or waitUntilDoneBuilding[6] == True or waitUntilDoneBuilding[7] == True 
          or waitUntilDoneBuilding[8] == True or waitUntilDoneBuilding[9] == True or waitUntilDoneBuilding[10] == True
          or waitUntilDoneBuilding[11] == True or waitUntilDoneBuilding[12] == True or waitUntilDoneBuilding[13] == True
          or waitUntilDoneBuilding[14] == True):
        spin = True
    
    print(colored('DONE: All hash table rule sets have been created', 'blue'))

    for hashedPassword in passwordHashes:
        hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleOneDictionary[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleOneDictionary[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleTwoDictionary[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleTwoDictionary[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleThreeDictionary[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleThreeDictionary[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary1to3[hashedPassword]), 'green')
                outfile.write(hashedPassword + ':' + ruleFourDictionary1to3[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary1to3[hashedPassword],'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary1to3[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary4[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary4[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary5[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary5[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary6[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary6[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try: 
                print(colored(hashedPassword + ':' + ruleFourDictionary7_0[hashedPassword],'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_0[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_1[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_1[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_2[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_2[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_3[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_3[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_4[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_4[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_5[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_5[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_6[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_6[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_7[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_7[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_8[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_8[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFourDictionary7_9[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFourDictionary7_9[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            try:
                print(colored(hashedPassword + ':' + ruleFiveDictionary[hashedPassword], 'green'))
                outfile.write(hashedPassword + ':' + ruleFiveDictionary[hashedPassword] + '\n')
                hashFound = True
            except:
                hashFound = False
        if(hashFound == False):
            print(colored('Hash not found . . . ' + hashedPassword, 'red'))
        
main()
