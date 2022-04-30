# #python strings
course = "python for beginners"
print(course.find('n'))
course.upper()
print(course.upper())
print(course.title())
print([5])
#IF,elseif,else IS USED TO MAKE CONDITION
temperature = 30
if temperature > 30:
    print("Its a hot day")
    print("drink a lot of water")
elif temperature > 20:
    print("its a nice day")
elif temperature < 10:
    print("its a bit cold")
else:
    print("its cold")
    print("Done")
weight = int(input("weight: "))
unit = input("(k)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))








