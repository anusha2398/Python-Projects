#largest 
def lrgest(list):
	max=list[0]
	for i in list:
		if i>max:
			max=i
	return max
print(largest([4,5,6,7,9]))



#alternate
a=[2,3,4,5]
print(max(a))