import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
x = np.arange(start=1, stop=15, step=1)
y_linear = x + 5 * np.random.randn(14)
y_quadratic = x**2 + 10 * np.random.randn(14)

fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(x, y_linear, 'bo', x, y_quadratic, 'go', x, fn_linear(x), 'b-', x, fn_quadratic(x), 'g-', linewidth=2.)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.set_title('Scatter Plots with Best Fit Lines')
plt.xlabel('x')
plt.ylabel('f(x)')

predict_x = 16
predict_y = fn_linear(predict_x)
print(predict_y)
plt.scatter(predict_x,predict_y)

plt.xlim((min(x)-1, predict_x+1))
# predict_x로 변경, predict_x가 더 길이가 넓으므로
plt.ylim((min(y_quadratic)-10, max(y_quadratic)+10))
# y 최대값은 그대로 유지 기존 값이 더 크기 때문에

plt.savefig('scatter_plot.png', dpi=400, bbox_inches='tight')

plt.show()