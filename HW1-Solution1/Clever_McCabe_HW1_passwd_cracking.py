#!/usr/bin/python3
#Clever, Clare & McCabe, Patrick
#HW1, Spring 2020
import hashlib
from threading import *
from termcolor import colored
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

def ruleFive(encrypt):
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
    
def main():
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
    
main()

'''
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
