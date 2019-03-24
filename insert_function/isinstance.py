'''
isinstance()
可以用 isinstance 函数判断某个对象是否属于某个类的实例
'''
print(isinstance(1, (int, str)))#True

print(isinstance("", (int, str)))#True

print(isinstance({}, dict))#True