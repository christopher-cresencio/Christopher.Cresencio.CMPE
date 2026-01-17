shape = "circle"

if shape == "circle":
    print("circle")
elif shape == "square":
    print("square")
elif shape == "triangle":
    print("triangle")
else:
    print("wala")

print("sunod")

mygrade = float(int(input("enter your grade: ")))
if mygrade >= 97:
    print("galing 1.0 ")
elif mygrade >= 94:
    print("galing pa rin 1.25 ")
elif mygrade>= 91:
    print("nice 1.5 ")
elif mygrade >= 88:
    print("nice din 1.75 ")
elif mygrade >= 85:
    print("good 2.0 ")
elif mygrade >= 82:
    print("good (?) 2.25 ")
elif mygrade >= 79:
    print("eh 2.5 ")
elif mygrade >= 76:
    print("eh 2.75 ")
elif mygrade >= 75:
    print("bruh 3.0 ")
elif mygrade < 75:
    print("bruh u failed ")
else: print("u tried?")

citizenship = input("Enter your citizenship: ")
age = float(int(input("Enter your age: ")))
Updated_Registry = input("Is Your Registry Updated? Y/N: ")

if Updated_Registry == "Y":
    Updated_Registry = True
else :
    Updated_Registry = False



if citizenship == "Filipino" and age >= 18:
    if Updated_Registry :
        print("Paldo sa Election")
    else:
        print("Lumbay sa Election")
elif citizenship == "Filipino" and age < 18:
    print("Wait for Registration")
else:
    print("You Can't Vote")

# --- FOR LOOPS ---
# initial, limit, increment
print("Start")
for x in range(0, 10, 1):
    print("x value is: " + str(x))
print("End")

print("Start")
componentsList = ["resistor", "capacitor", "inductor", "transistor"]
for component in componentsList:
    print("Component List Include:" + component)
print("End")

print("Start")
MyString = "CHRISTOPHER"
for char in MyString:
    print(char.upper())
print("End")

print("Start")
OriginalValue = "Christopher Cresencio"
print("Original Value: " + OriginalValue)
newValue = ""

for x in OriginalValue:
    newValue = x + newValue

print("New Value: " + newValue)
print("End")

print(OriginalValue[::-1])

print("Start")
for i in range(10):
    if i % 2 == 0:
        print("Even Number: " + str(i))
        continue
    elif i > 6:
        print("i is greater than 6")
        break
    print("i value now is: " + str(i))
print("End")

print("Start")
import time

isConnected = False

for retry in range(4):
    time.sleep(1)
    isConnected = (input("Is Connected?"))
    if isConnected == "Yes":
        time.sleep(1)
        print("Now Connected👍🏻")
        break
    else:
        time.sleep(1)
        print("Processing Request...⏳")
        time.sleep(1)
        print("Request Timeout.✋")
time.sleep(1)
print("Transaction Done.✅")
print("End")

print("Start")
for i in range(5):
    print(str(i) + "-----")
    for x in range(3):
        print(x)
print("End")

print("Start")

charlist = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', ' Z', '0', '1', '2', '3', '4', '5', '6', '7',
             '8', ' 9', '!', '@', '#', '$', '%', '^', '&', '*',
             '(', ')', '-', '=', '+', '[', ']', '{', '}', ";",
             ":", "'", '"', ",", "<", ".", ">", "/", "?", "\\",
             "|", "`", "~", " "]

myInput = "Chris123"
output = ""
key = 3
indexcounter = 0

for letter in myInput:
    indexcounter = charlist.index(letter)
    output = output + charlist[indexcounter + key]

print("Encrypted: " + output)
print("End")