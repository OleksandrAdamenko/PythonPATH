import python

print("Hi, Wayfarer! What is your name?")

name = input("My name is ")

print("Welcome to the PythonPATH, ", name, "!", sep="")

keyword = input("Please, input keyword: ")

while (keyword != "Keywords"):
    keyword = input("This keyword is wrong! Please repeat your input: ")

# match keyword:
#     case "keyword":
#         print()

print("Python keywords: ")

for keyword in python.keywords:
    print(keyword)