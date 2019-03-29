#product
list=[]
for i in  range(1,5):
	list.append(i)
	print(list)
result=1
for item in list:
	result=result+item
print("product of all elements:",result)