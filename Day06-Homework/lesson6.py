"""გავაკეთოთ სიმულაცია სადაც მომხმარებელს შეეძლება რეგისტრაცია, მომხმარებელი შემოიტანს 3 ცვლადს, სახელი, გვარი, ასაკი (int ფუნქცია არ არის სავალდებულო ასაკთან) საბოლოოდ ამ ყველაფერს print'ის მეშვეობით გამოიტანთ ტერმინალში."""

#declare login variables
first_name = input("your first name :")
last_name = input("your last name :")
gmail = input("your gmail :")
age = input("how old are you :")

#print declared variables
print("your first name is :",first_name,"your last name is :",last_name,
      "your gmail :",gmail,"your age is :",age,)

"""მომხმარებელს შემოატანინეთ 3 რიცხვი. შეინახეთ ისინი ცვლადებში და მათზე ცალცალკე გამოიტანეთ print'ის მეშვეობით გამრავლება, გაყოფა, მიმატება, გამოკლება. (თუ არ იცით კონკრეტული მათემატიკური ოპერაციები დასერჩეთ google'ში. e.g: how to multiply numbers in python)"""

#declaring number variables
first_number = int(input("first number is :"))
second_number = int(input("second number is :"))
third_number = int(input("third number is :"))

#declare + - * / variables
example1 = first_number + second_number + third_number
example2 = first_number - second_number - third_number
example3 = first_number * second_number * third_number
example4 = first_number / second_number / third_number

#print every declared variable
print(example1,example2,example3,example4)