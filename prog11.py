a=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
search=int(input("enter the number:"))
b=[]
for i, val in enumerate(a):
	if val is search:
		b.append(i)

print(b)
