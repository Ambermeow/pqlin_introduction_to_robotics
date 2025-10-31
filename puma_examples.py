import roboticstoolbox as rtb
import numpy as np
# from roboticstoolbox import DHLink


# 加载内置的PUMA560模型（使用标准DH参数）
puma560 = rtb.models.DH.Puma560()
# 查看DH参数
# print("PUMA560 DH参数表:")
# print(puma560.dh)
# print("\n" + "="*50 + "\n")

# 查看具体的 a_2, a_3, d_3, d_4 值
print("您关心的具体参数:")
print(f"a_2 (第2连杆长度): {puma560.links[1].a}")
print(f"a_3 (第3连杆长度): {puma560.links[2].a}")
print(f"d_3 (第3连杆偏移): {puma560.links[2].d}")
print(f"d_4 (第4连杆偏移): {puma560.links[3].d}")
print("\n" + "="*50 + "\n")

# # 定义一组关节角度（单位：弧度）
# # 例如： [肩部旋转, 肩部伸展, 肘部伸展, 手腕旋转, 手腕弯曲, 手腕旋转]
# q = np.array([0, np.pi/4, np.pi/4, 0, np.pi/8, 0])  # 示例角度
#
# # 计算正向运动学，得到基座到末端执行器的齐次变换矩阵
# T = puma560.fkine(q)
#
# # 打印变换矩阵
# print("基座到末端的变换矩阵 T:")
# print(T)
#
# # 如果你想提取具体的位置和欧拉角
# position = T.t  # 位置向量 (x, y, z)
# print(f"\n末端执行器位置 (x, y, z): {position}")
#
# # 转换为旋转矩阵或欧拉角
# rot_matrix = T.R  # 3x3 旋转矩阵
# euler_angles = T.eul()  # 欧拉角 (默认ZYZ顺序，有时可能是其他顺序如‘xyz’)
# print(f"\n旋转矩阵 R: \n{rot_matrix}")
# print(f"\n欧拉角 (ZYZ): {euler_angles}")