class Greeter:
    def __init__(self,name,email,pwd):
        self.name=name
        self._email=email
        self.__pwd=pwd
        self.__P1='test private'
    def greet(self,prefix):
        print('%s %s'%(prefix,self.name))
        print('pwd=%s'%self.__pwd)
    def getP1(self):
        return self.__P1

g=Greeter('u1','e1','123')
g.greet('Hello')
print('name=%s'%g.name)
print('email=%s'%g._email)
print('P1=%s'%g.getP1())
#print('pwd=%s',%g.__pwd)





