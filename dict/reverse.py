dic = {
    'a': 123.5,
    'B1': 78.0,
    '3C': 463.8,
}
for i in dic.values():
    print(i)
for c in dic.keys():
    print(c)
for k, v in dic.items():#items()
   print(k, v)
print("reversed keys and values:")
reverse = {v: k for k, v in dic.items()}
print(dic)
print(reverse)







#max_dic=max(zip(dic.values(),dic.keys()))#zip() Two or more sequences
#print(max_dic)