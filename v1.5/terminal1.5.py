import time
print("This is Terminal v1.4")
print("Type 'Help' for commands")
while True:
    text = input("")
    text = text.lower()
    if text == "print":
        text = input("print what? ")
        print(text)
    elif text == "join":
        num1 = input("join what? ")
        num2 = input("to what? ")
        print(num1 + num2)
    elif text == "time":
        print (time.strftime("%H:%M:%S"))
    elif text == "add":
        num1 = input("add what? ")
        num2 = input("to what? ")
        text = num1 + num2
        num =(str(text).isnumeric())
        if num == True:
            text = int(num1) + int(num2)
            print(text)
        else:
            print("NaN")
    elif text == "minus":
        num1 = input("minus from what? ")
        num2 = input("minus what? ")
        text = num1 + num2
        num =(str(text).isnumeric())
        if num == True:
            text = int(num1) - int(num2)
            print(text)
        else:
            print("NaN")
    elif text == "multiply":
        num1 = input("multiply what? ")
        num2 = input("by what? ")
        text = num1 + num2
        num =(str(text).isnumeric())
        if num == True:
            text = int(num1) * int(num2)
            print(text)
        else:
            print("NaN")
    elif text == "div":
        num1 = input("divide what? ")
        num2 = input("into what? ")
        text = num1 + num2
        num =(str(text).isnumeric())
        if num == True:
            text = int(num1) / int(num2)
            print(text)
        else:
            print("NaN")
    elif text == "power":
        num1 = input("what? ")
        num2 = input("to the power of ")
        text = num1 + num2
        num =(str(text).isnumeric())
        if num == True:
            text = int(num1) ** int(num2)
            print(text)
        else:
            print("NaN")
    elif text == "exit":
        print("Good Bye!")
        exit()
    elif text == "help":
        print('''Commands:
Print
Join
Time
Add
Minus
Multiply
Div
Power
Exit
''')