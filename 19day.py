#PYTHON VISUALIZATION

# Line Plot
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [3,5,10,6,7]
plt.plot(x,y, color = 'r')
plt.title('Line Chart')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()


# BarChart
import matplotlib.pyplot as plt
marks = [50,60,70,80,90]
subject = ['Computer', 'Physics', 'Biology', 'Chemistry', 'Math']
plt.bar(subject, marks, color="Brown")
plt.show()


# PIE CHART
import matplotlib.pyplot as plt
sizes = [20, 30, 25, 25]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels , autopct = '%1.1f%%')
plt.title('Pie Chart')
plt.show()


# HEAT MAP
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data = np.random.rand(5,5)
df = pd.DataFrame(data, columns = ('A','B','C','D','E'))
sns.heatmap(data , annot=True, cmap='coolwarm')
# print(data)
# print(df)
plt.show()

# BOX PLOT
import matplotlib.pyplot as plt
import seaborn as sns
sns.boxplot(x =['A','B','C'],y = [5,7,9])
plt.title('BoxPlot')
plt.show()