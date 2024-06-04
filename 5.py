num1 = int(input("Please enter the first number: "))
num2 = int(input("Now the second one: "))
sym = input("Now enter the symbol: ")

if (sym == '+'):
    print(f"{num1} + {num2} = {num1 + num2}")
elif(sym == '-'):
    print(f"{num1} - {num2} = {num1 - num2}")
elif(sym == "*"):
    print(f"{num1} * {num2} = {num1 * num2}")
else:
    if (num2 == 0):
        print("You can't divide number by zero")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
