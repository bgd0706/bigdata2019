#coding: cp949

while True :
    num = int(input("Ȧ���� �Է��ϼ���(0 <- ����): ")) # �غ��� ����

    if (num == 0) : break # 0�� �� ����
     
    row = int(num / 2) + 1 # ���� -> ���� ����
    col = num # �غ��� ���� -> ���� ����
    start = row-1 # ���� ���� ���� ��ġ
    finish = row-1 # ���� ���� �� ��ġ

    print(' ', end='') 
    print('-'*(col), end='') # �� �׵θ� 
    print(" ")

    if (start >=0 and finish <=col) : # ������ �غ����� 
        for j in range(0, row) : # 0���� ���� �������� 
            print ('|', end='') # ���� �׵θ�

            for i in range(0, col) : # 0���� ���� ��������
                if start <= i <= finish : # i�� ���� ���� ���۰� �� ��ġ ���� �ִ� ����
                    print ('*', end='') # ���� �׸���.
                else : # ���̿� ���� ����
                    print ('', end=' ') # ������ �ִ´�.
            print ('|', end='') # ������ �׵θ�
            start -= 1 # ���� start�� ���� �������� -1
            finish += 1 # ���� finish�� ���� �������� +1

            print(" ") # ���� ���� �࿡ �׸� �غ� 


    if (start <= row-1 and finish >= row-1) : # �غ����� �Ʒ�����
        start += 2 # +1�� �ƴ� +2�� �� ������ �غ��� �ߺ����� ������ �����̴�.
        finish -= 2
        for j in range(0, row-1) :
            print('|', end='')

            for i in range(0, col) :
                if start <= i <= finish :
                    print ('*', end='')
                else :
                    print ('', end=' ')
            print ('|', end='')            
            start += 1
            finish -= 1

            print(" ")
   
    print(' ', end='')
    print('-'*(col), end='') # �Ʒ��� �׵θ�
    print(" ")
