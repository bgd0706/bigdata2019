# coding: cp949

age = int(input("���̸� �Է��ϼ���: "))
price = 0
grade = ""

if age < 0 :
    print ("�ٽ� �Է��ϼ���.")
    exit()

if 0 < age <= 3:
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

