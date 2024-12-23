price = int(input("Enter the price of an item: "))
if price > 1000:
    print("10% Discount.")
elif price > 500:
    print("5% Discount.")
else:
    print("No Discount.")

ask = str(input("Choose between Vegeterian and Non-Vegetarian: "))
if ask == 'vegeterian':
    food1 = str(input("Choose between Salad and Pasta: "))
elif ask == 'non-vegeterian':
    food2 = str(input("Choose between Chicken or Fish: "))

monthly_salary = int(input("Enter the monthly salary of an employee: "))
if monthly_salary > 50000:
    print("High Earner.")
elif monthly_salary <= 50000:
    print("Mid Earner.")
else:
    print("Low Earner.")

num = int(input("ENter any number: "))
if num % 2 == 0:
    if num % 5 == 0:
        print("This number is divisible by both 2 and 5.")
else:
    print("This number is not divisible by 2 and 3.")

marks = int(input("Enter the marks of a student: "))
if marks > 50:
    if marks > 90:
        print("Excellent.")
    elif marks >= 51 and marks <=90:
        print("Good.")
else:
    print("Fail.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
print("The largest number is:", largest)

print("Welcome to the Forest Adventure.")
direction = str(input("Choose between left and right: "))
if direction == 'right':
    print("You fell into a trap. Game Over.")
elif direction == 'left':
    activity = str(input("Choose between explore and rest: "))
    if activity == 'rest':
        print("You were attacked by wild animals. Game Over.")
    elif activity == 'explore':
        print("You found treasure!")

print("Welcome to the Jungle Survival Challenge.")
activity1 = str(input("Choose between search for food and build a shelter: "))
if activity1 == 'build a shelter':
    print("Your shelter collapsed in the rain. Game Over.")
elif activity1 == 'search for food':
    activity2 = str(input("Choose between hunt and gather: "))
    if activity2 == 'hunt':
        print("You were attacked by wild animals. Game Over.")
    elif activity2 == 'gather':
        print("You found enough food. You win!")

print("Welcome to the Space Adventure.")
activity1 = str(input("Choose between land on Mars and fly to Jupiter: "))
if activity1 == 'fly to Jupiter':
    print("Your spaceship crashed. Game Over.")
elif activity1 == 'land on Mars':
    activity2 = str(input("Choose between explore and build a base: "))
    if activity2 == 'build a base':
        print("You ran out of resources. Game Over.")
    elif activity2 == 'explore':
        print("You found alien artifacts. You win!")

print("Welcome to the Haunted Castle.")
activity1 = str(input("Choose between enter the castle and run away: "))
if activity1 == 'run away':
    print("You escaped safely.")
elif activity1 == 'enter the castle':
    activity2 = str(input("Choose between red, green and black: "))
    if activity2 == 'red':
        print("You entered a room full of flames. Game Over.")
    elif activity2 == 'black':
        print("You were captured by ghosts. Game Over")
    elif activity2 == 'green':
        print("You found the treasure. You Win!")

print("Welcome to the Underwater World.")
activity1 = str(input("Choose between dive deeper and surface: "))
if activity1 == 'surface':
    print("You returned safely.")
elif activity1 == 'dive deeper':
    activity = str(input("Choose between search for pearls and chase the fish: "))
    if activity2 == 'chase the fish':
        print("You got lost underwater. Game Over.")
    elif activity2 == 'search for pearls':
        print("You found a rare pearl. You Win!")

print("Welcome to the Pirate Ship Adventure.")
activity1 = str(input("Choose between search for treasure and battle enemy ships: "))
if activity1 == 'search for treasure':
    activity2 = str(input("Choose between dig on the island and explore the cave: "))
    if activity2 == 'explore the cave':
        print("You were trapped inside. Game Over.")
    elif activity2 == 'dig on the island':
        print("You found a hidden treasure chest. You Win!")
elif activity1 == 'battle enemy ships':
    activity3 = str(input("Choose between attack and defend: "))
    if activity3 == 'defend':
        print("You were outnumbered. Game Over.")
    elif activity3 == 'attack':
        print("You won the battle. You Win!")

print("Welcome to the Wizarding World.")
subject = str(input("Choose a subject: 'spells' or 'potions': "))
if subject == 'spells':
    activity1 = str(input("Would you like to 'practice magic' or 'compete in duels': "))
    if activity1 == 'practice magic':
        print("You mastered a powerful spell. You Win!")
    elif activity1 == 'compete in duels':
        print("You lost to a rival wizard. Game Over.")
elif subject == 'potions':
    activity2 = str(input("Would you like to 'brew an elixir' or 'create poison': "))
    if activity2 == 'brew an elixir':
        print("You healed a village. You Win!")
    elif activity2 == 'create poison':
        print("Your potion backfired. Game Over.")
else:
    print("Invalid choice. Please start again.")

print("Welcome to the Cybersecurity Mission.")
mission = str(input("Choose your mission: 'trace the hacker' or 'secure the system': "))
if mission == 'trace the hacker':
    activity1 = str(input("Would you like to 'track their IP' or 'decode their message': "))
    if activity1 == 'track their IP':
        print("You caught the hacker. You Win!")
    elif activity1 == 'decode their message':
        print("The message was a trap. Game Over.")
elif mission == 'secure the system':
    activity2 = str(input("Would you like to 'shut down the server' or 'upgrade the firewall': "))
    if activity2 == 'shut down the server':
        print("The attack was stopped. You Win!")
    elif activity2 == 'upgrade the firewall':
        print("The hacker bypassed it. Game Over.")
else:
    print("Invalid choice. Please start again.")

num = int(input("Enter any number: "))
if num % 2 == 0 and num % 7 == 0:
    print("Double Seven.")
elif num % 2 == 0:
    print("Even.")
elif num % 7 == 0:
    print("Lucky Seven.")
else:
    print(num)

num = int(input("Enter any number: "))
if num > 100:
    print("Big Number.")
elif num >= 50 and num <= 100:
    print("Medium Number.")
elif num < 50:
    print("Small Number.")
else:
    print("No Number.")

color = str(input("Choose between Red, Yellow, Green: "))
if color == 'red':
    print("Stop")
elif color == 'yellow':
    print("Slow Down")
elif color == 'green':
    print("Go")
else:
    print("Invalid Signal.")

celsius = int(input("Enter the temperature in celsius: "))
if celsius >= 40:
    print("Hot.")
elif celsius >= 20 and celsius <= 39:
    print("Warm.")
elif celsius < 20:
    print("Cold.")
else:
    print("Invalid Celsius")

BMI = float(input("Enter the weight of a person in BMI: "))
if BMI < 18.5:
    print("Underweight.")
elif BMI >= 18.5 and BMI < 24.9:
    print("Normal Weight.")
elif BMI >= 25 and BMI < 29.9:
    print("Overweight.")
elif BMI >= 30:
    print("Obesity.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    sum = num1 + num2
    print(f"Sum is {sum}")
elif num1 % 2 == 0:
    diff = num1 - num2
    print(f"Difference is {diff}")
else:
    mul = num1 * num2
    print(f"Product is {mul}")

price = int(input("Enter the price of a person: "))
if price >= 1000:
    new_price = price * 0.20
    print(f"New Price is {new_price}")
elif price >= 500 and price < 1000:
    new_price2 = price * 0.10
    print(f"New Price is {new_price2}")
elif price < 500:
    print(f"No discount. So {price}")

age = int(input("Enter the age of a person: "))
gender = str(input("Choose the gender: "))
income = int(input("Enter the income of a person: "))
if age >= 18 and age < 60:
    if gender == 'M':
        if income >= 1000000:
            print("Tax 30%.")
        elif income >= 500000 and income < 1000000:
                print("Tax 20%.")
        elif income <= 500000:
                    print("Tax 10%.")
    elif gender == 'F':
        if income >= 1000000:
            print("Tax 25%..")
        elif income >= 500000 and income < 1000000:
                print("Tax 15%.")
        elif income <= 500000:
                    print("Tax 5%.")
elif age >= 60:
    if gender == 'M' or gender == 'F':
        if income > 1000000:
            print("Tax 20%.")
        elif income <= 1000000:
            print("Tax 10%.")
        
age = int(input("Enter your age: "))
gender = str(input("Enter your gender: "))
score = int(input("Enter your academic score (out of 100): "))
if 18 <= age <= 25:
    if gender == 'M':
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender == 'F':
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
else:
    print("Age not within the eligible range.")

age = int(input("Enter your age: "))
gender = str(input("Enter your gender: "))
experience = int(input("Enter your experience (years): "))
if 21 <= age <= 35:
    if gender == 'M':
        if experience >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == 'F':
        if experience >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
elif age > 35:
    print("Manager Role")
else:
    print("Age not within the eligible range.")

age = int(input("Enter your age: "))
gender = str(input("Enter your gender: "))
show_type = str(input("Enter the show type ('Matinee'/'Evening'): "))
if age < 12:
    if show_type == 'Matinee':
        print("Ticket = Rs500")
    elif show_type == 'Evening':
        print("Ticket = Rs700")
elif 12 <= age < 60:
    if gender == 'M':
        if show_type == 'Matinee':
            print("Ticket = Rs800")
        elif show_type == 'Evening':
            print("Ticket = Rs1000")
    elif gender == 'F':
        if show_type == 'Matinee':
            print("Ticket = Rs700")
        elif show_type == 'Evening':
            print("Ticket = Rs900")
elif age >= 60:
    print("Ticket = Rs600")
else:
    print("Invalid input.")

age = int(input("Enter your age: "))
gender = str(input("Enter your gender: "))
membership_type = str(input("Enter the membership type ('Monthly'/'Yearly'): "))
if 18 <= age < 30:
    if gender == 'M':
        if membership_type == 'Monthly':
            print("Membership fee = Rs50")
        elif membership_type == 'Yearly':
            print("Membership fee = Rs500")
    elif gender == 'F':
        if membership_type == 'Monthly':
            print("Membership fee = Rs45")
        elif membership_type == 'Yearly':
            print("Membership fee = Rs450")
elif 30 <= age <= 50:
    if membership_type == 'Monthly':
        print("Membership fee = Rs60")
    elif membership_type == 'Yearly':
        print("Membership fee = Rs600")
elif age > 50:
    if membership_type == 'Monthly':
        print("Membership fee = Rs40")
    elif membership_type == 'Yearly':
        print("Membership fee = Rs400")
else:
    print("Invalid input.")

