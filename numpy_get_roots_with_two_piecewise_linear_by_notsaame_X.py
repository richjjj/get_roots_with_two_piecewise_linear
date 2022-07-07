import numpy as np
import matplotlib.pyplot as plt
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号



from numpy_get_roots_with_two_piecewise_linear_by_same_X import *


# 求交集范围
def X1X2ab(X1ab=(1, 6), X2ab=(5,9)):
    '''
    xa, xb = X1X2ab(X1ab=(X1[0], X1[-1]), X2ab=(X2[0], X2[-1]))
    '''
    X1a = X1ab[0]
    X1b = X1ab[1]
    if X2ab == None:
        X2a = X1a
        X2b = X1b
    else:
        X2a = X2ab[0]
        X2b = X2ab[1]
        if X2a == None:
            X2a = X1a
        if X2b == None:
            X2b = X1b


    # 先确定X2a的位置 , r_left
    if X2a <= X1a:
        r_left = X1a
    elif X1a < X2a and X2a <X1b:
        r_left = X2a
    elif X2a >= X1b:
        return None
    # 再确定X2b的位置, r_right
    if X2b <= X1a:
       return None
    elif X1a < X2b and X2b <X1b:
        r_right = X2b
    elif X2b >= X1b:
        r_right = X1b
    xab = (r_left, r_right)
    return xab





def numpy_get_roots_with_two_piecewise_linear_any(

    X1 = [1, 1.8, 3, 4, 5],
    Y1 = [5, 5, 9, 10, 5],

    X2 = [2, 3.2, 4.5, 5.1, 6, 8, 11],
    Y2 = [8, 5, 5, 8, 3, 5, 4],

    plot = 0

    ):

    # 构造新的X_new
    X_ = X1 + X2
    X_.sort()
    X_new = []
    # 共同定义域
    a, b = X1X2ab(X1ab=(X1[0], X1[-1]), X2ab=(X2[0], X2[-1]))
    for i in X_:
        if i >= a and i <= b:
            X_new.append(i)
    X_new = list(set(X_new)) # 去重
    X_new.sort()
    #print(X_new)

    # 构造新的Y1_new、Y2_new
    Y1_new = np.interp(X_new, X1, Y1)
    Y2_new = np.interp(X_new, X2, Y2)

    roots = numpy_get_roots_with_two_piecewise_linear_by_same_X(Y1=Y1_new, Y2=Y2_new, X=X_new, plot=plot)
    return roots




if __name__ == '__main__':

    X1 = [1, 1.8, 3, 4, 5]
    Y1 = [5, 5, 9, 10, 5]

    X2 = [2, 3.2, 4.5, 5.1, 6, 8, 11]
    Y2 = [8, 5, 5, 8, 3, 5, 4]


    roots = numpy_get_roots_with_two_piecewise_linear_any(X1=X1, Y1=Y1, X2=X2, Y2=Y2, plot=1)
    print(roots)


    plt.figure(figsize=(12, 6))
    plt.title('两组离散数据(不同序列X)求交点')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.plot(
        X1, 
        Y1, 
        marker='*',
        label='X1,X1离散数据')

    plt.plot(
        X2, 
        Y2, 
        marker='*',
        label='X2,X2离散数据')

    plt.legend()
    plt.show()
