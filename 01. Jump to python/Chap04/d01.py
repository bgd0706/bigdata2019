def greet_users (usernames) :
    for i in usernames :
        print("Hello, " + i[0].upper() + i[1:]+'!')

usernames = input("이름을 입력하세요 : ").split(" ")
greet_users(usernames)