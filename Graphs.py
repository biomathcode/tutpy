import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
x =[5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.bar(x,y,color='g',label='line one',linewidth = 3)
plt.bar(x2,y2,color ='r',label='line two', linewidth= 3)
plt.title('Epic info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True, color='k')
plt.show()
