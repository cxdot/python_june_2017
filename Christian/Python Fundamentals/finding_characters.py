word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []	
	
for i in range(0, len(word_list)):
	if char in word_list[i]:
		new_list.append(word_list[i])
print new_list 

