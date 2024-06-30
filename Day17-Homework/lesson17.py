
#დავალება1:
""" შექმენით ლისტი სადაც ჩამოწერილიქნება თამაშის სახელები და შემდგომ თამაშებს ვანაცვლებთ სოლოლერნით , w3 , codewars - ებით და ასეშემდეგ."""

game_list = [
    "GTA",
    "CS2",
    "Call of Duty",
]

game_lists0 = "sololearn" 
game_lists1 = "codewar"
game_lists2 = "w3"

all_game_lists = game_lists0,game_lists1,game_lists2

print(all_game_lists)


#დავალება2:
"""შექმენით 5 ინფუთი და ამ ინფუთებით შეადგინეთ სია, შემდეგ გამოიტანეთ ამ სიიდან ლუწი რიცხვები, ისე რომ ლოგიკამ ყველა შემთხვევაში იმუშაოს"""

input1 = int(input("please enter first number:"))
input2 = int(input("please enter second number:"))
input3 = int(input("please enter third number:"))
input4 = int(input("please enter fourth number:"))
input5 = int(input("please enter fifth number:"))

list = [input1,input2,input3,input4,input5]
even_numbers = [number for number in list if number % 2 == 0]

print(even_numbers)
