# 목적 : 막대 그래프
import matplotlib.pyplot as plt
plt.style.use('ggplot')

customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers)) # range(0,5) => [0,1,2,3,4]
sales_amounts = [127, 90, 201, 111, 232]

fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.bar(customers_index, sales_amounts, align='center', color = 'darkblue') # x축, y축 이름과 위치 정하기
# x축 눈금 위치를 아래쪽
axl.xaxis.set_ticks_position('bottom')
# y축 눈금 위치를 왼쪽
axl.yaxis.set_ticks_position('left')

# xticks(ticks, [labels], **kwargs)
# ticks : array_like
# A list of positions at which ticks should be placed. You can pass an empty list to disable xticks.

# labels : array_like, optional
# A list of explicit labels to place at the given locs.

# **kwargs
# Text properties can be used to control the appearance of the labels.

# plt.xticks(customers_index, customers)
# plt.xticks(customers_index, customers, color='red')
plt.xticks(customers_index, customers, color='red', fontsize='large') # 플롯이나 차트에서 축상의 위치 표시 지점을 tick이라고 하고,
                                                                      # 이 틱에 써진 숫자 혹은 글자를 틱 라벨

plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')

# dpi : The resolution in dots per inch
# bbox_inches : 'tight'일 경우 마진이 거의 없이 tight하게 그림
# plt.savefig('bar_plot.png', dpi=400)
plt.savefig('bar_plot_tight.png', dpi=400, bbox_inches='tight')
plt.show()
