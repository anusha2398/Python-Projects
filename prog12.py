fruits = {'apple':'sweet', 'mango':'sweet'}
key_1 = input("enter the key")
value_1 = input("enter the value")
if  key_1 not in fruits.keys():
	fruits[key_1]=value_1
print(fruits)
