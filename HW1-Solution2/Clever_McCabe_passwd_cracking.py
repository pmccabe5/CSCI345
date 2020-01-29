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
ruleFourDictionary7 = {}

# dictionary specifically for rule five
ruleFiveDictionary = {}

# booleans to keep track of whether or not the hash tables are done generating
waitUntilDoneBuilding = [True, True, True, True, True, True]

# symbols that are included in rule four
symbols = ["*", "~", "!", "#"]

# files needed for the operation of the program
wordlist = open('/usr/share/dict/words', 'r')
passwordDump = open('passwordDump.txt', 'r')
outfile = open('cracked-passwords-Clever-McCabe.txt', 'w')
passwordsCracked = 0


'''
ruleOne implements the a rule for 7 char word + capitalized first letter at 
position 0. The password file for this function is named ruleOnePasswords.txt, 
with the formatting plaintext:sha256.
'''

def ruleOne(encrypt):
    hashfile1 = open('ruleOnePasswords.txt', 'r')
    for line in hashfile1:
        line = line.strip('\n')
        passwd = []
        passwd = line.split(':')        
        if passwd[1] == encrypt:
            print(colored(encrypt + ':' + passwd[0], 'green'))
            outfile.write(passwd[1] + ':' + passwd[0] + '\n')
            return True

'''
ruleTwo takes into account th possibility of a password of legnth 5 with a
special character at the beginning of the password. Special characters included
in this list include [*, ~, !, #] followed by 4 digits. The passwords are 
located in the directory in ruleTwoPasswords.txt, with the formatting 
plaintext:sha256.
'''

def ruleTwo(encrypt):
    hashfile2 = open('ruleTwoPasswords.txt', 'r')
    for line in hashfile2:
        line = line.strip('\n')
        passwd = []
        passwd = line.split(':')        
        if passwd[1] == encrypt:
            print(colored(encrypt + ':' + passwd[0], 'green'))
            outfile.write(passwd[1] + ':' + passwd[0] + '\n')
            return True

'''
ruleThree performs the password check on passwords that contain  either an 'a'
or an 'l' and substituted for '@' and '1' respectively. The passwords are 
located in ruleThreepasswords.txt, with the formatting plaintext:sha256.
'''
       
def ruleThree(encrypt):
    hashfile3 = open('ruleThreePasswords.txt', 'r')
    for line in hashfile3:
        line = line.strip('\n')
        passwd = []
        passwd = line.split(':')        
        if passwd[1] == encrypt:
            print(colored(encrypt + ':' + passwd[0], 'green'))
            outfile.write(passwd[1] + ':' + passwd[0] + '\n')
            return True

'''
ruleFour compares the hashes where they may be numeric (digits 0-9) up to 
seven digits in length. The passwords are stored in ruleFourPasswords.txt,
stored as plaintext:sha256
'''

def ruleFour(encrypt):
    hashfile4 = open('ruleFourPasswords.txt', 'r')
    for line in hashfile4:
        line = line.strip('\n')
        passwd = []
        passwd = line.split(':')        
        if passwd[1] == encrypt:
            print(colored(encrypt + ':' + passwd[0], 'green'))
            outfile.write(passwd[1] + ':' + passwd[0] + '\n')
            return True

'''
ruleFour compares the hashes where the word could be contained in 
/usr/share/dict/words. The passwords are stored in ruleFourPasswords.txt,
stored as plaintext:sha256
'''

def ruleFivePass(encrypt):
    hashfile5 = open('ruleFivePasswords.txt', 'r')
    for line in hashfile5:
        line = line.strip('\n')
        passwd = []
        passwd = line.split(':')        
        if passwd[1] == encrypt:
            print(colored(encrypt + ':' + passwd[0], 'green'))
            outfile.write(passwd[1] + ':' + passwd[0] + '\n')
            return True
            
'''
threaded is used for threading the program to improve perfomance and sppeed of
the password cracker
'''
    
