"""შემოატანინეთ მომხმარებელს თავისი ასაკი input  ფუნქციის გამოყენებით შემდეგ შეამოწმეთ ასაკი არის თუ არა  მეტი  ან უდრის0 და ნაკლები 18 ზე დაუბეჭდეთ სხვა შემთხვევაში მეტია ან უდრის18 ზე და ნაკლებია 50 ზე დავუბეჭდოთ რომ არის ზრდასრული სხვა შემთხვევაში ის არის მოხუცი"""

age = int(input("enter your age"))

if age >=0:
    print("you are kid")
elif age < 18:
    print("you are kid")
if age >= 18:
    print("you are adult")
elif age <= 50:
    print("you are adult")
else: 
    print("you are old")


"""2) მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ შემოტანილი რიცხვი, თუ რიცხვი მეტია ნულზე მაშინ დავუბეჭდოთ რომ რიცხვი არის დადებით, სხვა შემთხვევაში თუ რიცხვი ნაკლებია ნნულზე დავუბეჭდოთ რომ რიცხვი არის უარყოფითი, ხოლო სხვა შემთხვევაში დაბეჭდეთ რომ რიცხვი არის 0"""
 
num = int(input("please enter number"))

if num > 0:
    print("positive")
elif num <0:
    print("negative")
else:
    print("number is 0")