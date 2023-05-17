import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
f = open("result.txt","r")

ALGO_NUM = 4
SERVICE_NUM = 1
MU_NUM = 1
STD_NUM = 1
DATA_NUM = 1000
SERVICE_RANGE = 4

ALGO_LABEL = ["HEFT","CPOP","PEFT","DHS"]

result_x = [[] for _ in range(SERVICE_RANGE)]
result_y = [[] for _ in range(SERVICE_RANGE)]
result_z = [[] for _ in range(SERVICE_RANGE)]

for i in range(ALGO_NUM):
    for j in range(SERVICE_NUM):
        for s in range(STD_NUM):
            lst = [[] for _ in range(SERVICE_RANGE)]
            ans = []
            for k in range(DATA_NUM):
                arr = np.array(f.readline().split(),dtype=np.float32)
                s = arr.std()
                m = arr.mean()
                n = int(f.readline())
                #print(arr)
                lst[n-3].append([m,s,float(f.readline())])
                #ans += float(f.readline())
            #print(lst)
            for r in range(SERVICE_RANGE):
                #lst[i].sort()
                lst[r] = np.array(lst[r])
                x = lst[r][:,0]
                y = lst[r][:,1]
                z = lst[r][:,2]
                result_x[r].append(x)
                result_y[r].append(y)
                result_z[r].append(z)
                ans.append(sum(z)/len(z))
            print(sum(ans)/len(ans))
        print(j,"---------")
    print(i,"***********************")

f.close()

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(111,projection='3d')
ax.scatter(result_x[0][0],result_y[0][0],result_z[0][0])

plt.xlabel('mean')
plt.ylabel('std')
plt.show()

"""
for i in range(SERVICE_RANGE):
    for j in range(ALGO_NUM):
        fit_l = np.polyfit(result[i][j][0],result[i][j][1],1)
        fit_x = np.array([min(result[i][j][0]),max(result[i][j][0])])
        fit_y = fit_l[0]*fit_x + fit_l[1]
        plt.scatter(result[i][j][0],result[i][j][1],s=20, label=ALGO_LABEL[j])
        plt.plot(fit_x,fit_y)
    plt.legend()
    plt.xlabel("mean")
    plt.ylabel(i)
    plt.show()

    plt.hist(result[i][0][0],bins=10,alpha=0.5, histtype="step", label="HEFT")
    plt.hist(result[i][1][0],bins=10,alpha=0.5, histtype="step", label="CPOP")
    plt.hist(result[i][2][0],bins=10,alpha=0.5, histtype="step", label="PEFT")
    plt.hist(result[i][3][0],bins=10,alpha=0.5, histtype="step", label="DHS")
    plt.legend()
    plt.xlabel("mean")
    plt.show()

    plt.hist(result[i][0][1],bins=10,alpha=0.5, histtype="step", label="HEFT")
    plt.hist(result[i][1][1],bins=10,alpha=0.5, histtype="step", label="CPOP")
    plt.hist(result[i][2][1],bins=10,alpha=0.5, histtype="step", label="PEFT")
    plt.hist(result[i][3][1],bins=10,alpha=0.5, histtype="step", label="DHS")
    plt.legend()
    plt.xlabel("time")
    plt.show()

    plt.scatter(result[i][0][0], result[i][0][1], label="HEFT")
    plt.scatter(result[i][1][0], result[i][1][1], label="CPOP")
    plt.scatter(result[i][2][0], result[i][2][1], label="PEFT")
    plt.scatter(result[i][3][0], result[i][3][1], label="DHS")
    plt.legend()
    plt.xlabel("mean")
    plt.show()
"""