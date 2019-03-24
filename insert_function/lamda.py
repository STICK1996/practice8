"""
匿名函数：lambda
lambda [arg1 [,arg2,.....argn]]:expression
map()函数
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回

"""
# ###################### 普通函数 ######################
# 定义函数（普通方式）
def func(arg1,arg2):
    return arg1 * arg2
result = func(8,9)
print("func:",result)

# ###################### lambda ######################
# 定义函数（lambda表达式）
my_lambda = lambda arg1,arg2: arg1 *arg2

# 执行函数
result = my_lambda(9,8)
print("my_lambda:",result)
# ######################  map  ######################
result=map(func,[1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
for i in result:
    print(i,end=' ')
print('\n')
result=(map(lambda arg1,arg2: arg1 *arg2,[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
for i in result:
    print(i)