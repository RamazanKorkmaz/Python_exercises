trapped_water = 0
user_input = []
while True:
    high_of_terrain = input("Type 'ok' when you are done: ")
    if high_of_terrain.lower() == "ok":
        break
    else:
        user_input.append(high_of_terrain)
print(f"user input: ", user_input)
left = []
right = []
max_left = user_input[0]
max_right = user_input[-1]

for i in range(len(user_input)):
    if max_left < user_input[i]:
        max_left = user_input[i]
        left.append(max_left)
    else:
        left.append(max_left)
print(f"from left side: ", left)
user_input.reverse()

for i in range(len(user_input)):
    if max_right < user_input[i]:
        max_right = user_input[i]
        right.append(max_right)
    else:
        right.append(max_right)
right.reverse()
print(f"from right side: ", right)

for i in range(len(user_input)):
    height = min(left[i],right[i])
    trapped_water = trapped_water + int(height) - int(user_input[i])
print(f"the amaunt of water in terrain: ", trapped_water)

