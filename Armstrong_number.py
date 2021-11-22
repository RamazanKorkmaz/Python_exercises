while True:
    number = input("Enter a positive number: ")
    armstrong = 0
    if number.isdigit():
        if int(number) > 0:
            for i in range(len(number)):
                armstrong += pow(int(number[i]), len(number))
            break
    else:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue

if int(number) == armstrong:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")


