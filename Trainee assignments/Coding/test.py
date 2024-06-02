import matplotlib.pyplot as plt
x=[4,5,6,7]
y1=[6,9,5,2]
y2=[2,4,5,6]

plt.plot(x,y1,marker='o',linestyle='--',label='one')
plt.plot(x,y2,marker='o',linestyle='--',label='two')
plt.legend()
plt.title('test')
plt.xlabel('x_values')
plt.ylabel("y_lable")
plt.show()