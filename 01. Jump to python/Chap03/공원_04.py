# coding: cp949

age = int(input("���̸� �Է��ϼ���: "))
price = 0
grade = "����"

if age < 0 :
    print ("�ٽ� �Է��ϼ���.")
    exit()
elif 0 < age <= 3:
    grade = "����"
elif 3 < age <= 13:
    price = 2000
    grade = "���"
elif 13 < age <= 18:
    price = 3000
    grade = "û�ҳ�"
elif 18 < age <= 65:
    price = 5000
    grade = "����"
else :
    grade = "����"
    
print("���ϴ� %s����̸�, ����� %d�� �Դϴ�." %(grade, price))

choice = int(input("��� ������ �����ϼ���. (1: ����, 1. CSV: ���� ���� �ſ�ī��) : "))

if choice == 1 : 
    if price == 0 :
        print("�����մϴ�. Ƽ���� �����մϴ�.")
        exit()

    input_price = int(input("����� �Է��ϼ���."))
    
    if input_price < price :
        print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %(price-input_price, input_price))
    elif input_price == price :
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    else :
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ �մϴ�." %(input_price-price))
elif choice == 2 :
    dis_price = price*0.9
    if age >= 60 and age <= 65 :
        dis_price = dis_price*0.95
    print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(dis_price))

else :
    exit()


