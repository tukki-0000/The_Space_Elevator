###直径80~130[mm]のタイヤを使用することを想定し、速度5000~10000mm/sを実現するモータに必要な回転数を求める###
###[mm]で統一

#インポート

import numpy as np
import math

#初期設定

Distance = 100000 #[mm]

######## 関数群 ########

#円周　Circumference
def Circumference(Diameter):
    Circumference = Diameter * math.pi
    return Circumference

#100m到達できる回転数 Complete_Rotation_Speed
def Complete_Rotation_Speed(Circumference):
    Complete_Rotation_Speed = 100000 / Circumference
    return Complete_Rotation_Speed

#一回転にかかる時間
def One_Rotation_Speed(END_TIME, Complete_Rotation_Speed):
    One_Rotation_Speed = END_TIME / Complete_Rotation_Speed
    return One_Rotation_Speed

#SPM
def SPM(One_Rotation_Speed):
    SPM = 1 / One_Rotation_Speed
    return SPM

#RPM
def RPM(SPM):
    RPM = SPM * 60
    return RPM

#トルク
def Torque(Radius):
    Torque = 25 * 9.81 * Radius / 1000 #ここだけmになおす
    return Torque

#動力
def Power(Radius, RPM):
    Power = (25 * 9.81 * Radius * RPM) / 9549
    return Power

########## MAIN ##########

for Diameter in np.arange(80, 131, 1):
    Circumference1 = Circumference(Diameter)
    Complete_Rotation_Speed1 = Complete_Rotation_Speed(Circumference1)
    Radius = Diameter / 2
    Torque1 = Torque(Radius)
    print("ーーータイヤ直径", Diameter, "[mm] 必要トルク", Torque1, "[N・m]の場合ーーー")

    for V in np.arange(5000, 10001, 100):
        END_TIME = Distance / V
        One_Rotation_Speed1 = One_Rotation_Speed(END_TIME, Complete_Rotation_Speed1)
        SPM1 = SPM(One_Rotation_Speed1)
        RPM1 = RPM(SPM1)
        print("V", V, "[mm/s]", "SPM", SPM1, "[回転/秒]", "RPM", RPM1, "[回転/分]")
        P = Power(Radius, RPM1)
        print("必要な動力", P, "[W]")


 ################ 結論 ##################

 #車輪直径　80mm 必要トルク 9.81 N・m
 #車輪直径　130mm 必要トルク 15.94 N・m
 #車輪４個、6個？　ー　タイヤは構造による
 #モータ２個、４個？　ー　モータはトルクを考えて2個でいい

 #不確定要素が多すぎる
 #改善　ー　タイヤとテザーを抑える力（挟む力）を機体重量のに倍以上にすることは可能なのか？（駆動輪を回す場合この限りでない）
 #     ー　静止摩擦係数、動摩擦係数がいくらになるか求める
 #　　　ー　トルクや摩擦力、動力の安全率を考える　（例：クレーンなどのワイヤロープ　6以上, エレベーターのワイヤーロープ　10以上）
