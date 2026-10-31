Skill ={"Python","Java", "C++",'Python'}

print("My skills are:", Skill)

RequiredSkill = {"SQL","AI","Java"}

#Returns the common skills between two sets

commonSkill = Skill & RequiredSkill
print("Common skills are:", commonSkill)

#Returns the skills that are in either set, but not both
commonSkill2 = Skill | RequiredSkill
print("Skills that are in either set, but not both:", commonSkill2)

#Frozen set is an immutable version of a set. Once created,
# the elements of a frozen set cannot be changed or modified.

frozen = frozenset(Skill)
print("Frozen set:", frozen)

#Set Operations
#1. union() - Returns a set that contains all items from both sets, without duplicates
commonSkill3 = Skill.union(RequiredSkill)
print("Union of two sets:", commonSkill3)

#2. intersection() - Returns a set that contains the common items between both sets
commonSkill4 = Skill.intersection(RequiredSkill)
print("Intersection of two sets:", commonSkill4)

#3.difference()- Returns a set that contains the items that are in the first set but not in the second set 
commonSkill5 = Skill.difference(RequiredSkill)  
print("Difference of two sets:", commonSkill5)

commonskill6 = RequiredSkill.difference(Skill)
print("Difference of two sets:", commonskill6)

#4.symmetric_difference() - Returns a set that contains the items that are in either set, but not in both sets
commonSkill7 = Skill.symmetric_difference(RequiredSkill)
print("Symmetric difference of two sets:", commonSkill7)

#5.issubset() - Returns True if all items in the first set are there in the second set, otherwise it returns False
commonSkill8 = Skill.issubset(RequiredSkill)
print(commonSkill8) 

#6.add - used to add a value to the set
Skill.add("API")
print("After Adding Skill:", Skill)

#Frozen Set iterating using loop

for Skill in frozen:
    print("Frozen set using loop: ", Skill)