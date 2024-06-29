# 1) დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)
# If the age is less than 18, print "You are a minor."
# If the age is between 18 and 65, print "You are an adult."
# If the age is 65 or older, print "You are a senior citizen."

age = int(input("please enter youre age:"))

if age < 18:
    print("you are a minor")
elif age >= 18 and age < 65:
    print("you are an adult")
else:
    print("you are a senior citizen")

# 2) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი. გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი.

for i in range(5):
    number = int(input("please enter number:"))

    if number % 2 == 0:
        print(number,"is even")
    else:
        print(number,"is eve")


# 3) დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
# If the grade is A, print "Excellent!"
# If the grade is B, print "Good job!"
# If the grade is C, print "You passed."
# If the grade is D, print "You can do better."
# If the grade is F, print "You failed."

grade = input("please enter your grade(A,B,C,D,F):")

if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good job")
elif grade == "C":
    print("You passed")
elif grade == "D":
    print("You can do better")
elif grade == "F":
    print("You failed")


# 4) დაწერეთ პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე while ციკლის გამოყენებით
    
num = 1 

while num < 10:
    print(num)
    num = num + 1

# 5) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს

import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    print("Sorry, that's not the correct number. Try again.")


# 6) დაწერეთ პროგრამა, რომელიც დაბეჭდავს მოცემული რიცხვის (მაგ 5) პირველ 10 ჯერადს for loop-ის გამოყენებით.
print("This program will print the multiples of the number you enter")

num = int(input("please enter first number:"))


for i in range(1, 10 + 1):
     sum = num * i
     print(sum)



# 7) შექმენით პროგრამა, რომელიც ბეჭდავს უკუთვლას 10-დან 1-მდე for loop-ის გამოყენებით.
    
i = 10

for x in range(10):
    print(i)
    i = i - 1
