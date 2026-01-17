""""
student1_name = "Jasper"
student1_grade = "1.5"
student1_subject = ["Calculus, Chemistry"]

student2_name = "Mark"
student2_grade = "2.0"
student2_subject = ["Basic Electronics, Biology"]

student3_name = "Kurt"
student3_grade = "1.0"
student3_subject = ["Mathematics, Statistics"]

def print_student_info_function(name, grade, subject):
    print(f"{name} grade: {grade}  subject {subject}")

if __name__ == "__main__":
    print_student_info_function(student1_name, student1_grade, student1_subject)
    print_student_info_function(student2_name, student2_grade, student2_subject)
    print_student_info_function(student3_name, student3_grade, student3_subject)


class Student:
    DEFAULT_SUBJECT = ["Basic Electronics, Biology"]

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info_method(self):
        print(f"{self.name} grade: {self.grade} subject {self.subject}")

    @staticmethod
    def is_grade_passing(grade):
        return grade <= 3.00

    @classmethod
    def create_default_student(cls, name, grade):
        print(f"{name} grade: {grade}  subject {cls.DEFAULT_SUBJECT}")
        return cls(name, grade, cls.DEFAULT_SUBJECT)


if __name__ == "__main__":
    student1 = Student("Matt", 1.75, ["Physics", "Programming"])
    student1.print_student_info_method()
    if Student.is_grade_passing(student1.grade):
        print("Passed")
    else:
        print("Failed")

    student2 = Student("Jordan", 2.00, ["Entrepreneurship", "PE"])
    student2.print_student_info_method()
    if Student.is_grade_passing(student2.grade):
        print("Passed")
    else:
        print("Failed")


    student3 = Student("Kenneth", 3.00, ["UTS", "Science"])
    student3.print_student_info_method()
    if Student.is_grade_passing(student3.grade):
        print("Passed")
    else:
        print("Failed")

    student4 = Student.create_default_student( "Jaylo", 3.5)
    if Student.is_grade_passing(student4.grade):
        print("Passed")
    else:
        print("Failed")

"""

import serial
import threading
import time

PORT =  "COM2"
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE, timeout=1)
time.sleep(2)

def send(message):
    ser.write((message + '\n').encode())
    print(f"sent : {message}")

def receive():
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        if data:
            print(f"received : {data}")
            return data
    else:
        return None

def received_continuous():
    while running:
        received_data = receive()
        time.sleep(0.1)

running = True
receiver_thread = threading.Thread(target=received_continuous, daemon=True)
receiver_thread.start()

try:
    while True:
        message = input("Press enter your message: ")
        if message:
            send(message)

except KeyboardInterrupt:
    print("Exit")

finally:
    running = False
    ser.close()
















