list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

def list(list_one, list_two):
	if list_one == list_two:
		print "The lists are the same"
	elif list_one != list_two:
		print "The list are different"
list(list_one, list_two)