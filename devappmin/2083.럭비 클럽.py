import sys

while True:
    s = input()
    name, age, weight = s.split()
    age, weight = int(age), int(weight)

    if name == '#' and age == 0 and weight == 0:
        break

    if age > 17 or weight >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")

