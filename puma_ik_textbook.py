#  教材勘误， 有一部分文字资料和comment中说明了。
#  但视频中仍有答案正确过程不正确的公式。
#  因此本代码为机械手臂逆运动学pieper解的python实现，可以对照课程中演示的过程，加深对逆运动学运算的理解。
from roboticstoolbox import RevoluteDH, DHRobot, DHLink, SerialLink
from sympy import symbols, solve, Eq, simplify, expand, factor, atan2
import math

import numpy as np

alpha0 = 0
a0 = 0
d1 = 0

alpha1 = -np.pi / 2
sa1 = np.sin(alpha1)
ca1 = np.cos(alpha1)
a1 = -30
d2 = 0

alpha2 = 0
sa2 = np.sin(alpha2)
ca2 = np.cos(alpha2)
a2 = 340
d3 = 0

alpha3 = -np.pi / 2
sa3 = np.sin(alpha3)
ca3 = np.cos(alpha3)
a3 = -40
d4 = 338

alpha4 = np.pi / 2
sa4 = np.sin(alpha4)
ca4 = np.cos(alpha4)
a4 = 0
d5 = 0

alpha5 = -np.pi / 2
sa5 = np.sin(alpha5)
ca5 = np.cos(alpha5)
a5 = 0
d6 = 0

w0T = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 373], [0, 0, 0, 1]])
sixcT = np.array([[0, 0, 1, 0], [0, -1, 0, 0], [1, 0, 0, 206], [0, 0, 0, 1]])
cos35 = np.cos(math.radians(35))
sin35 = np.sin(math.radians(35))
TDC = np.array([[cos35, -sin35, 0, -280], [sin35, cos35, 0, 250], [0, 0, 1, 62.5], [0, 0, 0, 1]])
wcT = np.array([[1, 0, 0, 830], [0, 1, 0, 20], [0, 0, 1, 330], [0, 0, 0, 1]]) @ TDC

zero_six_T = np.linalg.inv(w0T) @ wcT @ np.linalg.inv(sixcT)
print(zero_six_T)

theta1 = math.radians(21.8)
theta2 = math.radians(-52.2)
theta3 = math.radians(2.5)

L1 = DHLink(alpha=alpha0, a=a0, d=d1, qlim=[-np.pi / 2, np.pi / 2], mdh=True)  # 第1个关节
L2 = DHLink(alpha=alpha1, a=a1, d=d2, qlim=[-np.pi, np.pi], mdh=True)  # 第2个关节
L3 = DHLink(alpha=alpha2, a=a2, d=d3, qlim=[-np.pi, np.pi], mdh=True)  # 第3个关节
# rotation3 = DHLink(alpha=alpha3, a=a3, d=d4, qlim=[-np.pi, np.pi], mdh=True)
rotation3 = DHLink(alpha=alpha3, a=0, d=0, qlim=[-np.pi, np.pi], mdh=True)
robot0_3 = SerialLink([L1, L2, L3, rotation3], name="03R")
q = [theta1, theta2, theta3, 0]
T03_modify = robot0_3.fkine(q)
# print("比较旋转前后的Transformation matrix")
T03 = SerialLink([L1, L2, L3], name="03R_pure").fkine([theta1, theta2, theta3])
print(f"T03_modify: {T03_modify}")
print(f"T03: {T03}")
R36_modify = np.linalg.inv(T03_modify) @ zero_six_T
print(f"R36_modify: {R36_modify}")
R36 = np.linalg.inv(T03) @ zero_six_T
print(f"R36: {R36}")

theta5 = atan2(math.sqrt(R36_modify[2, 0] ** 2 + R36_modify[2, 1] ** 2), R36_modify[2, 2])
theta5 = float(theta5)
theta4 = atan2(R36_modify[1, 2] / np.sin(theta5), R36_modify[0, 2] / np.sin(theta5))
theta6 = atan2(R36_modify[2, 1] / np.sin(theta5), -R36_modify[2, 0] / np.sin(theta5))


print(f"theta456: {math.degrees(theta4) }, {math.degrees(theta5)}, {math.degrees(theta6) }")