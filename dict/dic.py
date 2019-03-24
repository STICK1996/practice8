'''
字典和列表、元组在构建上有所不同。列表是方括号 []，元组是圆括号 ()，字典是花括号 {}
'''
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
a=(tel.keys())
print(a)
b=sorted(tel.keys())
print(b)
print('guido' in tel)
print('jack' not in tel)
d={'apple':[9,7,3],'pear':{'k':3,9:'c'},'orange':2}
print(d['pear'])
print(d['pear']['k'])
print(d['apple'][-2])
