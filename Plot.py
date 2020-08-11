# importing modules
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def x_y_( data_x, data_y ):
    x = np.array(data_x).reshape((-1, 1))
    y = np.array(data_y)
    model = LinearRegression().fit(x, y)

    r_sq = model.score(x, y)
    print('equation: y= ' + str(model.coef_[0]) + 'x + ' + str(model.intercept_))
    print('r squared: ' + str(r_sq))
    plt.scatter(x, y, color='black')
    plt.plot(x, (model.coef_[0] * x) + model.intercept_, color='blue', linewidth=3)
    plt.xlabel('rating differential')
    plt.ylabel('expected score differential')
    plt.show()
