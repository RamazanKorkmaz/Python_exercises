while True:
    number = input("enter a positive number: ")
    prime = False
    divisors_list = []
    if number.isdigit():
        for i in range(1, int(number) + 1):
            if int(number) % i == 0:
                divisors_list.append(i)
        if 1 and int(number) in divisors_list and len(divisors_list) < 3:
            prime = True   # there are max. 2 divisors for a prime number. one of them is 1 the other one is the number
        break
    else:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue

if prime:
    print("{} is a prime number ".format(number))
else:
    print("{} is NOT a prime number ".format(number))