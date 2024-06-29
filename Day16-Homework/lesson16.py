#დავალება1:
"""შექმენით სია სადაც შეინახავთ თქვენთვის საყვარელ ფილმებს და დაბეჭდეთ მთლიანი სია/ კონკრეტული ფილმი"""
my_favorite_movies = [
    "Bronx Tale",
    "Harry Potter",
    "The Godfather",
]

#კონკრეტული ფილმი
print(my_favorite_movies[0])

#დავალება2:
"""შექმენით 2 სია და გააერთიანეთ ისინი"""

list1 = [
    "Bronx Tale",
]

list2 = [
    "Harry Potter",
    "The Godfather",
]

comb = list1 + list2
print(comb)

#დავალება3:
"""შექმენით სტრინგი მაგ. თქვენი სახელი, და გამოიტანეთ სახელის პირველი და ბოლო სიმბოლო"""

name = "nika"

first = name[0]

last = name[-1]
print("name's first letter is",first,"name 's last letter is",last)

#დავალება4:
"""შექმენით სია და სტრინგი ხოლო შემდეგ დაბეჭდეთ len ფუნქციის გამოყენებით მათი ზომა"""

car_list = [
    "bmw",
    "opel",
    "mercedes",   
]
print(len(car_list))

string = "GOAAAA"
print(len(string))


#დავალება5:
"""შეცვალეთ სიიდან რომელიმე მნიშვნელობა (ჯერ გაიარეთ სოლოლეარნი)"""
 
games = [
    "GTA 5",
    "cs2",
]
games[1] = "Call of duty"
print(games)


#დავალება6:
"""შექმენით რიცხვების სია სადაც 10 რიცხვს შეიტანთ, გამოიტანეთ პირელ ინდექსა და ბოლო ინდექსზე მყოფი ელემენტების ჯამი"""

number = [1,2,3,4,5,6,7,8,9,10]

print(number[0] + number[-1])