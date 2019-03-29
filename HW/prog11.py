#sum of elements in a list using for loop
list=[]
num=int(input('enter length:'))
for i in range (num):
	numbers=int(input('enter the number:'))
	list.append(numbers)
print("sum of elements in a given list is:",sum(list))