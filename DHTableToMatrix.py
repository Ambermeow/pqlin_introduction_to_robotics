import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import RevoluteDH, DHRobot, DHLink, SerialLink

# 输入您的DH参数表
# 格式: [[a1, alpha1, d1, theta1], [a2, alpha2, d2, theta2], ...]
dh_table = [
    [-np.pi/2, 0, 0, 0]
]

# 输入关节角度（弧度）
joint_angles = [-np.pi/4.5]
# joint_angles = [np.pi/2]

L1 = DHLink(alpha=0, a=0, d=0, qlim=[-np.pi, np.pi],mdh=True)         # 第1个关节
L2 = DHLink(alpha=-np.pi/2, a=0, d=220, qlim=[-np.pi, np.pi], mdh=True)  # 第2个关节
L3 = DHLink(alpha=0, a=430, d=-90, qlim=[-np.pi, np.pi], mdh=True)  # 第3个关节
L4 = DHLink(alpha=-np.pi/2, a=0, d=430, qlim=[-np.pi, np.pi], mdh=True)  # 第4个关节
L5 = DHLink(alpha=np.pi/2, a=0, d=0, qlim=[-np.pi, np.pi], mdh=True)  # 第5个关节
L6 = DHLink(alpha=-np.pi/2, a=0, d=0, qlim=[-np.pi, np.pi], mdh=True)  # 第6个关节

robot0_6 = SerialLink([L1, L2, L3, L4, L5, L6], name="6R")
robot0_4 = SerialLink([L1, L2, L3, L4], name="4R")

q = [np.radians(15), np.radians(-40), np.radians(-50), np.radians(30), np.radians(70), np.radians(25)]
# q = q[:4]
# T1_2 = L2.A(q[1])   # 第2个连杆的 A 矩阵
# print("T^1_2 =\n", T1_2)

T0_4 = robot0_4.fkine(q[:4])
print("T^0_4 = \n", T0_4)
T0_4 = T0_4.A
p4_origin = np.array([0, 0, 0, 1])

# 把 p4 原点变换到 frame0
p4_in_p0 = T0_4 @ p4_origin

print("p4 在 p0 下的齐次坐标：", p4_in_p0)        # [x, y, z, 1]
print("p4 在 p0 下的位置（x,y,z）：", p4_in_p0[:3])
# 等价地，直接取 T0_4 的平移项：
print("等价（T0_4 的平移列）：", T0_4[:3, 3])

T0_6 = robot0_6.fkine(q)
print("T^0_6 =\n", T0_6)
# T0_6 = robot0_6.fkine(q).A
# print("T^0_6 =\n", T0_6)








# # 创建机器人
# links = [RevoluteDH(a=a_i, alpha=alpha_i, d=d_i) for alpha_i, a_i, d_i, theta_i in dh_table]
# robot = DHRobot(links)

# 计算变换矩阵（只需要相关关节的角度）
# T = robot.fkine(joint_angles[start_joint:end_joint], end=end_joint, start=start_joint)
# T = robot.fkine(joint_angles)
#
# print(T)
# print("位置:", T.t)
# print("旋转矩阵:\n", T.R)