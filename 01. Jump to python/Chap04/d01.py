# def greet_users (usernames) :
#     for i in usernames :
#         print("Hello, " + i[0].upper() + i[1:]+'!')

# usernames = input("이름을 입력하세요 : ").split(" ")
# greet_users(usernames)

import sys

args = sys.argv[3:]
for i in args:
    print("Hello, "+i[0].upper()+i[1:])