'''
Python元组的升级版本 --namedtuple(具名元组)
因为元组的局限性：不能为元组内部的数据进行命名
collections.namedtuple(typename, field_names, verbose=False, rename=False)
 typename：元组名称
 field_names: 元组中元素的名称
 rename: 如果元素名称中含有 python 的关键字，则必须设置为 rename=True
 verbose: 默认
'''
from collections import namedtuple
# 定义一个namedtuple类型User，并包含name，sex和age属性。
User = namedtuple('User', ['name', 'sex', 'age'])

# 直接创建一个User对象
user = User(name='Bob', sex='male', age=12)

# 获取所有字段名
print( user._fields )

# 也可以通过一个list来创建一个User对象，这里注意需要使用"_make"方法
user = User._make(['Jack', 'male', 12])

print( user )
# User(name='user1', sex='male', age=12)

# 获取用户的属性
print( user.name )
print( user.sex )
print( user.age )

# 修改对象属性，注意要使用"_replace"方法
user = user._replace(age=22)
print( user )
# User(name='user1', sex='male', age=21)

# 将User对象转换成字典，注意要使用"_asdict"
print( user._asdict() )
# OrderedDict([('name', 'Runoob'), ('sex', 'male'), ('age', 22)])