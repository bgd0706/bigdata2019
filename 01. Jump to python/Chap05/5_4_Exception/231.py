try :
    f = open('foo.txt','r')
except FileNotFoundError as e :
    print(str(e))
# else :
#     data = f.read()
#     f.close()
data = f.read() # else문으로 해도 되지만 그냥 안해도 상관은 없다.
f.close()
