import matplotlib.pyplot as plt

# 数据
x = [100000, 200000, 400000, 800000]  # x轴数据
y1 = [1, 1, 1, 1]  # 第一条折线的y轴数据
y2 = [0.5062, 0.5054, 0.5013, 0.5033]  # 第二条折线的y轴数据
y3 = [0.2589, 0.0008, 0.2514, 0.2516]  # 第san条折线的y轴数据
y4 = [0.1681, 0.1692, 0.1670, 0.1670]  # 第san条折线的y轴数据


# 创建折线图
plt.plot(x, y1, label='One Process', color='blue', marker='o')
plt.plot(x, y2, label='Two Processes', color='red', marker='s')
plt.plot(x, y3, label='Four Processes', color='black', marker='d')
plt.plot(x, y4, label='Six Processes', color='green', marker='d')

# 设置标题和轴标签
plt.title("Sp")
plt.xlabel("N")
plt.ylabel("Sp")

plt.xticks(x)

# 添加图例
plt.legend()

# 添加每个数据点的y坐标标签到y轴
y_ticks = [y1, y2, y3, y4]
plt.yticks([item for sublist in y_ticks for item in sublist], [f'{item:.6f}' for sublist in y_ticks for item in sublist])

# 保存为PNG图片
plt.savefig('C:/Users/LMY/Desktop/012.png')

# 显示图形
plt.show()

# 绘制柱状图
# Path: graph.py
import matplotlib.pyplot as plt

# 数据
x = [100000, 200000, 400000, 800000]  # x轴数据
y1 = [1, 1, 1, 1]  # 第一条折线的y轴数据
y2 = [0.5062, 0.5054, 0.5013, 0.5033]  # 第二条折线的y轴数据
y3 = [0.2589, 0.0008, 0.2514, 0.2516]  # 第san条折线的y轴数据
y4 = [0.1681, 0.1692, 0.1670, 0.1670]  # 第san条折线的y轴数据


# 创建柱状图
plt.bar(x, y1, label='One Process', color='blue')
plt.bar(x, y2, label='Two Processes', color='red')
plt.bar(x, y3, label='Four Processes', color='black')
plt.bar(x, y4, label='Six Processes', color='green')


# 设置标题和轴标签
plt.title("Sp")

plt.xlabel("N")

plt.ylabel("Sp")

plt.xticks(x)

# 添加图例
plt.legend()

# 添加每个数据点的y坐标标签到y轴
y_ticks = [y1, y2, y3, y4]
plt.yticks([item for sublist in y_ticks for item in sublist], [f'{item:.6f}' for sublist in y_ticks for item in sublist])

# 保存为PNG图片
plt.savefig('C:/Users/LMY/Desktop/012.png')

# 显示图形
plt.show()



