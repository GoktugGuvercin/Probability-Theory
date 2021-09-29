

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dof = 2  # degree of freedom
mean, var = 30, 6
low, high = 1, 40

dist1 = np.random.uniform(low, high, 50000)
dist2 = np.random.chisquare(dof, 50000)
dist3 = np.random.normal(mean, var, 50000)

plt1 = sns.displot(data=dist1, kind="kde")
plt2 = sns.displot(data=dist2, kind="kde")
plt3 = sns.displot(data=dist3, kind="kde")

plt1.set_xlabels("Value Range (Problem Domain)")
plt1.set(title="Uniform Distribution")

plt2.set_xlabels("Value Range (Problem Domain)")
plt2.set(title="Chi-Square Distribution")

plt3.set_xlabels("Value Range (Problem Domain)")
plt3.set(title="Gaussian Distribution")

plt.show()
