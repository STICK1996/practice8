'''算法题如下：给个有序数组，然后求元素平方后不重复的元素个数，
例如[-10, -10, -5, 0, 1, 5, 8, 10]
'''
# 这是我的实现，没有用到集合，如果用到集合会更好
data = [-10, -10, -5, 0, 1, 5, 8, 10]
new_list = []
for x in data:
	temp = x*x
	if temp not in new_list:
		new_list.append(temp)
print(len(new_list))

#set
print(len(set([x**2 for x in data])))