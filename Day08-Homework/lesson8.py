#declare height and weight variables
required_height = 170
required_weight = 50


#declare user height and weight
user_height = int(input("your height :"))
user_weight = int(input("your weight :"))

#print right answer
#and
print(required_height == user_height and required_weight == user_weight)
print(required_height <= user_height and required_weight >= user_weight)

#or
print(required_weight == user_weight or required_height == user_height)
print(required_height <= user_height or required_weight >= user_weight)


#declare push ups and sit ups variables
required_push_ups = 100
required_sit_ups = 50

#declare how many push ups user do
push_ups = int(input("how many push ups did you do :"))
sit_ups = int(input("how many sit ups did you do :"))

#print 
#or 
print(required_push_ups == push_ups or required_sit_ups == sit_ups)



