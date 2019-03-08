def sum2(a,b) :
    return a+b

def safe_sum2(a,b) :
    if type(a) != type(b) :
        print("두 인자의 형이 다릅니다.")
        return
    else :
        return sum2(a,b)
    return result

if __name__ == "__main__" :
    print(sum2(1,2))
    print(safe_sum2(1,2))
    print(safe_sum2(1,"1. CSV"))