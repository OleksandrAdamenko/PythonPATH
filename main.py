import python

print("Hi, Wayfarer! What is your name?")

name = input("My name is ")

print("Welcome to the PythonPATH, ", name, "!", sep="")

keyword = input("Please, input keyword: ")

match keyword:
    case "Keywords":
        print("Python keywords: ")

        for keyword in python.keywords:
            print(keyword)

# while (keyword != "Keywords"):
#    keyword = input("This keyword is wrong! Please repeat your input: ")

# print("Python keywords: ")

# for keyword in python.keywords:
#     print(keyword)