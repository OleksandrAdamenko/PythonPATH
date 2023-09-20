keywords = ['True', 'False', 'None', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
            'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

password = input("To read the list of Python keywords you need input password: ")

while (password != "Python"):
    password = input("Your password is wrong! Please repeat your input: ")

print("Python keywords: ")

for keyword in keywords:
    print(keyword)