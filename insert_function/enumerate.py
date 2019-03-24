'''
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
enumerate(sequence, [start=0])
'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))        #下标从0开始，索引序列
print(list(enumerate(seasons, start=1)))   # 下标从 1 开始
seq = ['one', 'two', 'three','four','five','six','seven','eight']
for i, element in enumerate(seq,1):
   print(i,'->', element)
