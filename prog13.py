ide = {}
for i in range(3):
	key = input("Enter USN:")
	val = input("Enter name:")

	if key not in ide.keys():
		ide[key] = val

print (ide)