words = "It's thanksgiving day. It's my birthday,too!"
#finding first instance word "day"
words.find("day")
#replacing "days" with month
words.replace("days", "month")


x = [2,54,-2,7,12,98]
#printing min and max values of listed stated above
print "min value element : ", min(x)
print "max value element : ", max(x)


y = ["hello",2,54,-2,7,12,98,"world"]
#printing first index of y
print y[+0]
#printings last index of y
print y[-1]
#create new list with the first and last values of the string above 
newLIst = y[0], y[7]
print newList

p = [19,2,54,-2,7,12,98,32,10,-3,6]
#sorts numbers in order from least to greatest
p.sort()
#setting a new variable for p1 with the first half of the list above
p1 = p[0:len(p)/2]
print p1
[-3, -2, 2, 6, 7]
#setting a 2nd list with the other half of list above
p2 = p[len(p)/2:len(p)]
print p2
[10, 12, 19, 32, 54, 98]
#inserting p2 into the index of 0 of p1
p2.insert(0,p1)
print p2
[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]


