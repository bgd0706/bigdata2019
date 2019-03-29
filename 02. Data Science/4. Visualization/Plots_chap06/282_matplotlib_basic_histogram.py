# 목적 : 히스토그램
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

mu1, mu2, sigma = 100, 130, 15
# randn(10000) => -1 ~ 1 사이의 정규분포를 갖는 값을 10000개 생성
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)

fig = plt.figure()
axl = fig.add_subplot(1,1,1)
# hist함수 인자
# bins: 수치가 클수록 세로축이 정교해짐
# normed : False일 경우 확률이 아니라 빈도로 표시
# alpha : 투명도 (겹치는 부분)
n, bins, patches = axl.hist(x1, bins=50, normed=False, color='darkgreen')
n, bins, patches = axl.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)
axl.xaxis.set_ticks_position('bottom')
axl.yaxis.set_ticks_position('left')

plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Histograms', fontsize=14, fontweight='bold')
axl.set_title('Two Frequency Distributions')

plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
plt.show()
