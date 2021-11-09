#enter "Yes" or "No" to the questions
age = input("Are you a cigarette addict older than 75 years old: ")
chronic = input("Do you have a severe chronic disease: ")
immune = input("Is your immune system too weak: ")
if age.title() == "Yes" or chronic.title() == "Yes" or immune.title() == "Yes":
    print("You are in risky group")
else: print("You are not in risky group")