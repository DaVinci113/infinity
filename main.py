from turtle import *


ru = 41
ld = 76
lu = 125
speed(20)
penup()
forward(250)
right(90)
forward(185)
left(90)
pendown()
for i in range(1):
	for i in range(166):
		if i <= ru:
			circle(100)
			forward(20)
			left(5)
		if ru < i < ld:
			circle(100)
			forward(13)
		if i == ld:
			penup()
			left(90)
			forward(200)
			right(90)
			pendown()
		if ld < i < lu:
			circle(-100)
			forward(20)
			right(5)
		if i == lu:
			penup()
			right(90)
			forward(200)
			left(90)
			pendown()
		if i > lu:
			circle(100)
			forward(13)
	left(23)

exitonclick()
