import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

simple_data1 = [1,2,3,4,5,6,7,8,9,10]
# simple_data2 = [4,5,6,7,7,8,8,9,10,12,20,40,80,160]
# simple_data2 = [3,12,15,16,16,17,19,34]
box_plot_data = [simple_data1]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

box_labels = ['s1']
ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Box Plots: Resampling of Two Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Value')

plt.show()