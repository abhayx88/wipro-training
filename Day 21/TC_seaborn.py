import seaborn as sns
import matplotlib.pyplot as plt
marks = [50, 60, 80, 70, 77, 86]

sns.set_style("whitegrid")
sns.histplot(marks, bins=5)
plt.title("Histogram of Marks")
plt.show()
