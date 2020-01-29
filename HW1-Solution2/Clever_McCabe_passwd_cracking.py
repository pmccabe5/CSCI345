#!/usr/bin/python3
#Clever, Clare & McCabe, Patrick
#HW1, Spring 2020
import hashlib
from threading import *
from termcolor import colored

ruleOneDictionary = {}

ruleTwoDictionary = {}

ruleThreeDictionary = {}

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

ruleFiveDictionary = {}

waitUntilDoneBuilding = [True, True, True, True, True, True, True, True, True, True, True, True, True, True]

symbols = ["*", "~", "!", "#"]

wordlist = open('/usr/share/dict/words', 'r')
#passwordDump = open('passwordDump.txt', 'r')
#outfile = open('cracked-passwords-Clever-McCabe.txt', 'w')
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


def ruleOneAndThreeAndFivePasswords():
    for line in wordlist:
        fulltext = line.strip('\n')
        rule5Sha256 = hashlib.sha256()
        rule5Sha256.update(line.encode())
        rule5Sha256 = rule5Sha256.hexdigest()
        ruleFiveDictionary[rule5Sha256] = fulltext     
        if len(line) == 7:
            line = line.capitalize()
            line = line.strip('\n')
            for count in range(10):
                temp = line.strip('\n')
                temp = temp + str(count)
                sha256 = hashlib.sha256()
                sha256.update(temp.encode())
                sha256 = sha256.hexdigest()
                ruleOneDictionary[sha256] = temp
        if len(fulltext) == 5:
            fulltext = fulltext.replace('a', '@')
            fulltext = fulltext.replace('l', '1')
            rule3Sha256 = hashlib.sha256()
            rule3Sha256.update(line.encode())
            rule3Sha256 = rule3Sha256.hexdigest()
            ruleThreeDictionary[rule3Sha256] = fulltext
    waitUntilDoneBuilding[3] = False
    

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
                                print("Current Status:")
                                print("8,999,999 Left . . .")
                            elif(number == '2000000'):
                                print("7,999,999 Left . . .")
                            elif(number == '3000000'):
                                print("6,999,999 Left . . .")
                            elif(number == '4000000'):
                                print("5,999,999 Left . . .")
                            elif(number == '5000000'):
                                print("4,999,999 Left . . .")
                            elif(number == '6000000'):
                                print("3,999,999 Left . . .")
                            elif(number == '7000000'):
                                print("2,999,999 Left . . .")
                            elif(number == '8000000'):
                                print("1,999,999 Left . . .")
                            elif(number == '9000000'):
                                print("999,999 Left . . .\n")

    waitUntilDoneBuilding[1] = False

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
            
def main():
    print('The program will begin by creating all the threads to build the hash table rule sets.\n')

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

    print('DONE: all threads have been created\n')

    print('Please wait. . . The program is currently generating the hash table rule sets.')
    print('Periodic updates will be given along the way displaying the programs progress.\n')
    
    while(waitUntilDoneBuilding[0] == True or waitUntilDoneBuilding[1] == True or waitUntilDoneBuilding[2] == True 
          or waitUntilDoneBuilding[3] == True or waitUntilDoneBuilding[4] == True 
          or waitUntilDoneBuilding[5] == True or waitUntilDoneBuilding[6] == True or waitUntilDoneBuilding[7] == True 
          or waitUntilDoneBuilding[8] == True or waitUntilDoneBuilding[9] == True or waitUntilDoneBuilding[10] == True
          or waitUntilDoneBuilding[11] == True or waitUntilDoneBuilding[12] == True or waitUntilDoneBuilding[13] == True):
        spin = True
    print('DONE: all hash table rule sets have been created\n')

    
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