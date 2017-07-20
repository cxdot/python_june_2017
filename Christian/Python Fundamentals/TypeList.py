mUni = ['Hello', 'Slut']
newStr = ""
sum = 0
numbers = False;


for i in range(0, len(mUni)):
	if type(mUni[i]) == int or type(mUni[i]) == float:
		sum += mUni[i]
		numbers = True;
	elif type(mUni[i]) == str:
		newStr += mUni[i] + " "
		
if (numbers == True and len(newStr) != 0):
	print "The list is mixed!"
	print "The sum is " + sum 
	print "The list contains these words: ", newStr
elif (numbers == True and len(newStr) == 0):
	print "The list contains numbers"
	print "The total is " + str(sum)
elif (sum == 0 and len(newStr) != 0):
	print "The list contains strings!"
	print "The list contains these words: ", newStr