# 목적 : 기본 그래프 그리기

import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.xlabel('X-axis label')
# plt.xlabel('한글 테스트') # 한글 폰트를 지정하지 않으면 한글은 깨져서 나온다.
plt.ylabel('Y-axis label')
plt.show()