"batoni data tezelashvilis davalebebi:"

"while ციკლის დავალებები:"

"""Timer: დაწერეთ პროგრამა, რომელიც ითვლის 10-დან 1-მდე, დაბეჭდავს თითოეულ რიცხვს და შემდეგ დაბეჭდავს "დრო ამოიწურა"."""

i = 10

while i >= 1:
    print(i)
    i = i - 1
print("time is up")

"""რიცხვების ჯამი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვებს განუწყვეტლივ, სანამ ისინი არ შეიყვანენ 0-ს. შემდეგ დაბეჭდეთ ყველა შეყვანილი რიცხვის ჯამი."""

num = int(input("please enter number: "))

sum = 0 
i = 0

while num != i:
     sum = sum + num 
     num = int(input("please enter number:")) 
     print("sum of numbers",sum)   


"""პაროლის შემოწმება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. განაგრძეთ კითხვა, სანამ სწორი პაროლი არ იქნება შეყვანილი. დავუშვათ, რომ სწორი პაროლი არის "12345678".""" 

password = input("please enter password:")

real_password = "12345678" 

while  password != real_password:
     print("password is incorect please try again")
else:
     print("thanks")

"""ლუწი რიცხვები: დაწერეთ პროგრამა, რომელიც ბეჭდავს ყველა ლუწ რიცხვს 0-დან 20-მდე while ციკლის გამოყენებით."""

i = 0

while i <= 20:
     print(i)
     i = i + 2

"""დადებითი რიცხვები: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს უწყვეტად შეიყვანოს დადებითი რიცხვები, სანამ ისინი უარყოფით რიცხვს არ შეიყვანენ. შემდეგ დაბეჭდეთ ყველა შეყვანილი დადებითი რიცხვის ჯამი. 
"""
sum_of_positive_numbers = 0

while True:
    number = float(input("Enter positive number (or  negative number to stop): "))
    
    if number < 0:
        break
    else:
        sum_of_positive_numbers += number

print("Sum of all positive numbers entered:", sum_of_positive_numbers)

"""შეამოწმეთ ლუწია თუ კენტი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს და ბეჭდავს ლუწია თუ კენტი.
"""
i = 1

while i <= 10:
    if i % 2 == 0:
          print(i, "is even")
    else:
         print(i, "is odd")
    print(i)
    i = i + 1

#if statements davalebebi
"""ტემპერატურის კლასიფიკაცია: შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს ტემპერატურას ცელსიუსში. შემდეგ დაბეჭდეთ ცხელი (> 30°C), თბილი (20-30°C) ან ცივი (<20°C)."""

temperature = int(input("please enter temperature:"))

hot_temperature = 30
warm_temperature = range(20, 30 + 1)
cold_temperature = 20

if temperature > hot_temperature:
     print("hot")
if temperature == warm_temperature:
     print("warm")
if temperature <= cold_temperature:
     print("cold")

"""ასოების შეფასება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოცდის ქულას. შემდეგ დაბეჭდეთ მათი ასოების შეფასება შემდეგი სკალის მიხედვით: A (90-100), B (80-89), C (70-79), D (60-69), F (< 60)."""

user_result = int(input("How many points did you get?:1"))

for a in range(90,100 + 1):
    if user_result == a:
        print("you got the highest point")
       

for b in range(80, 90):
    if user_result == b:
        print("you got a high point")


for c in range(70, 80):
    if user_result == c:
        print("you got an average point")

for d in range(60, 70):
    if user_result == d:
        print("you got a low point")

for c in range(0, 60):
    if user_result == c:
        print("you did not pass the point limit")

"""შეამოწმეთ გაყოფა: შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს. შემდეგ დაბეჭდეთ, იყოფა თუ არა 2-ზე, 3-ზე ან ორივეზე."""

number = int(input("enetr your number:"))

if number % 2 == 0 :
    print("divided")
else:
    print("not divided")

if number % 3 == 0:
    print("divided")
else:
    print("not diveded")

"""რიცხვების შედარება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს ორ რიცხვს და შეადარებს მათ."""

num1 = int(input("please enter first number:"))
num2 = int(input("enter second number:"))

if num1 > num2:
    print("is more:")
else:
    print("is less:")

if num1 < num2:
    print("is more:")
else:
    print("is less:")


if num2 < num1:
    print("is more:")
else:
    print("is less")


if num2 > num1:
    print("is more:")
else:
    print("is less:")

#combined 
    
"""რიცხვის გამოცნობა: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი (მაგ., 5, ეს რიცხვი თქვენ აირჩიეთ). განაგრძეთ კითხვა, სანამ არ გამოიცნობენ სწორად.
"""

number = int(input("please enter number:"))

while number != 5:
    number = int(input("please enter number:"))
else:
    print("you win")

"""რიცხვების შემოწმება: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს. სანამ ეს რიცხვი არ იქნება ლუწი, შეეკითხეთ მომხმარებელს თავიდან."""

number = int(input("enter your num:"))

while number % 2 != 0:
    number = int(input("enter your num:"))
else:
    print("this number is even")


"""რიცხვების კლასიფიკაცია: შექმენით პროგრამა, სადაც 50-იდან 100-ის ჩათვლით გამოიტანთ კენტ რიცხვებს. ციკლის გარეთ შექმენით ჯამის ცვლადი, სადაც დაემატება ციკლის ის რიცხვები, რომლებიც მეტია 75-ზე. ბოლოს დაპრინტეთ ამ ცვლადის მნიშვნელობა"""

sum = 0
sum1 = 0
for i in range(50, 100, 3):
    sum += i
    sum1 += sum
    print(i)
print(sum)
print(sum1)

"""რიცხვების შედარება: მომხმარებელს შეეკითხეთ რიცხვი. სანამ ის ნაკლები იქნება მასზე 20-ით დიდ რიცხვზე, დაპრინტეთ ის და მასზე მოახდინეთ იტერაცია 1-ით."""

num = int(input("please enter first number: "))

while num < 20:
    num = num + 1
    print(num)

"""სახელის გამოცნობა. შექმენით ცვლადი სადაც იქნება შენახული თქვენი სახელი. მომხმარებელს შეეკითხეთ სახელი და სანამ თქვენსას არ შემოიტანს თავიდან შეეკითხეთ."""

my_name = "nika"
user = input("please enter name:")

while my_name != user:
    user = input("please enter name again: ")
else:
    print("you win")

#ბატონი ლუკა ცხვარაძის დავალებები

#1   
i = 1

while i <= 10:
    print(i)
    i = i + 1

#2
i = 100

while i >= 0:
    print(i)
    i = i - 1

#3
i = 1

while i <= 10:
    if i % 2 == 0:
          print(i, "is even")
    else:
         print(i, "is odd")
    print(i)
    i = i + 1

#4
i = 1

while i <= 10:
     print(i)
     i = i + 2








