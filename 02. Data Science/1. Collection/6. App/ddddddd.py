import csv
from selenium import webdriver

# with open('ref_sub.csv', 'r', encoding='utf-8') as f_ref:
#     while True :
#         line = f_ref.readline().replace("\n","")
#         if not line : break
#         print("%s (이/가) %s 있습니다." %(line.split(' ')[0], line.split(' ')[1]))
        # search_url = "http://home.ebs.co.kr/cook/board/4/500514/list?bbsId=500514&boardType=2&iframeOn=false&searchCondition=pstCntnSrch&" \
        #              "searchKeyword=%s&searchKeywordCondition=1" % line.split(' ')[0]
        # driver = webdriver.Chrome('C:\chromedriver')
        # driver.implicitly_wait(3)
        # driver.get(search_url)

# line = []
# with open('ref_sub.csv', 'r', encoding='utf-8', newline='') as f_ref:
#     while True:
#         lines = f_ref.readline().replace("\n", "")
#         if not lines: break
#         print(lines.split(',')[0])
#         line.append(lines)
#     while True :
#         ingred_to_use = input("어떤 재료를 쓰겠습니까? (안하면 n) ")
#         if ingred_to_use == 'n': break
#         for i in range(len(line)) :
#             subject_name = line[i].split(',')[0]
#             subject_num = line[i].split(',')[1]
#             print(subject_num[:len(subject_num)-1]) # 3개
#             print(subject_num[:len(subject_num)-2]) # 3
#             print(subject_num[len(subject_num)-2]) # 개
            # if ingred_to_use == subject_name[:len(subject_name)] :
            #     num_to_now = int(subject_num[:len(subject_num)-2]) # 현재 냉장고에 있는 재료 수
            #     num_to_want = int(input("몇 %s 쓰겠습니까? " % subject_num[len(subject_num)-2])) # 쓰고 싶은 재료 수
            #     if num_to_want > num_to_now :
            #         print("현재 냉장고에 있는 수 보다 많습니다. 다시 선택해주세요.")
            #         break
            #     num_to_left = num_to_now - num_to_want # 남는 재료 수
            #     with open('ref_sub.csv', 'r', encoding='utf-8', newline='') as f_ref_2:
            #         while True:
            #             lines = f_ref_2.readline().replace("\n", "")
            #             if not lines: break
            #             if lines.split(',')[0] == subject_name :
            #                 lines.replace(lines.split(',')[1][:len(lines.split(',')[1])-2], str(num_to_left))
            #                 print(lines)
            #                 break

