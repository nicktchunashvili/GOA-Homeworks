
"""დავალება: მომხმარებელს შემოატანინეთ input-ით ფულის რაოდენობა. თუ ის აღემატება 100-ს, მაშინ დავბეჭდოთ, რომ მას გააჩნია საკმარისი თანხა. სხვა შემთხვევაში კი დავბეჭდოთ რომ საკმარისი თანხა არ აქვს """

money = int(input("please enter money quanity:"))

if money >  100:
    print("you have enought money")
else:
    print("you didnt have enought money")

"""დავალება2: მომხმარებელს შეეკითხეთ საკუთარი ასაკი. თუ ის აღემატება თვრამეტს გამოიტანეთ, რომ სრულწლოვანია. სხვა შემთხვევაში დაბეჭდეთ, რომ არის ბავშვი"""

age = int(input("enter your age:"))

if age > 18:
    print("you are adult")
else:
    print("you arent adult")

"""დავალება: გამოვიტანოთ while ციკლით 0-იდან 20-ის ჩათვლით ყველა ლუწი რიცხვი"""

i = 0

while i <= 20:
    i = i + 2
    print(i)

"""დავალება2: while ციკლით 100-იდან 0-ის ჩათვლით გამოიტანეთ რიცხვები"""

i = 100

while i >= 0:
    print(i)
    i = i - 1


"""დავალება3: 1-იდან 100-ის ჩათვლით გამოიტანეთ რიცხვთა ჯამი"""

i = 1

while i <= 100:
    i = i + 1
    print(i)

"""დავალება4: 50-იდან 100-ის ჩათვლით არსებული 5-ის ჯერადების  ჯამი გამოიტანეთ. გამოიყენეთ while ციკლი"""

i = 50
sum = 0

while i <= 100:
    sum = sum + i
    i = i + 5
print(sum) 


"""დავალება5: მომხმარებელს შემოატანინეთ რიცხვი და სანამ ის ორზე გაიყოფა გაყავით. შემდეგ გამოიტანეთ საბოლოო ვარიანტი"""

num  = int(input("enter number:"))

remained = num % 2

while num % 2 == 0:
    num = num / 2
    print(num)



