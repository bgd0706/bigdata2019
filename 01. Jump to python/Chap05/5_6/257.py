import time

# print(time.time())
# print(time.localtime(time.time()))
# print(time.asctime(time.localtime(time.time())))

# print(time.ctime())

print(time.strftime('%x',time.localtime(time.time())))
print(time.strftime('%c',time.localtime(time.time())))
