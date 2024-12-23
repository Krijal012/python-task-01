#Q) Take the price of an item as input. If the price is more than 1000, apply a 10% discount. Otherwise, check if the price is more than 500 and apply a 5% discount. Print the final price.
    
price = int(input("Enter the price of an item: "))
if price > 1000:
    print("10% Discount.")
elif price > 500:
    print("5% Discount.")
else:
    print("No Discount.")

Q) Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give them options. If vegetarian, ask if they want "Salad" or "Pasta". If non-vegetarian, ask if they want "Chicken" or "Fish".

ask = str(input("Choose between Vegeterian and Non-Vegetarian: "))
if ask == 'vegeterian':
    food1 = str(input("Choose between Salad and Pasta: "))
elif ask == 'non-vegeterian':
    food2 = str(input("Choose between Chicken or Fish: "))

Q) Take an employee's monthly salary as input. If it's more than 50,000, classify as "High Earner". If less than or equal to 50,000, check if it's more than 20,000 to classify as "Mid Earner", else classify as "Low Earner".

monthly_salary = int(input("Enter the monthly salary of an employee: "))
if monthly_salary > 50000:
    print("High Earner.")
elif monthly_salary <= 50000:
    print("Mid Earner.")
else:
    print("Low Earner.")

Q) Take a number as input. Check if it is divisible by 2. If yes, further check if it is divisible by 5. Print appropriate messages for each condition.

num = int(input("ENter any number: "))
if num % 2 == 0:
    if num % 5 == 0:
        print("This number is divisible by both 2 and 5.")
else:
    print("This number is not divisible by 2 and 3.")

Q) Take a student's marks as input. If the marks are more than 50, check if they are greater than 90. If so, print "Excellent". If between 51 and 90, print "Good". Otherwise, print "Fail"

marks = int(input("Enter the marks of a student: "))
if marks > 50:
    if marks > 90:
        print("Excellent.")
    elif marks >= 51 and marks <=90:
        print("Good.")
else:
    print("Fail.")

Q) Write a program to input three numbers and find the largest among them using nested if-else

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

Q) Write a program that starts with a greeting: "Welcome to the Forest Adventure".
 Prompt the user to choose a path: "left" or "right".
 If "left", ask them to pick between "explore" or "rest".
 If "explore", print "You found treasure!".
 If "rest", print "You were attacked by wild animals. Game Over."
 If "right", print "You fell into a trap. Game Over."

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

Q) Write a program starting with "Welcome to the Jungle Survival Challenge".
 Ask the user to "search for food" or "build a shelter".
 If "search for food", ask to choose between "hunt" or "gather".
 If "hunt", print "You were attacked by a wild animal. Game Over."
 If "gather", print "You found enough food. You Win!"
 If "build a shelter", print "Your shelter collapsed in the rain. Game Over."

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

Q) Create a game with the message: "Welcome to the Space Adventure".
 Ask the user to choose "land on Mars" or "fly to Jupiter".
 If "land on Mars", ask if they want to "explore" or "build a base".
o If "explore", print "You found alien artifacts. You Win!"
o If "build a base", print "You ran out of resources. Game Over."
 If "fly to Jupiter", print "Your spaceship crashed. Game Over."

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

Q) Start with "Welcome to the Haunted Castle".
 Ask the user to choose "enter the castle" or "run away".
 If "enter the castle", ask them to choose a door: "red", "green", or "black".
o If "red", print "You entered a room full of flames. Game Over."
o If "green", print "You found the treasure. You Win!"
o If "black", print "You were captured by ghosts. Game Over."
 If "run away", print "You escaped safely."

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

Q) Begin with "Welcome to the Underwater World".
 Ask the user to choose "dive deeper" or "surface".
 If "dive deeper", ask them to "search for pearls" or "chase the fish".
o If "search for pearls", print "You found a rare pearl. You Win!"
o If "chase the fish", print "You got lost underwater. Game Over."
 If "surface", print "You returned safely."

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

Q) Write a program that starts with "Welcome to the Pirate Ship Adventure".
 Ask the user to choose between "searches for treasure" or "battle enemy
ships".
 If "search for treasure", ask whether to "dig on the island" or "explore the
cave".
 If "dig on the island", print "You found a hidden treasure chest. You
Win!"
 If "explore the cave", print "You were trapped inside. Game Over."
 If "battle enemy ships", ask if they want to "attack" or "defend".
 If "attack", print "You won the battle. You Win!"
 If "defend", print "You were outnumbered. Game Over."

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

Q) . Start the program with "Welcome to the Wizarding World".
 Ask the user to choose a subject: "spells" or "potions".
 If "spells", ask them to "practice magic" or "compete in duels".
 If "practice magic", print "You mastered a powerful spell. You Win!"
 If "compete in duels", print "You lost to a rival wizard. Game Over."
 If "potions", ask whether to "brew an elixir" or "create poison".
 If "brew an elixir", print "You healed a village. You Win!"
 If "create poison", print "Your potion backfired. Game Over."

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

Q) Begin with "Welcome to the Cybersecurity Mission".
 Ask the user to "trace the hacker" or "secure the system".
 If "trace the hacker", ask to "track their IP" or "decode their message".
 If "track their IP", print "You caught the hacker. You Win!".
 If "decode their message", print "The message was a trap. Game
Over."
 If "secure the system", ask to "shut down the server" or "upgrade the firewall".
 If "shut down the server", print "The attack was stopped. You Win!"
 If "upgrade the firewall", print "The hacker bypassed it. Game Over."

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

