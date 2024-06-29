"""დავალება: შექმენით ორი სია, პირველში საყვარელი ადამიანების სახელები, ხოლო მეორეში ფავორიტი მანქანები ჩაწერეთ. ორივე სიაში 5 ელემენტი უნდა გქონდეთ. თავდაპირველად დაბეჭდეთ ორივე სია, შემდეგ გამოიყენეთ ინდექსები და დაბეჭდეთ კონკრეტული ელემენტები"""

favorite_people_name = [
    "nika",
    "giorgi",
    "luka",
    "mate",
    "saba",
]

favorite_cars_name = [
    "bmw",
    "Lada",
    "mercedes",
    "audi",
    "opel",
]

print("favorite_cars_name",favorite_cars_name)
print("favorite_people_name",favorite_people_name)

print(favorite_cars_name[3])
print(favorite_people_name[0])


"""დავალება: შექმენით ორი სთრინგი, პირველში შეინახეთ თქვენი სახელი, ხოლო მეორეში გვარი. საბოლოოდ გამოიტანეთ თქვენი ინიციალები - სახელის პირველი ასო + . + გვარის პირველი ასო"""

my_first_name = "nika"
my_last_name = "tchunashvili"

print(my_first_name[0],".",my_last_name[0])




"""დავალება:შექმენი სია, სადაც გექნება 1-იდან 10-ის ჩათვლით რიცხვები. შემდეგ ლუწ ინდექსებზე მყოფი ელემენტების ადგილას -1 დაწერე"""


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(num)):
    if i % 2 != 0:
       num[i] = -1

print(num)



"""დავალება: შექმენით ორი სია, უნდა გქონდეთ ორივე განსხვავებული ზომის. len ფუნქციის გამოყენებით გაიგეთ მათი სიგრძე"""

first_list = [5,7,2,4,6,1,8,10]
second_list = [3,4,5,6,7,1]

print(len(first_list))
print(len(second_list))

"""დავალება:len ფუნქციის გამოყენებით გამოიტანეთ თქვენი გვარის ბოლო ასო"""

surname = "tchunashvili"

print(surname[len(surname)-1][-1])

"""დავალება:გააერთიანეთ ერთ სია მეორე სიასთან"""

print(first_list + second_list)