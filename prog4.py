a = "Winter Is Coming!"
str_2 = ''
for letter in a:
	if letter.isupper():
		str_2 = str_2 + letter.lower()
	elif letter.islower():
		str_2 = str_2 + letter.upper()
	else:
		print(letter)
print (str_2)