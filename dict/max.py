'''
字典的键可以使用布尔类型的，True 默认代表 1，False 默认代表 0，如果包含 0 或 1 就无法使用布尔类型
'''
test1 = {0:"1", 1:"2", True:"3", False:"4"}
print(test1)
test2 = {"a":"1", "b" :"2", True:"3", False:"4"}
print(test2)
test = {'key1':'value1','key2':'value2'}
#test['key3'] #报错：KeyError:'key3'
print(test.get('key3')) #无输出
print(test.get('key3','default')) #输出'default'