#1-LISTS

# list1=[20,35,25.5,'hello',True]
# print(list1)
# print(list1[1])
# print(list1[1:4])
# list1[1]=88
# print(list1)
# print(len(list1))

# list1.append(50) #to add a element at the last of the list.
# print(list1)
# list1.pop()# it removes an element from the last.
# print(list1)

# list1.insert(1,'jecrc')#to insert an item at a particular position.
# print(list1)

# print(list1[3][-1])

# list2=[25,41,63,25.3,[100,200,300]]
# print(list2[4][1])

# list2[4][1]=1000
# print(list2)

# list3=[12,14,25,63,85,95]
# print(list3)
# list3.remove(63) # to remove a specific item from a list.
# print(list3)

# print(list3*2)

# list4=[1,2,3,4,5]
# list5=[6,7,8,9,10]
# list4.append(list5)
# print(list4)
# list4.extend(list5)
# print(list4)

#2-TUPLE

# tuple1=(10,20,30,40,75.5,'jecrc',True)
# print(type(tuple1))
# print(tuple1)
# tuple1[1]=200
# print(tuple1) - tuples can't be changed once they're made beacause they are immutable.

# name=('jecrc') #add a , if you want it to be a tuple.
# print(type(name))

# college_names="jecrc","poornima","skit"
# print(type(college_names))
# print(college_names) # paranthesis or brackets doesn't matter if you have multiple values for your variable.

# tuple2=(10,20,30,40)
# print(tuple2*2)

#3

# name='jecrc '
# surname="foundation"
# roll_no=100

# print(name*2)
# print(name + surname)
# print(name + roll_no) - impossible because both are diff datatypes.

# 4 - DICTIONARY

#dt = { key  : value }

# dict1={"name":"Ajeet singh","branch":"cs-ai","roll_no":8}
# print(dict1)
# print(type(dict1))
# print(dict1["name"]) # it doesn't support indexing.

# print(dict1.keys())
# print(dict1.values())

# dict1["name"]="rajput"
# print(dict1)

# dict2={0:"who",1:"are",2:"you"}
# print(dict2) # the dictionary can be of any datatype.

college_data={"name":["a","b","c","d"],"marks":[8,7,6,3],"sub":["physics","chemistry","maths"]}
print(college_data["name"][0])
print(college_data['marks'])