# 목적: 선그래프

from numpy.random import randn
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# cumsum() 값을 누적
plot_data1 = randn(50).cumsum()
plot_data2 = randn(50).cumsum()
plot_data3 = randn(50).cumsum()
plot_data4 = randn(50).cumsum()

fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.plot(plot_data1, marker=r'o', color = u'blue', linestyle='-', label='Blue Solid')
axl.plot(plot_data1, marker=r'+', color = u'red', linestyle='--', label='Red Dashed')
axl.plot(plot_data1, marker=r'*', color = u'green', linestyle='-.', label='Green Dash Dot')
axl.plot(plot_data1, marker=r's', color = u'orange', linestyle=':', label='Orange Dotted')
axl.xaxis.set_ticks_position('bottom')
axl.yaxis.set_ticks_position('left')

axl.set_title('Line Plots: Markers, Colors, and Linestyles')
plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.legend() # 범례를 화면에 나타내기 위해
# loc='best' : 그래프 상에서 범례를 최상의 위치에 배치
# plt.legend(loc='best')

plt.savefig('line_plot.png', dpi=400, bbox_inches='tight')
plt.show()
