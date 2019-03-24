'''
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)
open(file, mode='r')
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
'''
help(print)#查看 print 内置函数的参数列表和规范的文档
print(print.__doc__)#获取文档字符串
print("www","baidu","com", sep='.', file=open("hello.txt", "w"))

f = open("hello.txt", 'w', encoding='utf8')
f.write("hello python")

f = open("hello.txt", 'a', encoding='utf8')
f.write("!!!")
f = open("hello.txt",'r+')
print ("读取的字符串是 : ",f.read())
f.close()#关闭文件
