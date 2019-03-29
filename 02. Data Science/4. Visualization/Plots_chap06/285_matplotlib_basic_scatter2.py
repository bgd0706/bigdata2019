# 목적 : 산점도
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# 1~14까지 array 반환
x = np.arange(start=1, stop=15, step=1)

# 1차 방정식에 준하는 선형회귀 결과를 얻기 위한 공식
y_linear = x + 5*np.random.randn(14)
# 2차 방정식에 준하는 선형회귀 결과를 얻기 위한 공식
y_quadratic = x**2 + 1*np.random.randn(14)

# deg=1 : 1차 방정식 형태, deg=2 : 2차 방정식 형태
fn_linear = np.poly1d(np.polyfit(x,y_linear, deg=1))
fn_quandratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))

