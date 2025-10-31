from roboticstoolbox import RevoluteDH, DHRobot, DHLink, SerialLink
from sympy import symbols, solve, Eq, simplify, expand, factor, atan2
import math

import numpy as np
from spatialmath import SE3
from math import pi

#  算出T^0_6
w0T = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 373], [0, 0, 0, 1]])
wcT = np.array([[0.5, 0, -0.866, 330], [0, 1, 0, 472], [0.866, 0, 0.5, 740], [0, 0, 0, 1]])
sixcT = np.array([[0, 0, 1, 0], [0, -1, 0, 0], [1, 0, 0, 206], [0, 0, 0, 1]])

zero_six_T = np.linalg.inv(w0T) @ wcT @ np.linalg.inv(sixcT)
print(zero_six_T)

(x, y, z) = (zero_six_T[0:3, 3])
print(x, y, z)

r = x ** 2 + y ** 2 + z ** 2
print(f"r = {r}")
print(f"z = {z}")

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

u3 = symbols('u3')

c3 = (1 - u3 ** 2) / (1 + u3 ** 2)
s3 = 2. * u3 / (1 + u3 ** 2)

f1 = a3 * c3 + d4 * sa3 * s3 + a2
f2 = a3 * ca2 * s3 - d4 * sa3 * ca2 * c3 - d4 * sa2 * ca3 - d3 * sa2
f3 = a3 * sa2 * s3 - d4 * sa3 * sa2 * c3 + d4 * ca2 * ca3 + d3 * ca2

k1 = f1
k2 = -f2
k3 = f1 ** 2 + f2 ** 2 + f3 ** 2 + a1 ** 2 + d2 ** 2 + 2 * d2 * f3
k4 = f3 * ca1 + d2 * ca1
print(f"{k1}\n{k2}\n{k3}\n{k4}\n")

equation = Eq((r - k3) ** 2 / (4 * a1 ** 2) + (z - k4) ** 2 / sa1 ** 2 - k1 ** 2 - k2 ** 2, 0)
solutions = solve(equation, u3)
solutions = [sol for sol in solutions if sol.is_real]
print(f"方程 {equation} 的解: ")
print(f"{solutions}")

u3_list = solutions
# for solution in solutions:
#     # print(math.degrees(atan2(1.,1.)))
#     theta3 = atan2(solution, 1) * 2
#     print(f"theta3: {theta3}")
#     print(math.degrees(theta3))
#     theta3 = atan2(-solution, -1) * 2
#     print(math.degrees(theta3))
#
#  手算一半版
# ff1 = -40 * c3 - 338 * s3 + 340
# ff2 = -40 * s3 + 338 * c3
# ff3 = 0
# kk1 = ff1
# kk2 = -ff2
# kk3 = kk1 ** 2 + kk2 ** 2 + 900
# print(f"{kk1}\n{kk2}\n{kk3}\n")
#
# simplified_k1 = simplify(k1 - kk1)
# simplified_k2 = simplify(k2 - kk2)
# simplified_k3 = simplify(k3 - kk3)
#
# print(f"{simplify(k1)}")
# print(f"{simplify(kk1)}")
#
# print(f"k1 和 kk1 等价: {simplified_k1 == 0}")
# print(f"k2 和 kk2 等价: {simplified_k2 == 0}")
# print(f"k3 和 kk3 等价: {simplified_k3 == 0}")
# print(f"simplified_k3 为：{simplify(k3)}")

# formula2 = (r - kk3) ** 2 / 3600 + z ** 2 - kk1 ** 2 - kk2 ** 2
# formula2 = simplify(formula2)
# formula1 = (r - k3) ** 2 / (4 * a1 ** 2) + (z - k4) ** 2 / sa1 ** 2 - k1 ** 2 - k2 ** 2
# formula1 = simplify(formula1)
#
# print(f"formula1: {formula1}")
# print(f"formula2: {formula2}")
# diff = simplify(formula1 - formula2)
# print(f"formula1  和 formula2 等价: {diff == 0}")

# equation2 = Eq((r - kk3) ** 2 / 3600 + z ** 2 - kk1 ** 2 - kk2 ** 2, 0)
# solutions2 = solve(equation2, u3)
# print(f"方程 {equation2} 的解: ")
# print(f"{solutions2}")

# u3_list = []
# for solution in solutions:
#     # print(math.degrees(atan2(1.,1.)))
#     theta3 = atan2(solution2, 1) * 2
#     print(math.degrees(theta3))
#     if (math.degrees(theta3) < 180 and math.degrees(theta3) > -180):
#         u3_list.append(solution2)
#     theta3 = atan2(solution2 * (-1.), -1) * 2
#     print(math.degrees(theta3))
#     if (math.degrees(theta3) < 180 and math.degrees(theta3) > -180):
#         u3_list.append(solution2)
#
#  计算theta2
u23_list = []
u2 = symbols('u2')
c2 = (1 - u2 ** 2) / (1 + u2 ** 2)
s2 = 2 * u2 / (1 + u2 ** 2)
for u3_res in u3_list:
    c3_res = c3.subs(u3, u3_res)
    s3_res = s3.subs(u3, u3_res)
    k1_res = k1.subs(u3, u3_res)
    k2_res = k2.subs(u3, u3_res)
    k3_res = k3.subs(u3, u3_res)
    print(f"k1,k2,k3:{k1_res}, {k2_res}, {k3_res}")

    equation_theta2 = Eq((k1_res * c2 + k2_res * s2) * 2 * a1 + k3_res - r, 0)
    solutions_theta2 = solve(equation_theta2, u2)
    for u2_res in solutions_theta2:
        if u2_res.is_real:
            u23_list.append((u2_res, u3_res))

print(f"u2_list: {u23_list}")

