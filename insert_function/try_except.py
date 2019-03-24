try:
    file=open('eeee.txt','r+')
except Exception as e:#捕捉异常对象e
    print(e)
    print('there is no file as eeee')
    response=input('Do you want to create a new file')
    if response =='y':
        file=open('eeee.txt','w')
        file.write("EEEE")
    else:
        pass