def threaded(passwd):
    cracked = False
    if cracked == False:
        isCracked = ruleThree(passwd)
        if isCracked:
            cracked = True
    if cracked == False:
        isCracked = ruleTwo(passwd)
        if isCracked:
            cracked = True   
    if cracked == False:
        isCracked = ruleFive(passwd)
        if isCracked:
            cracked = True
    if cracked == False:
        isCracked = ruleOne(passwd)
        if isCracked:
            cracked = True
    if cracked == False:
        isCracked = ruleFour(passwd)
        if isCracked:
            cracked = True
    if cracked == False:
        print(colored('Password not found in the specified lists:' + passwd, 'red'))
    global passwordsCracked 
    passwordsCracked =  passwordsCracked + 1

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
        rule5Sha256.update(line.encode())
        rule5Sha256 = rule5Sha256.hexdigest()
        ruleFiveDictionary[rule5Sha256] = fulltext   

        if len(line) == 7:

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
        if len(fulltext) == 5:
            fulltext = fulltext.replace('a', '@')
            fulltext = fulltext.replace('l', '1')
            rule3Sha256 = hashlib.sha256()
            rule3Sha256.update(line.encode())
            rule3Sha256 = rule3Sha256.hexdigest()
            ruleThreeDictionary[rule3Sha256] = fulltext
        
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
    waitUntilDoneBuilding[4] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length six for rule four, 
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
and generates hashes up to length six for rule four, 
without any of the special characters from rule two.
'''

def ruleFourLength6():
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
    waitUntilDoneBuilding[1] = False

'''
This method continues from the previous method for rule four
and generates hashes up to length seven for rule four, 
without any of the special characters from rule two.
'''

def ruleFourLength7():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                number = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)
                                print(number)
                                rule4For7Sha256 = hashlib.sha256()
                                rule4For7Sha256.update(number.encode())
                                rule4For7Sha256 = rule4For7Sha256.hexdigest()
                                ruleFourDictionary7[rule4For7Sha256] = number
    waitUntilDoneBuilding[0] = False

def main():
    
    # threadZero = Thread(target = ruleFourLength7)
    # threadZero.start()

    threadOne = Thread(target = ruleFourLength6)
    threadOne.start()

    threadTwo = Thread(target = ruleFourLength5)
    threadTwo.start()

    threadThree = Thread(target = ruleOneAndThreeAndFivePasswords)
    threadThree.start()

    threadFour = Thread(target = ruleTwoAndRuleFourLength4)
    threadFour.start()

    threadFive = Thread(target = ruleFourLength1to3)
    threadFive.start()
    
    while(waitUntilDoneBuilding[1] == True or waitUntilDoneBuilding[2] == True 
          or waitUntilDoneBuilding[3] == True or waitUntilDoneBuilding[4] == True 
          or waitUntilDoneBuilding[5] == True):
        spin = True
    print(len(ruleFiveDictionary))

    
    #for i in range(len(plaintext)):
    #   print (plaintext[i])    
        
main()

'''

passwds = []
    cracked = []
    for line in passwordDump.readlines():
       password = line.split(':')[1].strip('\n') 
       isCracked = False 
       passwds.append(password)
       cracked.append(False)
    for password in passwds:
        thread = Thread(target = threaded, args = (password,))
        thread.start()  
    global passwordsCracked
    delay = True
    while passwordsCracked != len(passwds):
        #delay for closing the outputfile for security purposes
        delay = True    
    outfile.close()



hashfile = open('ruleThreePasswords.txt', 'r')
    for line in hashfile:
        line = line.strip('\n')
        passwd = []
        passwd = line.split(':')        
        if passwd[1] == encrypt:
            print(encrypt + ':' + passwd[0])
            outfile.write(passwd[1] + ':' + passwd[0])
            return True
def ruleFivePasswords():
    hashfile = open('ruleFivePasswords.txt', 'w')
    for passwd in infile: 
        passwd = passwd.strip('\n')    
        possibleHash = hashlib.sha256()
        possibleHash.update(passwd.encode())
        possibleHash = possibleHash.hexdigest()
        hashfile.write(passwd + ':' + possibleHash + '\n')
    hashfile.close()   

def ruleFourPasswords():
    hashfile = open('ruleFourPasswords.txt', 'w')
    for passwd in infile: 
        passwd = passwd.strip('\n')
        print(passwd)    
        possibleHash = hashlib.sha256()
        possibleHash.update(passwd.encode())
        possibleHash = possibleHash.hexdigest()
        hashfile.write(passwd + ':' + possibleHash + '\n')
    hashfile.close()   

'''
