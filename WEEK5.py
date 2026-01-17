# import tkinter
import serial

strFullname = " "
intlength = len(strFullname)
print(intlength)
print(strFullname[3])
print(strFullname[5])
print(strFullname[intlength - 1])

strInput = "christopher cresencio"

strFullname = strInput
print(strFullname)
intlength = len(strFullname)
print(intlength)

strFullname = "christopher cresencio"

strNewValue = strFullname.upper()
print(strNewValue)
strNewvalue = strFullname.count("e")
print(strNewvalue)
strNewvalue = strFullname.split(" ")
print(strNewvalue)

strFullname = "christopher cresencio lopina"
strNewValue = strFullname.replace("christopher", "chris")
print(strNewValue)

strFirstname = "christopher"
strMiddlename = "cresencio"
strLastname = "lopina"
strfullname = "_".join([strFirstname, strMiddlename, strLastname])
print(strfullname)

newValue = strFullname.isnumeric()
print(newValue)
newValue = strFullname[3:10]
print(newValue)
newValue = strFullname[2:9:1]
print(newValue)

strFullname.index("e")
print(strFullname.index("e", 2, 11))

strINPUT = "123christopher 123cresencio"
print(strINPUT)
print(strINPUT.replace("123","" ))

newString = ""
for char in strINPUT:
    if not char.isnumeric():
        newString = newString + char

print(newString)

myIntegerA = 33
myIntegerB = 34
myFloatA = 54.31
myFloatB = 9.1
myComplexA = 167 - 131j
myComplexB = 31 - 11j

sum = myIntegerA + myIntegerB
print(sum)
difference = myIntegerA - myIntegerB
print(difference)
product = myIntegerA * myIntegerB
print(product)
division = myIntegerA / myIntegerB
print(division)
remainder = myIntegerA % myIntegerB
print(remainder)

print(" ")
sum1 = myFloatA + myFloatB
print(sum1)
difference1 = myFloatA - myFloatB
print(difference)
product1 = myFloatA * myFloatB
print(product1)
division1 = myFloatA / myFloatB
print(division1)
myRounddivision1 = round(division1, 2)
print(myRounddivision1)
remainder1 = myFloatA % myFloatB
print(remainder1)

print(" ")
sum2 = myComplexA + myComplexB
print(sum2)
difference2 = myComplexA - myComplexB
print(difference)
product2 = myComplexA * myComplexB
print(product2)
division2 = myComplexA / myComplexB
print(division2)
remainder2 = myComplexA - myComplexB
print(remainder2)

isPresent = False
isExist = True
isAvailable = "True"
isValid = 1
isOkay = 0
isNumeric = False
myChar = "5"
isNumeric = myChar.isnumeric()
strIsNumeric = str(myChar.isnumeric())
print([isNumeric])
print([strIsNumeric])

a = 5
b = 6
isEqual = (a == b)
print(isEqual)
isGTE = (a >= b)
print(isGTE)
isLTE = (a <= b)
print(isLTE)


isIn = (5 in [25, 45, 23, 12, 5, 27])
print(isIn)
isIn = (5 in [25, 45, 23, 12, 27])
print(isIn)
isIn = ("hello" in  "hello world hi eath")
print(isIn)

isIS = ("hello" is "hello")
print(isIS)
isIS = ("hello" is "hi hello")
print(isIS)


isOkay = (5 in [25, 45, 23, 12, 5, 27]) and (5 in [25, 45, 23, 12, 27])
print(isOkay)
isOkay = (5 in [25, 45, 23, 12, 5, 27]) or (5 in [25, 45, 23, 12, 27])
print(isOkay)




intLength = len(strFullname)
print(strFullname)
print(intLength)
print(strFullname[0])
print(strFullname[5])
print(strFullname[6])
print(strFullname[14])
print(strFullname[intLength-1])

mySubString = strFullname[2:5:1]
print(mySubString)

strFullname = strFullname + "a"
print(strFullname)


strFullname = "Christopher Cresencio"


newValue = strFullname.upper()
print(newValue)
newValue = strFullname.lower()
print(newValue)
newValue = strFullname.capitalize()
print(newValue)

newValue = strFullname.split(" ")
print(newValue)
newValue = strFullname.split("is")
print(newValue)

newValue = strFullname.replace("e", "a")
print(newValue)
newValue = strFullname.replace("Cresencio", "Engineer")
print(newValue)
newValue = strFullname.replace("e", "")
print(newValue)

myFirstName = "Christopher"
myMiddleName = "C"
myLastName = "Cresencio"

myFullNameList = [myFirstName, myMiddleName, myLastName]

print("PASADO".join([myFirstName, myMiddleName, myLastName]))
print("PASADO".join(myFullNameList))

newValue = strFullname.count("e")
print(newValue)

myChar = strFullname[2]
print(myChar)
intIndex = strFullname.index("o")
print(intIndex)


import math
import mathplot
intA = 25
intB = 15
intC = 5

intSum = intA + intB + intC
print(intSum)
intDiff = intA - intB
print(intDiff)
intProd = intA * intB
print(intProd)
intQu = intA / intB
print(intQu)
intResult = intA ** intB
print(intResult)

intA = 555
intB = 4
intC = 5

isDivisible = False
remainder = intA % intB
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

isDivisible = False
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

#PMDAS

intAngle = 90
result = round(math.cos(math.radians(intAngle)), 1)
print(result)
result = round(math.sin(math.radians(intAngle)), 1)
print(result)
result = round(math.tan(math.radians(intAngle)), 1)
print(result)
intAngle = 45
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intX = 5
facResult = math.factorial(intX)
print(facResult)

myComA = 25+5j
myComB = 10-10j
comProd = myComA * myComB
print(comProd)


intA = 5
intB = 6
isResult = intA == intB
print(isResult)
isResult = intA <= intB
print(isResult)
isResult = intA >= intB
print(isResult)
isResult = intA != intB
print(isResult)
isResult = intA > intB
print(isResult)
isResult = intA < intB
print(isResult)


isResult = "e" in "madagascar"
print(isResult)
isResult = "e" in "medegescer"
print(isResult)
myList = ["pencil", "notebook", "ruler", "eraser", "compass", "calculator"]
isResult = "laptop" in myList
print(isResult)#False
myList = ["pencil", "notebook", "ruler", "eraser", "compass", "calculator", "laptop"]
isResult = "laptop" in myList
print(isResult)#True
isResult = "dege" in "medegescer"
print(isResult)


isResult = "dege" is "medegescer"
print(isResult)  #False
isResult = "medegescer" is "medegescer"
print(isResult)
isMyResult = isResult is True
print(isMyResult)


myInput = '1231hel1231312lo2313 23123231w231orld123'
myOutput = ""
for char in myInput:
    if not char.isnumeric():
        myOutput = myOutput + char
    else:
        print(f"Hindi pasok yan kasi yan ay: {char} ")
print(myOutput)


isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86
isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)
isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)
isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed)

isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86
isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)
isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)
isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed)


intA = 555
intB = 5
intC = 4

isDivisible = False #initial value
remainder = intA % intB
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

isDivisible = False
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)