Q) Accept input from the user:
 If the number is divisible by 2 and 7, print "Double Seven".
 If divisible by 2 but not 7, print "Even".
 If divisible by 7 but not 2, print "Lucky Seven".
 Otherwise, print the number as is.

num = int(input("Enter any number: "))
if num % 2 == 0 and num % 7 == 0:
    print("Double Seven.")
elif num % 2 == 0:
    print("Even.")
elif num % 7 == 0:
    print("Lucky Seven.")
else:
    print(num)

Q) Accept a number from the user:
 If the number is greater than 100, print "Big Number".
 If the number is between 50 and 100, print "Medium Number".
 If less than 50, print "Small Number".

num = int(input("Enter any number: "))
if num > 100:
    print("Big Number.")
elif num >= 50 and num <= 100:
    print("Medium Number.")
elif num < 50:
    print("Small Number.")
else:
    print("No Number.")

Q) Accept a color from the user:
 If the color is "Red", print "Stop".
 If "Yellow", print "Slow Down".
 If "Green", print "Go".
 Otherwise, print "Invalid Signal".

color = str(input("Choose between Red, Yellow, Green: "))
if color == 'red':
    print("Stop")
elif color == 'yellow':
    print("Slow Down")
elif color == 'green':
    print("Go")
else:
    print("Invalid Signal.")

Q) 8. Accept temperature in Celsius from the user:
 If greater than 40, print "Hot".
 If between 20 and 39, print "Warm".
 If less than 20, print "Cold".

celsius = int(input("Enter the temperature in celsius: "))
if celsius >= 40:
    print("Hot.")
elif celsius >= 20 and celsius <= 39:
    print("Warm.")
elif celsius < 20:
    print("Cold.")
else:
    print("Invalid Celsius")

Q) Accept a BMI value from the user:
 If BMI < 18.5, print "Underweight".
 If 18.5 ≤ BMI < 24.9, print "Normal weight".
 If 25 ≤ BMI < 29.9, print "Overweight".
 If BMI ≥ 30, print "Obesity".

BMI = float(input("Enter the weight of a person in BMI: "))
if BMI < 18.5:
    print("Underweight.")
elif BMI >= 18.5 and BMI < 24.9:
    print("Normal Weight.")
elif BMI >= 25 and BMI < 29.9:
    print("Overweight.")
elif BMI >= 30:
    print("Obesity.")

Q) 0. Accept two numbers from the user:
 If both numbers are even, print their sum.
 If one is even and the other is odd, print their difference.
 Otherwise, print their product.

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

Q) Accept the price of an item from the user:
 If the price is greater than 1000, apply a 20% discount and print the new price.
 If between 500 and 1000, apply a 10% discount.
 If less than 500, no discount.

price = int(input("Enter the price of a person: "))
if price >= 1000:
    new_price = price * 0.20
    print(f"New Price is {new_price}")
elif price >= 500 and price < 1000:
    new_price2 = price * 0.10
    print(f"New Price is {new_price2}")
elif price < 500:
    print(f"No discount. So {price}")

Q) Accept age, gender ('M', 'F'), and income and calculate the tax:
 Age >= 18 and < 60:
o Male:
 Income > 10,00,000: Tax = 30%
 Income between 5,00,000 and 10,00,000: Tax = 20%
 Income <= 5,00,000: Tax = 10%
o Female:
 Income > 10,00,000: Tax = 25%
 Income between 5,00,000 and 10,00,000: Tax = 15%
 Income <= 5,00,000: Tax = 5%
 Age >= 60:
o Male or Female:
 Income > 10,00,000: Tax = 20%
 Income <= 10,00,000: Tax = 10%

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

Accept the age, gender ('M', 'F'), and academic score (out of 100) and determine
eligibility:
 Age >= 18 and <= 25:
o Male:
 Score >= 85: "Full Scholarship"
 Score >= 70: "Partial Scholarship"
 Score < 70: "No Scholarship"
o Female:
 Score >= 80: "Full Scholarship"
 Score >= 65: "Partial Scholarship"
 Score < 65: "No Scholarship"

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

Q) Accept the age, gender ('M', 'F'), and experience (years) and assign a role:
 Age >= 21 and <= 35:
o Male:
 Experience >= 5: "Senior Developer"
 Experience < 5: "Junior Developer"
o Female:
 Experience >= 5: "Senior Analyst"
 Experience < 5: "Junior Analyst"
 Age > 35:
o Male or Female: "Manager Role"

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

Q) Accept the age, gender ('M', 'F'), and show type ('Matinee', 'Evening'):
 Age < 12:
o Male or Female:
 Matinee: Ticket = Rs500
 Evening: Ticket = Rs700
 Age >= 12 and < 60:
o Male:
 Matinee: Ticket = Rs800
 Evening: Ticket = Rs100
o Female:
 Matinee: Ticket = Rs700
 Evening: Ticket = Rs900
 Age >= 60:
o Male or Female: Ticket = Rs600

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

Q) Accept the age, gender ('M', 'F'), and membership type ('Monthly', 'Yearly'):
 Age >= 18 and < 30:
o Male:
 Monthly: Rs50
 Yearly: Rs500
o Female:
 Monthly: Rs45
 Yearly: Rs450
 Age >= 30 and <= 50:
o Male or Female:
 Monthly: Rs60
 Yearly: Rs600
 Age > 50:
o Male or Female:
 Monthly: Rs40
 Yearly: Rs400

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

