import numpy as np
import random
#目的関数
def obj_f(x):
    return(pow(x - 1, 2))
#最適な位置 
def p_gd (elements):
    return(sum(elements)/ len(elements))
#最適な粒子の位置
def p_id (elements):
    ans =[]
    for ele in elements:
        ans.append(obj_f(ele))
    index = np.argmin(ans)
    return (elements[index])
start_f = 1
#定数
c1 = 10
c2 = 0.1
esp = 0.005
num = 5

#step 1 各粒子の位置と速度をランダムに決定する
x = [random.uniform(-10, 10) for i in range(num)]
v = [random.uniform(-10, 10) for i in range(num)]
iteration = 1
while(1):
    print("iteration ", iteration)
    iteration += 1
    #step2　各粒子について適応度関数を評価する
    opt =[obj_f(i) for i in x]
        #Pbestを適切に設定するため
    if (start_f == 1):
        pbest = min(opt)
        pbest_index = np.argmin(opt)
        pbest_x = x[pbest_index]
        start_f = 0
    #step3・４　粒子の適応度関数を、Pbestと比較をし小さければ更新
    if (min(opt) < pbest):
        pbest = min(opt)
        pbest_index = np.argmin(opt)
        pbest_x = x[pbest_index]
    print("x: ", x)
    print("pbest: {0}, best_x:{1}".format(pbest, pbest_x))
    if abs(pbest) < esp:
        break
    #step6　量子の位置ベクトルと速度ベクトルを更新する
    pgd = p_gd(x)
    pid  = p_id (x)
    for i in range(len(x)):
        xid = x[i]
        vid = v[i]
        v[i] = vid + c1 * random.random() * (pid - xid) - c2 * random.random() * (pgd -xid)
        x[i] = v[i] + xid
    print("")

print("\n ans: {0}".format(pbest_x))
