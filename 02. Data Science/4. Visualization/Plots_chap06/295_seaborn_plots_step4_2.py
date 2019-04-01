import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# Linear regression model
tips = sns.load_dataset("tips")
print(tips.head(100))
sns.factorplot(x="time",y="total_bill", hue="sex",
               col="day",data=tips,kind="box",size=4,aspect=.5)
plt.show()