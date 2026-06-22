import numpy as np
import matplotlib.pyplot as plt


def scatter_plot():

    x = np.array([1,2,3,4,5,6,7,8,9,10])
    y = np.array([1,2,3,15,5,45,46,67,82,90])
    color = ([15,30,45,60,75, 80,60,50,100, 100])
    sizes = ([100,20,30,40,50,60,70,800,900,1000])
    plt.scatter(x, y, c=color, cmap = 'Accent', s=sizes, marker='s', label = 'niga', alpha = 0.5)
    plt.legend(loc='upper left')

def car():
    import matplotlib.pyplot as plt
    import numpy as np

    #day one, the age and speed of 13 cars:
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    plt.scatter(x, y)

    #day two, the age and speed of 15 cars:
    x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
    y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
    plt.scatter(x, y)

    #day three, the age and speed of 15 cars:
    x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    y = np.array([200, 210, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70])
    plt.scatter(x, y)


scatter_plot()


plt.show()