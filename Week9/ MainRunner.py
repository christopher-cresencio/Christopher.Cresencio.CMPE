import Resistor.Resistance
from Capacitor import Capacitor
from Inductor import Inductor
import NewRunner

''''
while True:
    selector = input("Please select calculator: ")

    match selector:
        case "CC_CV":
            print("Capacitance Calculator")

            Charge = float(input("Please enter charge: "))
            Voltage = float(input("Please enter voltage: "))

            Capacitor.get_capacitance_by_CV(Charge, Voltage)

        case "RC_OL":
            print("Resistance Calculator OHM'S LAW")

            voltage = float(input("Please enter voltage: "))
            current = float(input("Please enter current: "))

            Resistor.Resistance.get_resistance_by_ohmslaw(voltage, current)

        case "L_REAC":
            print(" Inductive Reactance Calculator")

            frequency = float(input("Please enter frequency: "))
            inductance = float(input("Please enter inductance: "))

            Inductor.get_inductive_reactance(frequency, inductance)

        case _:
            print("Invalid input, Please Select Again")
'''

student1_name = "Tope"
student1_grade = "1.5"
student1_subject = ["Calculus, Chemistry"]

NewRunner.print_student_info_function(student1_name, student1_grade, student1_subject)

student1 = NewRunner.Student("Tope", "1.5", ["Calculus, Chemistry"])
student1.print_student_info_method()


