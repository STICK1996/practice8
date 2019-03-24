'''
remove方法删除指定无素，如果要删除的元素的不在集合中，则报错；
discard方法删除指定元素，如果要删除物元素不在集合中，则不报错；
pop方法删除任意元素，并可将这个元素赋值给一个变量
'''
a=set('abcdefghijk')
print(a)
a.remove('a')
print(a)
#a.remove('w')
'''
Traceback (most recent call last):
  File "C:/Users/YOU-TO-BE/PycharmProjects/practice/set/delete.py", line 5, in <module>
    a.remove('w')
KeyError: 'w'

'''
a.discard('h')
print(a)
a.discard('w')
b=a.pop()
print(b,type(b))
print(a)
a.clear()
print(a)
