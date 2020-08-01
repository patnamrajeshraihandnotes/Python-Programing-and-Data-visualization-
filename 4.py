# scatter plot
from matplotlib import pyplot as plt

x=[10,20,30,40,50,60,70,80,90]
a=[1,2,3,4,5,6,3,5,9]
b=[5,6,7,8,9,1,2,3,4]

plt.scatter(x,a,s=200)
plt.scatter(x,b,s=500,marker='1')
plt.legend(['a','b'])
plt.title('X vs a&b')
plt.xlabel('x')
plt.ylabel('a&b')
plt.show()

