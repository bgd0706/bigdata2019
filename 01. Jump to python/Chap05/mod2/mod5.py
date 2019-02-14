def sum5(a,b) :
    return a+b

def safe_sum5(a,b) :
    if type(a) != type(b) :
        print("두 인자의 형이 다릅니다.")
        return
    else :
        return sum5(a,b)
    return result

if __name__ == "__main__" :
    print(sum5(1,2))
    print(safe_sum5(1,2))
    print(safe_sum5(1,"2"))