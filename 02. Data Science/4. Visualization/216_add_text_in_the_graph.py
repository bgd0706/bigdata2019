# 목적 : 여러 개의 그래프 그리기
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

plt.plot([1,2,3,4], [1,2,3,4], 'y')
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('matplotlib 활용')
plt.text(3.5,3.0, '평균:2.5') # x축 값이 3.5에 y축 값이 2.5에 '평균 2.5"라고 적혀져 있다.
plt.grid(True) # 턱 위치를 잘 보여주기 위해 그림 중간에 삽입되는 선이 grid!

plt.show()