from math import sqrt
import time
import numpy

def main():
    end = False
    lists = []
    while end == False:
        print("1 - Make a new list\n2 - Edit list\n3 - Delete list\n4 - print all lists\n5 - Dot product (only for lists of integers)\n6 - Generate list\n7 - End program")
        begFunc = input("Enter the number corresponding to the function you wish to perform: ")
        if begFunc == "1":
            newList = makeList()
            if newList != 0:
                lists.append(newList)
        elif begFunc == "2":
            index = int(input("enter the index of the list you wish to edit: "))
            editee = lists[index]
            data = "none"
            listEdit(editee, data)
        elif begFunc == "3":
            index = int(input("enter the index of the list you wish to delete: "))
            del lists[index]
        elif begFunc == "4":
            counter = 0
            for i in lists:
                listString = ""
                for l in range(i.length()):
                    listString += str(i.retrieve(l).data) + ", "
                print(f"List {counter}: {listString}")
                counter += 1
        elif begFunc == "5":
            index1 = int(input("Enter the index of the first list in the dot product: "))
            index2 = int(input("Enter the index of the second list in the dot product: "))
            lists1 = [lists[index1], lists[index2]]
            print("The dot product is: ", dotProduct(lists1))
        elif begFunc == "6":
            func = input("Input a function to be used for the list in python notation using x as a variable: ")
            parameter1 = input("enter the lowest value the function should evaluate: ")
            parameter2 = input("enter the highest value the function should evaluate: ")
            evalPermis = {'sqrt' : sqrt, 'abs' : abs}
            func1 = func.replace("x", parameter1)
            linList = linkedList(eval(func1, {}, evalPermis))
            for x in range(int(parameter1) + 1, int(parameter2)+1):
                func1 = func.replace("x", str(x))
                funcSum = eval(func1, {}, evalPermis)
                linList.append(funcSum)
                func1 = func
            lists.append(linList)
        elif begFunc == "7":
            end = True
        else:
            print("invalid input, please enter a number 1-7 corresponding to the desired function.")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data):
        nod = self.head
        while nod.next != None:
            nod = nod.next
        nod.next = Node(data)
    
    def printList(self):
        nod = self.head
        while nod:
            print(nod.data)
            nod = nod.next
    
    def insertBeginning(self, data):
        nod = Node(data)
        nod.next = self.head
        self.head = nod

    def insert(self, data, index):
        nod = self.head
        nod1 = self.head
        for i in range(int(index) - 1):
            nod = nod.next
        for i in range(int(index)):
            nod1 = nod1.next
        nod2 = Node(data)
        nod.next = nod2
        nod2.next = nod1
        
    def retrieve(self, index):
        nod = self.head
        for i in range(int(index)):
            nod = nod.next
        return nod
        
    def delete(self, index):
        nod = self.head
        nod1 = self.head
        if index == 0:
            self.head = self.head.next
            return
        for i in range(int(index)):
            nod = nod.next
        for i in range(int(index)-1):
            nod1 = nod1.next
        nod1.next = nod.next
        
    def length(self):
        count = 0
        nod = self.head
        while nod:
            nod = nod.next
            count += 1
        return count

def makeList():
        choice = input("if you want to make a new list, enter: 'new'. If you are done, enter: 'done': ")
        if choice == "new":
            data = input("Enter the first item of the list or 'stop1' to stop: ")
            linList = linkedList(data)
            listEdit(linList, data)
            return linList
        elif choice == "done":
            return 0
        else:
            print("Invalid input, please enter either 'new' or 'done': ")

def listEdit(linList, data):
    while data.upper() != "STOP1":
        method = input("Do you want to append, insert, retrieve, print list, delete or insert at beginning?: ")
        if method.upper() == "STOP1":
            break
        if ((method == "append") or (method == "")):
            data = input("Enter the next item of the list or 'stop1' to stop: ")
            linList.append(data)
        elif method == "insert":
            data = input("Enter the next item of the list or 'stop1' to stop: ")
            index = input("At what index do you want to insert?: ")
            linList.insert(data, index)
        elif method == "insert at beginning":
            data = input("Enter the next item of the list or 'stop1' to stop: ")
            linList.insertBeginning(data)
        elif method == "retrieve":
            index = input("At what index do you want to retrieve?: ")
            ret = linList.retrieve(index)
            print("Retrieved value:", ret.data)
        elif method == "print list":
            linList.printList()
        elif method == "delete":
            index = input("At what index do you want to delete?: ")
            linList.delete(index)
        else:
            data = method
            linList.append(data)

def dotProduct(lists):
    tot = 0
    minLen = min(lists[0].length(), lists[1].length())
    for i in range(minLen):
        tot += float(lists[0].retrieve(i).data) * float(lists[1].retrieve(i).data)
    return(tot)
    
if __name__ == "__main__":
    main()