theta123_list = []
u123_list = []
print("_____________" * 20)
for u2_res, u3_res in u23_list:
    f1_res = f1.subs(u3, u3_res)
    f2_res = f2.subs(u3, u3_res)
    f3_res = f3.subs(u3, u3_res)
    # print(f"k1,k2,k3:{k1_res}, {k2_res}, {k3_res}")

    c2_res = c2.subs(u2, u2_res)
    s2_res = s2.subs(u2, u2_res)

    g1 = c2_res * f1_res - s2_res * f2_res + a1
    g2 = s2_res * ca1 * f1_res + c2_res * ca1 * f2_res - sa1 * f3_res - d2 * sa1

    u1 = symbols('u1')
    c1 = (1 - u1 ** 2) / (1 + u1 ** 2)
    s1 = 2 * u1 / (1 + u1 ** 2)

    equation_theta1 = Eq(c1 * g1 - s1 * g2 - x, 0)
    solutions_theta1 = solve(equation_theta1, u1)
    print(f"solutions_theta1: {solutions_theta1}")
    for u1_res in solutions_theta1:
        if u1_res.is_real:
            u123_list.append((u1_res, u2_res, u3_res))

#  按照约定的degree范围筛选theta123 的值
theta123_list = []
for u1_res, u2_res, u3_res in u123_list:
    degree_theta1_list = [math.degrees(atan2(u1_res, 1) * 2), math.degrees(atan2(-u1_res, -1) * 2)]
    degree_theta2_list = [math.degrees(atan2(u2_res, 1) * 2), math.degrees(atan2(-u2_res, -1) * 2)]
    degree_theta3_list = [math.degrees(atan2(u3_res, 1) * 2), math.degrees(atan2(-u3_res, -1) * 2)]

    for theta1 in degree_theta1_list:
        for theta2 in degree_theta2_list:
            for theta3 in degree_theta3_list:
                if (theta3 > -180) and theta3 < 180:
                    if (theta2 > -180) and theta2 < 180:
                        if (theta1 > -90) and theta1 < 90:
                            theta123_list.append((theta1, theta2, theta3))
theta123_list = list(set(theta123_list))
print(theta123_list)
print(len(theta123_list))

L1 = DHLink(alpha=alpha0, a=a0, d=d1, qlim=[-np.pi / 2, np.pi / 2], mdh=True)  # 第1个关节
L2 = DHLink(alpha=alpha1, a=a1, d=d2, qlim=[-np.pi, np.pi], mdh=True)  # 第2个关节
L3 = DHLink(alpha=alpha2, a=a2, d=d3, qlim=[-np.pi, np.pi], mdh=True)  # 第3个关节
rotation3 = DHLink(alpha=alpha3, a=a3, d=d4, qlim=[-np.pi, np.pi], mdh=True)
# rotation3 = DHLink(alpha=alpha3, a=0, d=0, qlim=[-np.pi, np.pi], mdh=True)
robot0_3 = SerialLink([L1, L2, L3, rotation3], name="03R")

# theta123_list = [ll for ll in theta123_list if abs(ll[0]-64)<1]
for theta1, theta2, theta3 in theta123_list:
    theta1 = math.radians(theta1)
    theta2 = math.radians(theta2)
    theta3 = math.radians(theta3)
    q = [theta1, theta2, theta3, 0]
    T03_modify = robot0_3.fkine(q)
    # print("比较旋转前后的Transformation matrix")
    T03 = SerialLink([L1, L2, L3], name="03R_pure").fkine([theta1, theta2, theta3])
    R36_modify = np.linalg.inv(T03_modify) @ zero_six_T
    R36 = np.linalg.inv(T03) @ zero_six_T

    # print("比较旋转前后的T36")
    # print(f"R36_modify: {R36_modify}")
    # print(f"R36: {R36}")
    # print(f"R_31:{R36[2, 0]}")

    theta5 = atan2(math.sqrt(R36_modify[2, 0] ** 2 + R36_modify[2, 1] ** 2), R36_modify[2, 2])
    theta5 = float(theta5)
    theta4 = atan2(R36_modify[1, 2] / np.sin(theta5), R36_modify[0, 2] / np.sin(theta5))
    theta6 = atan2(R36_modify[2, 1] / np.sin(theta5), -R36_modify[2, 0] / np.sin(theta5))

    L4 = DHLink(alpha=alpha3, a=a3, d=d4, qlim=[-np.pi, np.pi], mdh=True)  # 第4个关节
    L5 = DHLink(alpha=alpha4, a=a4, d=d5, qlim=[-np.pi, np.pi], mdh=True)  # 第5个关节
    L6 = DHLink(alpha=alpha5, a=a5, d=d6, qlim=[-np.pi, np.pi], mdh=True)  # 第6个关节
    robot_PUMA = SerialLink([L1, L2, L3, L4, L5, L6], name="PUMA")
    q06 = [theta1, theta2, theta3, theta4+np.pi, theta5, theta6+np.pi]
    T06 = robot_PUMA.fkine(q06)

    T06_A = T06.A
    tolerance = 1e-6

    aa = zero_six_T[0:3, 3]
    bb= T06_A[0:3, 3]
    aa = [float(aaa) for aaa in aa]
    bb = [float(bbb) for bbb in bb]

    #  Here you can tell why the other theta123 are not the correct answer.
    are_equal = np.allclose(aa, bb, atol=tolerance)

    if are_equal:
        print(f"运动学和逆运动学的T06相等")

        print(f"zero_six_T: {zero_six_T}")
        print(f"T06: {T06}")
        print(f"theta123: {theta1},{theta2},{theta3}")
        print(f"theta456: {math.degrees(theta4)}, {-math.degrees(theta5)}, {math.degrees(theta6)}")




