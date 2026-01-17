toolsA = ["multimeter", "multimeter", "oscilloscope", "breadboard", "jumper wires"]
print(toolsA)
print(toolsA)
print(toolsA)
print(toolsA[2])
print(toolsA.index("oscilloscope"))
isThere = "oscilloscope" in toolsA
print(isThere)

toolsA.append("resistor")
print(toolsA)
toolsA.append("capacitor")
print(toolsA)

toolsA.insert(2, "soldering iron")
print(toolsA)

len(toolsA)
print (len(toolsA))

print(toolsA.count("jumper wires"))

toolsA.remove("multimeter")
print(toolsA)
toolsA.remove("multimeter")
print(toolsA)
print(toolsA.index("oscilloscope"))
toolsA[1] = "transistor"
print(toolsA)

toolsA = ["multimeter", "multimeter", "oscilloscope", "breadboard", "jumper wires"]
toolsB = ["capacitor", "soldering iron", "power supply", "transistor", "diode"]
toolsC = ["inductor", "pliers", "wire stripper", "battery", "sensor"]

toolKit_list = [toolsA, toolsB, toolsC]
print(toolKit_list)
print(toolKit_list[2])
print(toolKit_list[1][3])

toolKit_plus = toolsA + toolsB + toolsC
print(toolKit_plus)

(toolsA.extend(toolsB))
(toolsB.extend(toolsC))
print(toolsA)
print(toolsB)

toolsA = {"multimeter", "multimeter", "oscilloscope", "breadboard", "jumper wires", "soldering iron"}
toolsB = {"capacitor", "soldering iron", "power supply", "transistor", "diode", "breadboard"}
print(toolsA)

toolsA.add("diode")
print(toolsA)

toolsUnion = toolsA.union(toolsB)
print(toolsUnion)

toolsIntersection = toolsA.intersection(toolsB)
print(toolsIntersection)

toolDifference = toolsA.difference(toolsB)
print(toolDifference)

toolkitlistofset = [toolsA, toolsB]
print(toolkitlistofset)

toolsA = ("multimeter", "multimeter", "oscilloscope", "breadboard", "jumper wires", "soldering iron")
print(toolsA)

toolkit = (toolsA, toolsB)
print(toolkit)

superlist = [ {1, 2, 3}, True, toolkit, ["a"], [True, False], 13107]
print(superlist)

mytuple = (
(1, 2, 3, "A"),
(4, 5, 6, "B"),
(7, 8, 9, "C"),
)

print(mytuple[2][2])

# Updated to your info
myInfo =  {"Name": "Christopher",
           "Age": 18,
           "Height": 1.75,
           "Address": "Manila" }
print(myInfo)
print(myInfo["Age"])
print(myInfo["Height"])
print(myInfo["Address"])
print(myInfo.get("Address"))

myInfo["Name"] = "Cresencio"
print(myInfo)

print(myInfo["Name"])

myInfo.update({"Section" : 1})
print(myInfo)
print(myInfo["Section"])

myInfo.update({"Name": "Christopher"})
print(myInfo)

# Nested Dictionary Example
myInfo ={"Name" : {"Fist Name" : "Christopher", "Last Name" : "Cresencio"},
                  "Age" : 18, "Height": 1.75,
                  "Address": "Manila",
                  "Hobbies" : ("Coding",
                               "Engineering Projects") }
print(myInfo)

print(myInfo["Name"]["Last Name"])
print(myInfo["Hobbies"])

simpleATMDatabase = {
    "Name": {
        "Fist Name": "Christopher",
        "Last Name": "Cresencio"
    },
    "AccountNumber" : 13107,
    "PIN" : 2026,
    "Control Number" : 4321,
    "Balance" : 5000,}

myName = input("Enter your name: ")
myAccountNumber = input("Enter your account number: ")
myPIN = input("Enter your PIN: ")

print(f"Balance: {simpleATMDatabase['Balance']}")