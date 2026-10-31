'''
Loop
'''

for i in range (1,10):
    print(i)

my_list = ["python", "java", 100, "False"]
my_values =["apple", "banana", "cherry","orange","mango"]

my_dict2= {}

for i in my_list:
    print(i)

my_dict = {"name":"Vinod", "age": 10, "city":"Hyderabad"}
for key in my_dict:
    print(key,":",my_dict[key])

for i in range(min(len(my_list), len(my_values))):
    my_dict2[my_values[i]]= my_list[i]

print(my_dict2)

