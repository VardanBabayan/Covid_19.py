import calendar
import re
import json
import os
from Queue_Patient import Node, Queue
from Hash_COVID import *
from Specialists_SLinkedList import SLinkedList, Node

class Covid:
    Patient_filename = "patient.json"
    Symptoms_filename = "Symptoms.json"
    User_info = "user_information"
    Specialists = "Specialists_SLinkedList.py"


def openuserinformation(name, surname, birthMonth, birthDay, birthYear, condition):
    if not os.path.exists("user_information.json"):
        with open("user_information.json", "w+") as file:
            initial_dict = {
                "user_information": []
            }
            json.dump(initial_dict, file) #, indent=True

    with open("user_information.json", "r") as file:
        data_json = json.load(file)
    user_information = {'name': name,
                        'surname': surname,
                        'birthMonth': birthMonth,
                        'birthDay': birthDay,
                        'birthYear': birthYear,
                        'condition': condition
                        }
    data_json["user_information"].append(user_information)
    with open("user_information.json", "w+") as f:
        json.dump(data_json, f, indent=True)
    return user_information


def name():
    while True:
        name = input("Please Enter Name: ")
        if not re.match("^[a-z]*$", name):
            print("Error! Only letters a-z allowed!")
        else:
            return name


def surname():
    while True:
        surname = input("Please Enter Surname: ")
        if not re.match("^[a-z]*$", surname):
            print("Error! Only letters a-z allowed!")
        else:
            return surname


def birthMonth():
    while True:
        try:
            birthMonth = int(input("Enter your birth month :"))
            if 0 < birthMonth <= 12:
                return birthMonth
        except:
            print("That's not a valid option!")


def birthDay():
    while True:
        try:
            birthday = int(input("Enter your birth day :"))
            if 0 < birthday <= 31:
                return birthday
        except:
            print("That's not a valid option!")


def birthYear():
    while True:
        try:
            birthYear = input("Enter the year you were born (4 digits):")
            birthYear=int(birthYear)
            if 1919 < int(birthYear) <= 2020:
                return birthYear
        except:
            print("That's not a valid option!")


def condition():
    while True:
        try:
            condition = input("Please Enter the Condition from 0-5: ")
            condition= int(condition)
            if 0 <= condition <= 5:
                return condition
        except:
            print("That's not a valid option!")

def data():
    # info = {}
    with open("Symptoms.json") as file_data:
        info = json.load(file_data)
        return info


def displayCurrentDicValue(currentValue, step=0):
    if (type(currentValue) == list):
        for item in currentValue:
            displayCurrentDicValue(item, step+1)
            print(", ", end="")
        print("\n", end="")

    elif (type(currentValue) == dict):
        for key in currentValue:
            print("\n", "\t"*step, key, ": ", end="")
            displayCurrentDicValue(currentValue[key], step+1)

    else:
        print(currentValue, end="")


def main():
    year = 2020
    while True:
        try:
            month = int(input("Enter month in numbers to see the calendar: "))
            if 0 < month <= 12:
                break
        except:
            print("That's not a valid option!")

    print(calendar.month(year, month))
    # print("\n")

    user_name = name()
    user_surname = surname()
    birth_month = birthMonth()
    day = birthDay()
    year = birthYear()
    _condition = condition()
    openuserinformation(user_name, user_surname, birth_month, day, year, _condition)
    print("\n")
    print("\nThank you for registering.Here are some of the COVID-19 symptoms")
    data()
    specialists_info = data()
    displayCurrentDicValue(specialists_info)

    llist = SLinkedList()
    print("\nHere is a list of our health specialists:-")
    llist.headval = Node("General-Doctor")
    e2 = Node("Psychotherapist")
    e3 = Node("General Doctor")

    llist.headval.nextval = e2
    e2.nextval = e3

    llist.AtEnd("Neuropathalogist")
    llist.AtBegining("Anesthesiologist Reanimatologist")
    llist.Inbetween(llist.headval.nextval, "Radiologist ")
    # list.RemoveNode("General Doctor")

    llist.listprint()
    print("\n")

    Symtomps = HashMap()
    Symtomps.put("Bella", {"fullName": "Bella Brown",
                           "birthMonth":"1",
                           "birthDay":"1",
                           "birthYear":"2001",
                           "condition":"5"})
    Symtomps.put("Kate", {"fullName": "Kate John",
                          "birthMonth": "5",
                           "birthDay":"10",
                           "birthYear":"2005",
                           "condition":"0"})
    Symtomps.put("Sam", {"fullName": "Sam Strong",
                         "birthMonth": "10",
                           "birthDay":"11",
                           "birthYear":"1970",
                           "condition":"4"})
    Symtomps.put("Tim", {"fullName": "Tim Smith",
                           "birthMonth":"7",
                           "birthDay":"6",
                           "birthYear":"1997",
                           "condition":"1"})
    Symtomps.put("Lilly", {"fullName": "Lilly Williams",
                           "birthMonth":"2",
                           "birthDay":"3",
                           "birthYear":"1988",
                           "condition":"3"})

    r = "Kate"
    Symtomps.remove(r)
    h = Symtomps.hasKey("Bella")
    n="COVID-19 negative"
    p="Still COVID-19 positive:"
    print(n)
    print(h)
    print("\n")
    print(p)
    for elem in Symtomps:
        print(elem.get("fullName"))

    print("\n")
    q = Queue()
    q.EnQueue("Bella")
    q.EnQueue("Kate")
    q.DeQueue()
    q.DeQueue()
    q.EnQueue("Sam")
    q.EnQueue("Tim")
    q.EnQueue("Lilly")
    q.DeQueue()
    print("Queue Front: " + str(q.front.data))
    print("Queue Rear: " + str(q.rear.data))


main()