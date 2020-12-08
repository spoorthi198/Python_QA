'''print("*" * 10)
birth_year = int(input("enter the birth year"))
age = 2020 - birth_year
print(age) '''

#logical operator

'''has_high_income = True
has_high_credit = False

if (has_high_income and has_high_credit):
    print("Eligible for loan")
else:
    print("not eligible for true")'''

''' temerature = 45

if temerature > 30:
    print("It's a hot day")
    print("drink plenty of water")
elif temerature > 20 and temerature <30:
    print("its a nice day")
elif temerature < 10:
    print("its a cold day")
else:
    print("Good day")
'''

# calculating weight in kg and lbs
'''
weight = int(input("enter the weight: ->"))
unit = input("(K)g and (l)bs").upper()
if unit == "K":
    converted = weight/0.45
    print("weight in kg is" + str(converted))
elif unit == "L":
    converted = weight * 0.45
    print("weight in lbs is" + str(converted))
'''

# while example
'''
i = 1
while(i<=10):
    print(i * '*')
    i +=1
'''
# list
'''

names = ["jhon","spoorthi","red","jnana","Raj"]
print(names[0:4])
names.append("keerti")
names.insert(3,"test")
print("Raj" in names)
'''

number = range(5,10,2)
for i in number:
    print(i)