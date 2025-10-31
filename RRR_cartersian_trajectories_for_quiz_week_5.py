import numpy as np

deltat1 = 2
deltat2 = 2
deltat3 = 5

x1 = -4
x2 = -5
x3 = 2
x4 = 2

y1 = 0
y2 = 5
y3 = 3
y4 = -3

# theta1 = np.radians(120)
# theta2 = np.radians(45)
# theta3 = np.radians(30)
theta1 = 120
theta2 = 45
theta3 = 30
theta4 = 0



T_12_12 = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, deltat1, deltat1 ** 2, deltat1 ** 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, deltat2, deltat2 ** 2, deltat2 ** 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, deltat3, deltat3 ** 2, deltat3 ** 3],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2 * deltat3, 3 * deltat3 ** 2],
    [0, 1, 2 * deltat1, 3 * deltat1 ** 2, 0, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 6 * deltat1, 0, 0, -2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 2 * deltat2, 3 * deltat2 ** 2, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 6 * deltat2, 0, 0, -2, 0],
])

print(np.shape(T_12_12))

x_y_theta = np.array([
    [x1, y1, theta1],
    [x2, y2, theta2],
    [x2, y2, theta2],
    [x3, y3, theta3],
    [x3, y3, theta3],
    [x4, y4, theta4],
    [0, 0, 0, ],
    [0, 0, 0, ],
    [0, 0, 0, ],
    [0, 0, 0, ],
    [0, 0, 0, ],
    [0, 0, 0, ],
])

A12_3 = np.linalg.inv(T_12_12) @ x_y_theta
print(A12_3)

# A12_3[:, 2] = np.degrees(A12_3[:, 2])

# print(A12_3)

#  计算joint space 下的轨迹规划
l1 = 5
l2 = 3
theta_11 = np.pi - np.arccos(4. / 5)
theta_12 = np.pi - np.arccos(3. / 5)
theta_13 = -5 * np.pi / 6

theta_21 = np.pi * 3 / 4 - np.arccos((25 + 50 - 9) / (2 * 5 * np.sqrt(50)))
theta_22 = np.pi - np.arccos((9 + 25 - 50) / 30)
theta_23 = - (np.pi / 2 + np.arccos((9 + 50 - 25) / (6 * np.sqrt(50))))

# theta_31 = np.arccos(2 / np.sqrt(13)) + np.arccos((25 + 13 - 9) / (10 * np.sqrt(13)))
theta_31 = np.arccos(2 / np.sqrt(13)) - np.arccos((25 + 13 - 9) / (10 * np.sqrt(13)))
# theta_32 = - (np.pi - np.arccos((9 + 25 - 13) / 30))
theta_32 = np.pi - np.arccos((9 + 25 - 13) / 30)
# theta_33 = np.arccos((13 + 9 - 25) / (6 * np.sqrt(13))) - np.arccos(2 / np.sqrt(13)) + np.pi / 6
theta_33 = - (np.arccos((13 + 9 - 25) / (6 * np.sqrt(13))) + np.arccos(2 / np.sqrt(13)) - np.pi / 6)

# theta_41 = - (np.arccos(2 / np.sqrt(13)) - np.arccos((25 + 13 - 9) / (10 * np.sqrt(13))))
theta_41 = - (np.arccos(2 / np.sqrt(13)) + np.arccos((25 + 13 - 9) / (10 * np.sqrt(13))))
# theta_42 = - (np.pi - np.arccos((9 + 25 - 13) / 30))
theta_42 = np.pi - np.arccos((9 + 25 - 13) / 30)
# theta_43 = np.arccos((9 + 13 - 25) / (6 * np.sqrt(13))) + np.arccos(2 / np.sqrt(13))
theta_43 = - (np.arccos((9 + 13 - 25) / (6 * np.sqrt(13))) - np.arccos(2 / np.sqrt(13)))


theta1_2_3 = np.array([
    [theta_11, theta_12, theta_13],
    [theta_21, theta_22, theta_23],
    [theta_21, theta_22, theta_23],
    [theta_31, theta_32, theta_33],
    [theta_31, theta_32, theta_33],
    [theta_41, theta_42, theta_43],
    [0, 0, 0, ],
    [0, 0, 0, ],
    [0, 0, 0, ],
    [0, 0, 0, ],
    [0, 0, 0, ],
    [0, 0, 0, ],
])

A12_3_joint = np.linalg.inv(T_12_12) @ theta1_2_3
print("\n"*3)
print(A12_3_joint)