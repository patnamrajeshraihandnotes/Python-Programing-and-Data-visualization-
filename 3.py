# Bar Chart
from matplotlib import pyplot as plt
import numpy as np

fruit={'apple':30,'mango':45,'graps':10}
names=list(fruit.keys())
quantity=list(fruit.values())

plt.bar(names,quantity,color='orange')
plt.title('Distribution of fruits')
plt.xlabel('fruit')
plt.ylabel ('quantity')
plt.show()
