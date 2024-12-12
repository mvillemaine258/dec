import random

# 初始化节点和距离
distances = {}

# 定义根节点
roots = ['root1', 'root2', 'root3', 'root4', 'root5']

# 为每个根节点生成一个树
for idx, root in enumerate(roots):
    # 随机生成子节点数量，至少3个，最多5个
    num_child_nodes = random.randint(3, 5)
    
    # 生成树的其他节点和距离
    for i in range(1, num_child_nodes+1):
        start_node = root if i == 1 else root + '_son' + str(i-1)
        end_node = root + '_son' + str(i)
        distance = random.randint(-10, 10)  # 生成-10到10之间的随机数
        distances[(start_node, end_node)] = distance

    # 添加根节点之间的随机距离
    if idx < len(roots) - 1:
        distances[(root, roots[idx+1])] = random.randint(-10, 10)

# 输入一个子节点
random_child_node = input("请输入一个子节点: ")

# 找到该子节点到其父节点的距离
child_to_root_distance = 0
for nodes, distance in distances.items():
    if nodes[1] == random_child_node:
        child_to_root_distance += abs(distance)

# 找到根节点到中心根节点的距离
root_to_center_distance = 0
for idx, root in enumerate(roots):
    if idx < len(roots) - 1:
        root_to_center_distance += abs(distances[(root, roots[idx+1])])

# 输出子节点到根节点的距离和根节点到中心根节点的距离
print(f"子节点 {random_child_node} 到根节点的距离为 {child_to_root_distance}")
print(f"根节点到中心根节点的距离为 {root_to_center_distance}")
