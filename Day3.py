#Conditional Statement
'''
score  = int(input("Enter your marks : "))

if score >= 90 and score <= 100 :
    print("Your grade is A+")
elif score > 100:
    print("Invalid marks")
elif score >=80 :
    print("Your grade is B")
elif score >=70 :
    print("Your grade is C")
else :
    print("Your are Fail")
'''

#Nested Condition

age = int(input("Enter your age : "))

Pro = input ("Enter your subscription plan: ")      

if age >=18:
    if Pro:
        print("Full Access")
    else:
        print("Learning Mode only")
else: 
    print("You are eligble for Junior program content")

#Ternary Condition 
'''
Ternary condition is a shorthand way of writing an if-else statement in a single line.
It allows you to assign a value to a variable based on a condition.
'''

Status = "adult" if age >=18 else "minor"
print(Status)
