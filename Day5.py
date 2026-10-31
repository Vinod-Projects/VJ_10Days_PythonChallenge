'''
List Methods:
'''
my_SampleList = ['apple', 'banana', 'cherry', 'orange', 'mango']
print(my_SampleList)

'''
1. append() - Adds an element at the end of the list    
'''
my_SampleList.append('kiwi')
print("Appended List: ", my_SampleList)
'''
2. clear() - Removes all the elements from the list
'''
my_SampleList.clear()
print("Cleared List: ", my_SampleList)

'''
3. copy() - Returns a copy of the list
'''
my_SampleList2 = ['apple', 'banana', 'cherry', 'orange', 'mango','apple']
my_SampleList = my_SampleList2.copy()
print("Copied List: ", my_SampleList)

'''
4. count() - Returns the number of elements with the specified value
'''
print("Count of 'apple': ", my_SampleList.count('apple'))

'''
5. extend() - Add the elements of a list (or any iterable), to the end
'''
my_SampleList3 =['kiwi', 'grapes']
my_SampleList.extend(my_SampleList3)
print("Extended List: ", my_SampleList)

'''
6. index() - Returns the index of the first element with the specified value
'''
print("Index of Kiwi:", my_SampleList.index('kiwi'))
'''
7. insert() - Adds an element at the specified position
'''
my_SampleList.insert(3,'watermelon')
print("List after insertion: ", my_SampleList)
'''
8. pop() - Removes the element at the specified position
'''
my_SampleList.pop(3)
print("List after popping:", my_SampleList)

'''
9. remove() - Removes the first item with the specified value
'''
my_SampleList.remove('kiwi')
print("List after removing 'kiwi':", my_SampleList)
'''
10. reverse() - Reverses the order of the list
'''
my_SampleList.reverse()
print("Reversed List: ", my_SampleList) 
'''
11. sort() - Sorts the list
'''
my_SampleList.sort()
print("Sorted List: ", my_SampleList) 
'''
12. len() - Returns the length of the list
'''
my_SampleListLength = len(my_SampleList)
print("Length of the List: ", my_SampleListLength)
'''
13. min() - Returns the smallest item in the list
'''
my_SampleListMinValue =min(my_SampleList)
print("Minimum value in the List: ",my_SampleListMinValue)
'''
14. max() - Returns the largest item in the list
'''
my_SampleListMaxValue =max(my_SampleList)
print("Maximum value in the List: ",my_SampleListMaxValue)

'''         
15. sum() - Returns the sum of all items in the list
'''
my_SampleList4 = [1,2,3,4,5]
print("Sum of all items in the list: ",sum(my_SampleList4))
'''
16. sorted() - Returns a sorted list
'''
my_SampleList5 = ['banana', 'cherry', 'apple', 'mango']
print("Sorted List: ",sorted(my_SampleList5))
'''
17. list() - Converts an iterable (tuple, string, set, dictionary) to a list
18. any() - Returns True if any item in the list is True
19. all() - Returns True if all items in the list are True  
20. enumerate() - Returns an enumerate object
21. filter() - Returns an iterator where the items are filtered through a function
22. map() - Returns an iterator where the items are modified through a function
23. reduce() - Applies a rolling computation to sequential pairs of values in a list
24. zip() - Returns an iterator of tuples, where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
25. reversed() - Returns a reversed iterator
26. slice() - Returns a slice object
27. iter() - Returns an iterator object
28. next() - Retrieves the next item from the iterator
29. isinstance() - Returns True if the specified object is of the specified type
30. type() - Returns the type of the specified object
31. id() - Returns the identity of the specified object
32. dir() - Returns a list of the specified object's properties and methods
33. help() - Invokes the built-in help system
34. globals() - Returns a dictionary of the current global symbol table
35. locals() - Returns a dictionary of the current local symbol table
36. eval() - Evaluates a specified expression

'''