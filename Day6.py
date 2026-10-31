#Dictionary is a collection of key-value pairs. Each key is unique and is used to access the corresponding value.
SampleDict ={"Name":"Vinod","Age":35,"City":"Hyderabad"}

#Accessing values from the dictionary using keys
print("Name: ",SampleDict["Name"])
print("Age: ",SampleDict["Age"])
print("City: ",SampleDict["City"])

#Updating the value of Age in the dictionary
SampleDict["Age"]= 30
print("Updated Age: ",SampleDict["Age"])

#Incrementing the value of Age by 5
SampleDict["Age"] += 5
print("Updated Age: ",SampleDict["Age"])

#Adding new key-value pair to the dictionary

SampleDict['Skills'] = ['Python', 'Java', 'C++']

print("Skills: ",SampleDict['Skills'])
print(SampleDict)

SampleDict2 = {"Country":"India","State":"Telangana"}
#Merging two dictionaries using update() method
SampleDict.update(SampleDict2)
print(SampleDict)