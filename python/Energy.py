#インポート

import numpy as np

#初期設定

#地上を0mとする
m = 25 #kg　固定
g = 9.81 #m/s^2　固定

#関数

#位置エネルギー
def Potential_Energy(m, h):
    Potential_Energy = m * g * h
    return Potential_Energy

#運動エネルギー
def Kinetic_Energy(m, v):
    Kinetic_Energy = 1/2 * m * (v ** 2)
    return Kinetic_Energy


#のぼり（地上からの距離(Middle_H = 70 ~ 90[m])からブレーキをかけた時）
print("のぼり（地上からの距離(Middle_H = 70 ~ 90[m])からブレーキをかけた時）")

for i in np.arange(0, 3.1, 0.1):
    v = 5 #初期化
    v += i
    print("")
    print("途中のv", v, "[m/s]")

    for j in np.arange(0, 21, 1):
        Middle_H = 70 #初期化
        Middle_H += j

        Final_Potential_Energy = Potential_Energy(m, 100) #最高点は100mであると_仮定_
        Final_Kinetic_Energy = Kinetic_Energy(m, 0)

        Middle_Potential_Energy = Potential_Energy(m, Middle_H) #地上からの距離Middle_H
        Middle_Kinetic_Energy = Kinetic_Energy(m, v) #5~8m/s

        #摩擦力がした仕事 W = ΔE = E2 - E1 = (最高点の位置エネルギー + 最高点の運動エネルギー(0))　- (途中の位置エネルギー + 途中の運動エネルギー)
        #摩擦エネルギー Friction_Energy (-μ * 挟む力(F) * x)
        ###print(Final_Kinetic_Energy, Final_Potential_Energy, Middle_Kinetic_Energy, Middle_Potential_Energy)
        Friction_Energy = (Final_Potential_Energy + Final_Kinetic_Energy) - (Middle_Potential_Energy + Middle_Kinetic_Energy)

        #この摩擦エネルギーに差分の距離(最高点 - 途中の距離[m])を割ると摩擦力が出てくる
        #摩擦力 Friction
        Friction = Friction_Energy / (100 - Middle_H)


        print("v =", v, "Middle_H =", Middle_H)
        print("ブレーキをかけてから到達までに必要なエネルギー")
        print("摩擦エネルギー", Friction_Energy, "摩擦力", Friction)


#おり（頂上からの距離(Middle_H = 10 ~ 30[m])からブレーキをかけた時）
print("おり（頂上からの距離(Middle_H = 10 ~ 30[m])からブレーキをかけた時）")

for i in np.arange(0, 8.1, 0.1):
    v = 5 #初期化
    v += i
    print("")
    print("途中のv", v, "[m/s]")

    for j in np.arange(0, 21, 1):
        Middle_H = 10 #初期化
        Middle_H += j

        Final_Potential_Energy = Potential_Energy(m, 0) #最下点0m
        Final_Kinetic_Energy = Kinetic_Energy(m, 0) #ゼロに抑える

        Middle_Potential_Energy = Potential_Energy(m, Middle_H) #地上からの距離Middle_H
        Middle_Kinetic_Energy = Kinetic_Energy(m, v) #5~8m/s

        Friction_Energy = (Final_Potential_Energy + Final_Kinetic_Energy) - (Middle_Potential_Energy + Middle_Kinetic_Energy)

        #この摩擦エネルギーに地上からの距離(最高点 - 途中の距離[m])を割ると摩擦力が出てくる
        #摩擦力 Friction
        Friction = Friction_Energy / Middle_H


        print("v =", v, "[m/s] Middle_H =", Middle_H, "[m]")
        print("ブレーキをかけてから到達までに必要なエネルギー")
        print("摩擦エネルギー", Friction_Energy, "摩擦力", Friction * 0.102, "[kgf]")


######### 結論(条件：挟む力(F) * μ > mgが成り立つ場合) ##########


#### のぼり ####

#摩擦力は普段負で表されるが、上の計算ではすべて正の値を示す
#つまりのぼりは重力とモータ制御だけで静止する
#ブレーキを使用しない場合の制動距離　V0^2 / 2g


#### おり ####

#摩擦力最低

#v = 5.0 Middle_H = 10
#ブレーキをかけてから到達までに必要なエネルギー
#摩擦エネルギー -2765.0 摩擦力 -276.5
#v = 5.0 Middle_H = 30
#ブレーキをかけてから到達までに必要なエネルギー
#摩擦エネルギー -7670.0 摩擦力 -255.66666666666666

#摩擦力最高

#v = 8.0 Middle_H = 10
#ブレーキをかけてから到達までに必要なエネルギー
#摩擦エネルギー -3252.5 摩擦力 -325.25
#v = 8.0 Middle_H = 30
#ブレーキをかけてから到達までに必要なエネルギー
#摩擦エネルギー -8157.5 摩擦力 -271.9166666666667


##### まとめ #####
#のぼりは物理ブレーキ使用しない
#おりは5.0[m/s]で地上10mの位置から丁度地上で止めるには摩擦力277[N]以上必要で、地上30mから止める場合は256[N]以上必要
#8.0[m/s]で地上10mの位置から丁度地上で止めるには摩擦力325[N]以上必要で、地上30mから止める場合は272[N]以上必要
#これは一部抜粋のデータなので、細かく見たい場合はPythonで実行してください
