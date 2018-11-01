age = int(input("How old are you? "))
if age < 5:
    print(str(age) + "?, " + "You are in preschool")
elif age == 5:
    print(str(age) + "?, " + "You are in kindergarten")
elif age > 5 and age < 18:
    print(str(age) + "?, " + "You are in school")
elif age > 18 and age < 99:
    print(str(age) + "?, " + "No school for you!")
else:
    print("I guess you're an anomaly!")