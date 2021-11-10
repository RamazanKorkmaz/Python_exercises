len_list = int(input("Enter the length of number list: "))
number_list = []
for i in range(len_list):
    user_inp = int(input(f"enter {i+1}. number: "))
    number_list.append(user_inp)
count = 0
longest = 0
while count < len_list:
    if number_list[count] > longest:
        longest = number_list[i]
    count += 1
print(f"the longest number you entered is {longest}")