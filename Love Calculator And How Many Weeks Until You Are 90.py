
user_age = int(input("How many weeks do you have until you're 90? "
                 "Please enter your age and find out.\n "))

def life_in_weeks(age):
    if age < 90:
      diff = 90-age
      weeks =  diff * 52.143
      print(f"You have {weeks} weeks left.")

life_in_weeks(user_age)


user_name1 = input("Welcome to the love compatibility calculator. "
                   "Please enter your first name.\n ")
user_name2 = input("Please enter your second name.\n ")

def calculate_love_score(name1, name2):

    score1 = 0
    score2 = 0

    for char in name1.lower():
        if char in "true":
            score1 += 1
        if char in "love":
            score2 += 1

    for char in name2.lower():
        if char in "true":
            score1 += 1
        if char in "love":
            score2 += 1

    score1 *= 10
    score1 += score2
    love_score = score1
    if love_score <= 50:
        print("That is a low score. Your relationship is doomed.")
    elif love_score < 79:
        print("Your a good match.")
    else:
        print("You are perfect together.")

    print(love_score)


calculate_love_score(user_name1, user_name2)