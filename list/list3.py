#a = [1, 4, 9, 16, 25]
#a += [36, 49, 64, 81, 100]
import numpy as np
a=[x**2 for x in range(1,11)]
print(a)
a.reverse()
print("reversed results:",a)
a.sort()
print("sorted result:",a)
a.insert(2,['wanglu','love'])
print(a)
a.remove(25)
print(a)
a.pop(0)#stack bottom
print(a)
a.pop()#stack top
print(a)