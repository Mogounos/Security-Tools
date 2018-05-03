'''PasswordJS.py, 2018/01/13, Compute Password Strength'''

import string

MinPassWordLength = 8

AllPrintableLetters = [chr(i) for i in range(32, 127)]

def CountFromList(inTextString, ListToFind) :
    '''============================================================='''
    retVal = 0
    for letter in inTextString :
        if letter in ListToFind :
            retVal = retVal + 1
    return retVal

def CountUnprintable(inTextString) :
    '''============================================================='''
    retVal = len(inTextString)
    retVal = retVal - CountFromList(inTextString,AllPrintableLetters)
    return retVal

def ComputePassWordStrength(wordToTest) :
    '''============================================================='''
    retVal = 1
    if (CountUnprintable(wordToTest)>0) :
        retVal = -1
    elif (wordToTest.count(" ")>0) :
        retVal = -2
    elif (len(wordToTest)<MinPassWordLength) :
        retVal = -3

    else:
        retVal = retVal*2
        retVal = retVal*CountFromList(wordToTest, string.digits)
        retVal = retVal*CountFromList(wordToTest, string.ascii_lowercase)
        retVal = retVal*CountFromList(wordToTest, string.ascii_uppercase)
        retVal = retVal*CountFromList(wordToTest, string.punctuation)
    return retVal

def ReportPassWordStats(test) :
    '''=============================================================
        Print a report showing the properties pf the the given password'''

    '''============================================================='''
    print("="*40)
    print("TestText : '%s'"%(test))
    print("="*40)
    print("\tLength : %3d"%(len(test)))
    print("\tDigits : %3d"%(CountFromList(test,string.digits)))
    print("\tUppercase : %3d"%(CountFromList(test,string.ascii_uppercase)))
    print("\tLowercase : %3d"%(CountFromList(test,string.ascii_lowercase)))
    print("\tSpecial : %3d"%(CountFromList(test,string.punctuation)))
    print("="*40)
    print("\tSpaces : %3d"%(CountFromList(test, ' ')))
    print("\tUnprinatable : %3d"%(CountUnprintable(test)))
    print("="*40)
    print("\tStrength : %3d"%(ComputePassWordStrength(test)))
    print("="*40)

'''=============================================================
    Main Program
   ============================================================='''
if(__name__=='__main__') :
    WordsToTest = [string.printable, "Able Was I #123456789", 'Dog#42',
                   '4-JULY-2004', 'Apple5^uc3', 'H!nT@M3', "Frodo |_1Ve5",
                   "NcC-1701a"]
    for myWord in WordsToTest :
        ReportPassWordStats(myWord)
'''============================================================='''
