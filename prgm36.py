import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris=pd.read_csv("iris.csv")
sns.displot(iris['Sepal.Length'],kde=True,rug=True)
plt.title("Distribution of Sepal length")
plt.show()
sns.histplot(iris['Petal.Width'],kde=True,bins=20)
plt.title("Histogram of Petal width")
plt.show()
sns.relplot(x="Sepal.Length",y="Sepal.Width",data=iris,hue="Species",style="Species")
plt.title("Sepal Length v/s Sepal Width")
plt.show()