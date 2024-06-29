"""დაწერეთ ალგორითმი რომელიც დაბეჭდავს დადებითია, უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი"""

num = int(input("please enter first number:"))

if num < 0:
    print("number is negative")
if num == 0:
    print("number is = zero")
if num > 0:
    print("number is integer")

"""დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი. მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა, რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა. თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision".
"""
print("1. km - miles")
print("2. miles - km")

choice = int(input("please enter operetion number (1 or 2):"))
number  = float(input("please enter number to convert it:"))

if choice == 1:
    print(number / 1.6)
elif choice == 2:
    print(number * 1.6)
else:
    print("wrong choice:")

"""შექმენით რეგისტრაციის ალგორითმი. მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი და მეილი, საბოლოოდ კი ერთ წინადადებაში გამოიტანეთ მიღებული ინფორმაცია."""

name = str(input("enter your name:"))
surname = str(input("enter your surname:"))
age =str(input("enter your age:"))
mail = str(input("enter your gmail:"))

print(name,surname,age,mail)

"""მომხმარებელს სამჯერ შეეკითხეთ რიცხვითი მნიშვნელობა და დაბეჭდეთ მათი საშუალო არითმეტიკული."""

num1 = int(input("please enter first numebr:"))
num2 = int(input("please enter second:"))
num3 = int(input("please enter third number:"))

result = (num1 + num2 + num3) / 3

print(result)

"""მომხმარებელს შეეკითხეთ 1-იდან 9-ის ჩათვლით რომელიმე რიცხვი. შემდეგ გამოიყენეთ for ციკლი და გამოიტანეთ ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში."""

number = int(input("write any number from 1 to 9 inclusive:"))

for i in range(1, 50, + 1):
    if i % number == 0:
        print(i)

"""მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for ციკლში საწყის, ხოლო უდიდესი საბოლოო მნიშვნელობად გამოიყენეთ. ციკლში იტერაცია მოახდინეთ ერთით და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი)."""

num1 = int(input("enter your first number:"))
num2 = int(input("enter your second number:"))

smallest = min(num1,num2)
largest = max(num1,num2)

for i in range(smallest,largest + 1):
    print(f"the cube of {i} is {i**3}:")

"""მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მისი ციფრთა ჯამი."""


number = input("შეიყვანეთ რიცხვი: ")

total = sum(int(digit) for digit in number if digit.isdigit())

print("ციფრთა ჯამი:", total)

"""დაწერეთ პროგრამა, რომელიც იღებს მომხმარებლისგან მთელ რიცხვს და დაბეჭდავს მის გამრავლების ცხრილს 10-ის ჩათვლით. მაგ: x, x2, x3 ... x*10."""

number = int(input("please enter an integer:"))

for i in range(1,10, + 1):
    print(f"{number} * {i} = {number * i}")

"""შექმენით კალკულატორი, სადაც გექნებათ ოთხი ოპერაცია: + - / და გამრავლება (ფიფქი არ იწერება). მომხმარებელს შეეკითხებით ორ რიცხვს, შემდეგ სასურველ ოპერაციას და დაუბეჭდავთ გამოთვლილ მნიშვნელობას."""

print ("Please select the operation")    
print ("1 - Add")    
print ("2 - Subtract")
print ("3 - Divide")     
print ("4 - Multiply")    
operacion = input("please enter choice: ")


num1 = int(input("enter first number for calculator: "))
num2 = int(input("enter second number for calculator: "))


if operacion == "1" :
    print(num1,"+", num2, "=", num1 + num2)

if operacion == "2" :
    print(num1,"-",num2,"=",num1 - num2)

if operacion == "3" :
    print(num1,"/",num2,"=",num1 / num2)

if operacion == "4": 
    print(num1,"x",num2,"=",num1 * num2)

"""დაწერეთ პროგრამა, რომელიც იღებს სთრინგს, შემდეგ მომხმარებელს ეკითხება თუ რამდენჯერ განმეორდეს და for ციკლის გამოყენებით დაბეჭდეთ ის.
"""
num = input("please enter number: ")
interacion = int(input("how mant times you want interacion:"))
for i in range(interacion):
    print(num)

"""დაწერეთ პროგრამა, რომელიც გამოთვლის სხეულის მასის ინდექსს (BMI), მომხმარებლისგან მიღებული წონის (კილოგრამებში) და სიმაღლის (მეტრებში) გათვალისწინებით. 
"""
height = int(input("please enter your height in meters:"))
weight = int(input("please enter your weight in kg:"))
bmi = weight / height

print("youre bmi =",bmi)

"""მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ ის ნაკიანი არის თუ არა."""
leap_year = "29 february"
user_info = input("please enter your birtyday")

if user_info == leap_year:
    print("You are in a lean year")
else:
    print("You are not in a lean year")

"""დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი 1-დან 5-ის ჩათვლით. თუ რიცხვი არის 1-ზე ნაკლები ან 5-ზე მეტი, დაბეჭდეთ "Invalid input". თუ რიცხვი 1-დან 5-ის ჩათვლითაა, დაბეჭდეთ "Valid input". 
"""

num = int(input("please enter first number in range (1, 5) : "))

if num < 1:
    print("invalid input")
elif num > 5:
    print("invalid input")
else:
    num == range(1, 5 + 1)
    print("valid input")

#პითაგორა
Pythagorean_triple = (3, 4, 5, 6, 8, 10, 7, 24, 25, 12, 13, 20, 21, 29, 15, 17, 99, 101, 48, 55, 73, 144)

num = int(input("Write any number and find out if it is a Pythagorean number or not: "))

if num == Pythagorean_triple:
    print("These are Pythagorean numbers")
else:
    print("These are not Pythagorean numbers")


