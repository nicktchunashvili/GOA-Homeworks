from turtle import *

#home 0

shape("turtle")
speed(100)
width(6)

color("brown")

#draw the cube
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
end_fill()
#end of the cube

#draw the door
color("red")
begin_fill()
left(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()
#door handle
color("black")
penup()
goto(95,40)
pendown()
left(90)
forward(5)
#end of the dorr

#draw the roof
color("green")
begin_fill()
penup()
goto(200,200)
pendown()
left(120)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#draw the windowns
#window 1
color("blue")
begin_fill()
penup()
goto(20,110)
pendown()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
#end of the 1 window

#draw window 2
color("blue")
begin_fill()
penup()
goto(130,110)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
#end of windows

#draw black line around the house
color("black")
penup()
goto(0,0)
pendown()
right(180)
forward(200)
left(90)
forward(200)
left(30)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
left(180)
forward(200)
left(90)
forward(200)
left(90)
forward(65)
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)

#on windows
color("black")
penup()
goto(20,110)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

color("black")
penup()
goto(130,110)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
#end of the house 0

#draw house 1

#draw the cube
color("brown")
begin_fill()
penup()
goto(400,0)
pendown()
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
#end of the cube

#draw the door
left(90)
forward(70)
color("green")
begin_fill()
left(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()

#draw the door handle
color("black")
penup()
goto(500,40)
pendown()
left(90)
forward(5)
#end of the door

#draw the roof 
color("yellow")
begin_fill()
penup()
goto(600,200)
pendown()
left(120)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#draw the windows

#draw the window 1
color("blue")
begin_fill()
penup()
goto(420,110)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#draw the window 2
color("blue")
begin_fill()
penup()
goto(530,160)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#end of the  windows

#draw black line around the house
color("black")
penup()
goto(400,0)
pendown()
right(180)
forward(200)
left(90)
forward(200)
left(30)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
left(180)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
left(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)

#draw line on the windows
#window1
color("black")
penup()
goto(420,110)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
#window2
color("black")
penup()
goto(530,110)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
#end of the house 1

#draw the house 2

#draw the cube
color("brown")
begin_fill()
penup()
goto(-400,0)
pendown()
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
#end of the cube

#draw the door
left(90)
forward(70)
color("orange")
begin_fill()
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
right(90)
forward(50)
end_fill()

#draw the door handle
color("black")
penup()
goto(-290,40)
pendown()
forward(10)
#end of the door

#draw the roof
color("red")
begin_fill()
penup()
goto(-200,200)
pendown()
right(60)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#draw the windows
color("blue")
begin_fill()
penup()
goto(-380,110)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#draw the window 2
color("blue")
begin_fill()
penup()
goto(-270,110)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#end of the windows

#draw black line around the house
color("black")
penup()
goto(-400,0)
pendown()
left(90)
forward(200)
left(90)
forward(200)
left(30)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
left(180)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)

#draw black line around the windows
color("black")
penup()
goto(-380,110)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

#window2
color("black")
penup()
goto(-270,110)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
#end of the house 2

#draw grass
color("green")
begin_fill()
penup()
goto(-800,-1)
pendown()
left(90)
forward(1600)
right(90)
forward(500)
right(90)
forward(1600)
right(90)
forward(500)
end_fill()
#end of the grass

#draw the lake
color("blue")
begin_fill()
penup()
goto(-510,-200)
pendown()
circle(100)
end_fill()

#draw road
color("#5C4033")
begin_fill()
right(90)
forward(1000)
right(90)
forward(50)
right(90)
forward(1000)
right(90)
forward(50)
penup()
goto(-330,0)
pendown()
right(180)
forward(200)
left(90)
forward(50)
left(90)
forward(200)
left(90)
forward(50)
right(180)
end_fill()
#end of the road

#draw the sun
color("yellow")
begin_fill()
penup()
goto(-700,200)
pendown()
circle(200)
end_fill()

exitonclick()




 #my name and lastname
# name = "nika"
# lastname = "tchunashvili"

# #my age
# age = 15
# year = 10
# #my age after 10 yeas
# age_after_ten_years = age + year

# #display 
# print(now, name, lastname, age)

 #display everything after 10 years
# print(name, lastname, age_after_ten_years)




