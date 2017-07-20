# What would our output be for this example? Predict the following:
# 1. r"v"
# 2. r"^[aeiou]"
# 3. r"(\w)\1"
# Write regular expressions to find words that fit the following criteria, and use the above code to test your regex:
# 1. Contains "ss". Should match: ['issue', 'mattress', 'obsessive']
	#answer:  r"(s)\1"
# 2. Contains a "b", any character, then another "b". Should match: ['baby']
	#answer:  r"b.b"
# 3. Contains a "b", one or more characters, then another "b". Should match: ['baby', 'baseball']
	#answer: r"b.+b"
# 4. Contains all five vowels in order, with any number of characters between them. Should match: ['facetious']
	#answer: r"a.*e.*i.*o.*u"
# 5. Words ending in two vowels. Should match: ['issue', 'paranoia']
	#answer:  r"[aeiou]{2}$"
# 6. Words that only contain the letters in "regular expressions". Should match: ['issue', 'paranoia', 'union']
	#answer:  r"^[regular expressions]+$"
# 7. Words that don't contain any of the letters in "regex". Try looking up the two meanings of "^" in regular expressions! Should match: ['baby', 'union']
	#answer:  r"^[^regex]+$"


# Look at the output below, and try to find a regex that will match those words and only those words:
# 1. ['baby', 'baseball', 'rabble']
# 2. ['baby', 'rabble'] Hint: These should remind you of questions 2 and 3 above. What's the same? What's different?
# 3. ['facetious', 'union']
# 4. ['issue', 'obsessive', 'rabble']
# 5. ['mattress', 'volleyball']
	#answer: r"(\w)\1.*(\w)\2"

import re
def get_matching_words(regex):
    results = []
    words = [
        "baby",
        "baseball",
        "denver",
        "facetious",
        "issue",
        "mattress",
        "obsessive",
        "paranoia",
        "rabble",
        "union",
        "volleyball",
    ]
    for word in words:
        if re.search(regex, word):
            results.append(word)
    return results
my_expression =  r"^[^regex]+$"
print get_matching_words(my_expression)

