import numpy as np
import matplotlib.pyplot as plt


def graph():
    y_axis = [1,2,3,4,10]
    x_axis = [1,2,3,4,5]
    plt.plot(x_axis, y_axis,'o-.m', ms = 15,mec = 'r', label='Line 1',mfc = "#00FFFF", lw=4) 
    plt.grid(axis = 'x')
    plt.title('Graph Title', fontdict={'fontsize': 20, 'color': 'blue'})
    plt.legend()     

    # ms = marker size
    # mec = marker edge color
    #shortcut for marker/line/color = for eg - 'o-.m'
    mfc = 'g' # marker face color
    ls = '--' # line style
    c = 'b' # color


def graph2():

    x = np.array([1,2,3,4,5])
    y = np.array([1,2,3,15,5])
    x2 = np.array([1,2,3,4,5])
    y2 = np.array([5,4,3,2,1])
    plt.plot(x,y,x2,y2)
    plt.xlabel('x axis', fontdict={'fontsize': 20, 'color': 'red'})
    plt.ylabel('y axis', fontsize = 15)
    plt.title('graph', loc = 'left', fontsize = 30)
    plt.grid(True, color = 'b', linestyle = 'dashed')
    plt.legend()



plt.subplot(2,1, 1)
graph()
plt.subplot(2, 1, 2)    
graph2()
plt.suptitle('Subplots Example', fontsize=20, fontweight='bold')
plt.tight_layout()

plt.show()