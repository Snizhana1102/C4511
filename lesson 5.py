import colorama

age = 15
name = "John"
weight = 45.4
is_student = True

print(f"{name} is {type(name)}")
print(f"{age} is {type(age)}")
print(f"{weight} is {type(weight)}")
print(f"{is_student} is {type(is_student)}")

for _ in dir(name):
    print(_)

help(str)