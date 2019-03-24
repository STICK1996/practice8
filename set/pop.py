'''
s.pop()
在脚本模式下，随机删除集合中的一个元素
在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素）
'''
thisset = set(("Google", "Baidu", "Taobao", "Facebook"))
x = thisset.pop()
print(x)
print(thisset)
print(len(thisset))
print("Facebook" in thisset)