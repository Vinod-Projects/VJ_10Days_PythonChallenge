'''
Data Types
'''
'''
1.Numbers - (int- 10, 20.-30.45 :: float - 20.0, 30.43,45.67 :: complex - 2+3j, 4+5j)
'''    
#number
a =10

''' 
2.String - "Python", 'Programming', "10 Days of Code"
'''
#String
b= "Python"
'''
## 3. List = [value1, value2, value3, value4, value5,....] ##
List - Any data type can be stored in a List ex: [1, 2, 3, 4, 5], ["Python", "Programming", "10 Days of Code"], [1, "Python", 3.14, True]
it will be called with postion of index starting from 0,1,2,3,4,5
For example, if you have a list called my_list = [1, 2, 3, 4, 5],
 you can access the first element of the list using my_list[0], which will return 1.
   Similarly, you can access the second element using my_list[1], which will return 2, and so on.
'''
#List
list = [1, 2, 3, 4, 5, "Python", 3.14, True]
'''
## 4. Dict = { key: Value, key: Value, key: Value} ##
Dict - A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.
Here Key is immutable and Value is mutable. 
In Python, dictionaries are defined using curly braces {} and the key-value pairs are separated by colons (:).
For example, you can create a dictionary called my_dict = {"name": "John", "age": 30, "city": "New York"}.
You can access the values in a dictionary using their corresponding keys. 
For example, you can access the value of the "name" key in my_dict using my_dict["name"], which will return "John".
You can also add new key-value pairs to a dictionary using the assignment operator (=).

'''

#Dictionary
dict = {"name": "Vinod", "age": 30, "city": "Hyderabad"}
'''
5. tuple = (value1, value2, value3, value4, value5,....) ##
Tuple - A tuple is an ordered collection of elements, similar to a list,
but unlike lists, tuples are immutable, meaning that their elements cannot be changed after they are created.  
tupleas are defined using parentheses () and the elements are separated by commas (,).
For example, you can create a tuple called my_tuple = (1, 2, 3, 4, 5). 
You can access the elements of a tuple using their index positions, just like you would with a list.                      

'''

#Tuple
tuple = (1, 2, 3, 4, 5)
'''
6. Set = {value1, value2, value3, value4, value5,....} ##
Set - A set is an unordered collection of unique elements, meaning that it cannot contain duplicate values.
Sets are defined using curly braces {} or the set() constructor, and the elements are separated by commas (,).
For example, you can create a set called my_set = {1, 2, 3, 4, 5}.
You can perform various operations on sets, such as union, intersection, and difference, using built    -in set methods or operators.   
Set s are commonly used in Python for tasks such as removing duplicates from a list or checking for membership in a collection of values.
Sets are also useful for performing mathematical operations on collections of data, such as finding the intersection or union of two sets.
Sets are also commonly used in data analysis and machine learning applications, where they can be used to represent unique values in a dataset or to perform set operations on different subsets of data.
Sets are also used in Python for tasks such as filtering data, finding unique values, and performing set operations on collections of data.
Set is mutable, meaning that you can add or remove elements from a set after it has been created.    

'''
#Set
set = {1, 2, 3, 4, 5}
'''
7. boolean = True or False ##
Boolean - A boolean is a data type that can have one of two values: True or False
'''
#Boolean
boolean = True or False

print("The value of a is:", a)
print("The value of b is:", b)
print("The value of list is:", list[2])
print("The value of dict is:", dict["age"])  
print("The value of tuple is:", tuple[3])
print("The value of set is:", set)  









