import numpy as np
np.set_printoptions(linewidth=1000)

import matplotlib.pyplot as plt
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

from scipy import interpolate
# 寻找X1、X2的公共定义域
def numpy_find_commen_definitional_domain_X_by_X1X2(
    X1 = np.array([1, 1.8, 3, 4, 5]), 
    X2 = np.array([2, 3.2, 4.5, 5.1, 6, 8, 11])
    ):

    X1.sort()
    X2.sort()

    a = np.max([X1[0], X2[0]])
    b = np.min([X1[-1], X2[-1]])

    X_full = np.append(X1, X2)
    X_full = np.array(list(set(X_full))) # 去重
    X_full.sort()
    X_commen = X_full[np.where(np.logical_and(X_full>=a, X_full<=b))]
    return X_commen # [2.  3.  3.2 4.  4.5 5. ]
# 两组离散数据点(#不允许线段有重合！)
X1 = [1, 1.8, 3, 6.5, 12]
Y1 = [5, 5, 9, 6.2, 5]

X2 = [1, 3.2, 4.5, 5.1, 6, 8, 11] # 2
Y2 = [8, 5, 5, 8, 3, 5, 4]
# 显示离散点(#不允许线段有重合！)
plt.figure(figsize=(12, 6))
plt.title('两组离散数据')
plt.xlabel('X')
plt.ylabel('Y')

plt.plot(
    X1, 
    Y1, 
    linestyle= 'dashed',
    marker='*',
    label='X1,Y1离散数据')

plt.plot(
    X2, 
    Y2, 
    linestyle= 'dashed',
    marker='*',
    label='X2,Y2离散数据')

plt.legend()
plt.show()


# 寻找公共定义域（严格单调递增数据）
X_new = numpy_find_commen_definitional_domain_X_by_X1X2(X1=X1, X2=X2)
print(X_new)
[ 1.   1.8  3.   3.2  4.5  5.1  6.   6.5  8.  11. ]
Y1_new = np.interp(X_new, X1, Y1)
Y2_new = np.interp(X_new, X2, Y2)
Y_new = Y1_new - Y2_new # 作差

# 两离散数据的交点
inersections_X = numpy_scipy_find_roots_by_XY(X=X_new, Y=Y_new, plot=0)
inersections_Y = np.interp(inersections_X, X1, Y1)
print(inersections_X, inersections_Y) # 3个交点
[2.20645161 4.98275862 5.24299065] [6.35483871 7.4137931  7.20560748]
# 封装成函数便于调用
# 两组离散曲线求交点
def numpy_scipy_find_inersections_by_X1Y1X2Y2(X1, Y1, X2, Y2, print_=0, plot=0, xlabel='X', ylabel='Y'):

    # X1、X2必须为严格单调递增数据
    if np.all(np.diff(X1) > 0) == True:
        pass
    else:
        raise Exception('X1必须为严格单调递增数据!')

    if np.all(np.diff(X2) > 0) == True:
        pass
    else:
        raise Exception('X2必须为严格单调递增数据!')

    # 寻找公共定义域（严格单调递增数据）
    X_new = numpy_find_commen_definitional_domain_X_by_X1X2(X1=X1, X2=X2)
    #print(X_new)
    Y1_new = np.interp(X_new, X1, Y1)
    Y2_new = np.interp(X_new, X2, Y2)
    Y_new = Y1_new - Y2_new

    inersections_X = numpy_scipy_find_roots_by_XY(X=X_new, Y=Y_new, print_=print_, plot= plot)
    inersections_Y = np.interp(inersections_X, X1, Y1)



    if print_ == 1:
        print(inersections_X, inersections_Y)

    if plot == 1:

        # 显示曲线
        plt.figure(figsize=(12, 6))
        plt.title('两组离散数据的交点')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)


        plt.plot(
            X1, 
            Y1, 
            linestyle= '-',
            marker='*',
            label='X1,Y1离散数据')

        plt.plot(
            X2, 
            Y2, 
            linestyle= '-',
            marker='*',
            label='X2,Y2离散数据')

        plt.legend()
        plt.show()

    return inersections_X, inersections_Y
inersections_X, inersections_Y = numpy_scipy_find_inersections_by_X1Y1X2Y2(X1, Y1, X2, Y2, plot=1, print_=1)
[2.20645161 4.98275862 5.24299065]
