'''
print("a ^ b",a ^ b)

'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 这里演示的是去重功能
print(set(basket))
print('orange' in basket)  # 快速判断元素是否在集合内
print('crabgrass' in basket)
# 下面展示两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print('差集:',a.difference(b))
print('差集:',a-b,'\n')
print('交集：',a.intersection(b))
print('交集：',a & b,'\n')
print('并集：',a.union(b))
print('并集：',a | b,'\n')
