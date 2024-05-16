# 1. Dictionary

# dict1={"a": 10,"b": 20,"c": 30, "d":[1,2,3,4,5]}

# print(dict1["d"])
# dict1["a"]=11
# print(dict1)

# print()

# 2. Sets
# set is unordered and mutable

# set1={20, 'jecrc', 99.9}
# print(set1)

## type casting
# set(), int(), float(), bool(), list(), tuple()
# list1=[1,1,2,2,3,3,4,4,5,5]
# print(set(list1))

# # you can't add duplicate elements in set.
# set2={1,1,2,2,3,3,4,4,5,5}
# print(set2)

# set2.add(100)
# print("After adding 100: ",set2)

# set2.remove(100)
# print("After removed: ", set2)

# set2.discard(100)
# print(set2)

# set2.remove(10) - it gives you an error.
# print(set2)

# set2.discard(10) - it doesn't give you an error.
# print(set2)

# 3. OPERATORS

## Arithmetic operators.

# num1= input("enter first num: ")
# num2= input("enter second num: ")
# print(num1 + num2)  # it's a string.

# num1= int(input("enter first num: "))
# num2= int(input("enter second num: "))
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2) #it gives you the remiander
# print(num1 ** num2) #num1^num2
# print(num1 // num2) #no decimals

## Comparison operators
# >,<,==,!=,>=,<=
## Conditional statement
# if, else, elif

# num1= int(input("enter first num: "))
# num2= int(input("enter second num: "))

# if num1 > num2:
#     print("number 1 is greater than number 2.")

# # elif num1==num2: 
# #     print("both numbers are equal.")

# elif num1!=num2:
#     print("not equal.")

# else:
#     print("number 2 is greater than number 1.")

# if num1%2==0:
#     print("it's an even number.")

# else:
#     print("it's an odd number.")

## Logical operators
# and, or, not

# age = int(input("enter your age:"))
# gender= input("enter your gender:")

# if age>18  and age<100 and gender=="male" or gender=="female":
#     print("You can vote.")

# else:
#     print("You can't vote.")

## Assignment operators
# =, +=, -= etc

# num = 10
# num += 1  # num = num + 1
# num -= 2  # num = num - 2
# num *= 3  # num = num * 3
# print(num)

## Membership operators
# in, not in

# colors=['white', 'black', 'yellow', 'red']
# if 'white' in colors:
#     print("it is available.")

# else:
#     print("it is not available.")

# print('white' in colors)
# print("violet" in colors)
# print('violet' not in colors)
# print('white' not in colors)

# 4. LOOPS

for i in range(1) :
    n = 0
    a=int(input("range:"))
    for a in range(a):
     n+=1
     print(n)