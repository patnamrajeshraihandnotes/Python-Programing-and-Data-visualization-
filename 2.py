from matplotlib import pyplot as plt
import numpy as np

x= np.arange(1,10,0.1)
y1=2*x+5
y2=3*x+10

plt.subplot(1,2,1)
plt.title('Line chart')
plt.plot(x,y1)

plt.subplot(1,2,2)
plt.plot(x,y2)


plt.xlabel('X-axis')
plt.ylabel('y-axis')


plt.show()
