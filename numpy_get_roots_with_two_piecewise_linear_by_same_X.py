import numpy as np
import matplotlib.pyplot as plt
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


#### 两组离散数据（同X）求交点 ####
def numpy_get_roots_with_two_piecewise_linear_by_same_X(
    Y1 = [6, 5, 3, 10, 5, 6, 8], 
    Y2 = [2, 5, 5, 4, 3, 5, 8], 
    X = None, 
    plot = 0
    ):
    # 注1：Y1与Y2长度相等，每条直线段最多只能有一个交点（不可能有两个）
    # 注1：X的值必须由小到大（X须为单调递增序列）
    if X == None:
        X = [i+1 for i in range(len(Y1))]
    else:
        pass
    
    roots = []
    for i in range(len(Y1)-1):
        Y_i_1 = [Y1[i], Y1[i+1]]
        Y_i_2 = [Y2[i], Y2[i+1]]
        X_i = [X[i], X[i+1]]

        poly_i_1 = np.poly1d(np.polyfit(X_i, Y_i_1, 1))
        poly_i_2 = np.poly1d(np.polyfit(X_i, Y_i_2, 1))
        poly_delta = poly_i_1 - poly_i_2
        
        # 非水平直线函数poly_delta必定有且只有一个解
        root_i = poly_delta.roots[0]
        y = poly_i_1(root_i)
        
        # 减少精度，找回因数据精度损失造成节点处丢失的根
        root_i = round(root_i, 6)
        y = round(y, 6)
        #print((root_i, y), X_i)
        if root_i >=  X_i[0] and root_i <= X_i[1]:
            #print((root_i, y), X_i)
            roots.append((root_i, y))

    if plot == 1:
        # 显示曲线
        plt.figure(figsize=(12, 6))
        plt.title('两组离散数据(相同序列X)求交点')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.plot(
            X, 
            Y1, 
            marker='*',
            label='X,Y1离散数据')

        plt.plot(
            X, 
            Y2, 
            marker='*',
            label='X,Y2离散数据')

        plt.legend()
        plt.show()

    roots = list(set(roots))
    roots.sort()
    return roots

if __name__ == '__main__':

    roots = numpy_get_roots_with_two_piecewise_linear_by_same_X(Y1=[6, 5, 3, 10, 5, 6, 8], Y2=[2, 5, 5, 4, 3, 5, 8], X=None, plot=1)
    print(roots)
    
    
