#print odds
for odds in range(1, 1001, 2):
    print odds

#for multiples of 5
for multiples in range(5, 1000001, 5):
    print multiples

#print sums of the list
x = [1, 2, 5, 10, 255, 3]
sum = 0
for y in x:
    sum += y
print sum

#avg of list
a = [1, 2, 5, 10, 255, 3]
sum = 0
avg = 0
for y in a:
    sum += y
    avg = sum / len(a)
print avg
