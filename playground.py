# number_of_years =10
# purchase_price=10000
# price_per_gallon=4
# annual_miles_driven=15000
# fuel_efficiency = 20

# annual_fuel_consumed= annual_miles_driven/fuel_efficiency
# annual_feul_cost= price_per_gallon * annual_fuel_consumed
# operating_cost = number_of_years * annual_feul_cost
# total_cost= purchase_price + operating_cost

# print(f'The price of a car is  {total_cost}')

# a= 45
# b= 10

# sum = a+b
# difference = a-b
# product = a*b
# division = a/b

# print(sum ,difference)



# bookPrice=float(input("Enter Price of the Book:"))
# print(f'Price of the Book= {bookPrice}')
# shippingCharges=int(input("Enter Shipping charges:"))
# print(f'Shipping Charges={shippingCharges}')
# totalCost=bookPrice+shippingCharges

# print (f'The Total Charges Are:{totalCost}')


# Name='Aaqib'
# print(Name[2])

# m = stack()
# m.push('x')
# m.peek()

# a=int(input("enter first Numebr:"))
# b=int(input("enter second Numebr:"))
# if a>b:
#     print("aahh")
# elif a==b:
#     print("bahh")
# else:
#     print('jahh')

# i=0
# while i<6:
#     print('aaqib')
#     i+=1

# **** L A B - 0 7 *****
# capital =0
# names='aAQib'
# for i in names:
#     print(i)
#     if i == 'A':
#         capital=capital +1
# print (f"The Number of Capitals:{capital}")

# def sum(a,b):
#     addition = a+b
#     return addition

# a=int(input("Enter First number:"))
# b=int(input("Enter second number:"))

# result=sum(a,b)
# print(result)

# for i in range(1,5):
#     print(2)

# def fact(a):
#     f=1
#     for i in range(a):
#         f*=a
#     return f
# a=int(input('Enter a Number to Find its factorial:'))
# print(fact(a))

# names=['Aaqib','Aizaz','Anfal']
# for x in range(len(names)):
#     print(names[x])

# stack =[]
# stack.append(10)
# print(stack)

# class myClass:
#     x =5
# p1 = myClass()
# print(p1.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# class studentData:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(self.marks)

# aaqib=studentData('Aaqib',23,100)
# aaqib.display()

# import collections
# stack =collections.deque()
# stack
# stack.append(10)
# stack.append(20)
# print(stack)
# stack.pop()
# print(stack)

# stack = []


# while True:

#     print("1: Push")
#     print("2: Pop")
#     print("3: Quit")

#     def empty():
#         if len(stack) == 0:

#             print("Stack is Empty")

#     var = int(input('Enter your choice from 1 to 3 : '))

#     if var == 1:
#         val1 = input("Enter element you want to add : ")
#         stack.append(val1)
#         print(stack)
#     elif var == 2:

#         if len(stack) != 0:
#             val2 = stack.pop()
#             print(val2)


#         else:
#             empty()
#     elif var == 3:
#         print("you are quit")
#         break
        
# stack = []

# while True:
#     def empty():
#         if len(stack)==0:
#             print("empty")
#     print("1:push an element")
#     print('2:Pop an element')
#     print('3:Exit')
#     var = int (input('Choose an option:'))
    
#     if var ==1:
#         val1=input("Enter an Element")
#         stack.append(val1)
#         print(stack)
#     elif var==2:
#         if len(stack)!=0:
            
#             val2=stack.pop()
#             print(val2)
#         else:
#             empty()
#     elif var == 3:
#         print('Exited')
#         break
        

# class stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,item):
#         self.items.append(item)

# class Stack:
#         def __init__(self):
#             self.items = []

#         def isEmpty(self):
#             return self.items == []

#         def push(self, item):
#             self.items.append(item)

#         def pop(self):
#             return self.items.pop()

#         def peek(self):
#             return self.items[len(self.items)-1]

#         def size(self):
#             return len(self.items)

# #from pythonds.basic.stack import Stack

# def divideBy2(decNumber):
#     remstack = Stack()

#     while decNumber > 0:
#         rem = decNumber % 2
#         remstack.push(rem)
#         decNumber = decNumber // 2

#     binString = ""
#     while not remstack.isEmpty():
#         binString = binString+ str()

# class stack:
#     def __init__(self,data=None):
#         self.data = data

#     def push(self,data):
#         self.data.append(data)

#     def pop(self,data):
#         return self.data.pop()
#     def show(self):
#         return self.data
# aaqib=stack()
# aaqib.push(8)
# aaqib.show()

class Stack:
    def __init(self):
        self.elements=[]
    def push(self,data):
        self.elements.append(data)
        return data

    def pop(self):
        self.elements.pop(data)
        return data
    def peek(self):
        return self.elements=[-1]
    def is_empty(self):
        return len(self.elements)==0