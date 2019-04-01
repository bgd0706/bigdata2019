import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# Linear regression model
tips = sns.load_dataset("tips")
print(tips.head(100))
sns.lmplot(x="total_bill", y="tip", data=tips)

plt.show()