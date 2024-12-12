import random

# 初始化节点和距离
distances = {}

# 定义根节点
roots = ['root1', 'root2', 'root3', 'root4', 'root5']

# 每个根节点生成一个树
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

# 添加根节点到中心节点的距离
for root in roots:
    if root != 'root1':
        distances[(root, 'root1')] = random.randint(-10, 10)

# 定义DFS函数
def dfs(start_node, end_node, distances, visited_nodes):# 深度优先搜索 DFS 递归  visited_nodes 用于记录已经访问过的节点
    # 如果开始节点就是结束节点，那么距离就是0
    if start_node == end_node:
        return 0

    # 标记开始节点为已访问
    visited_nodes.add(start_node)

    # 遍历所有与开始节点相连的节点
    for nodes, distance in distances.items():
        if nodes[0] == start_node and nodes[1] not in visited_nodes:
            # 使用DFS递归搜索子节点
            child_distance = dfs(nodes[1], end_node, distances, visited_nodes)
            
            # 如果找到了路径，返回距离
            if child_distance is not None:
                return abs(distance) + child_distance

    # 如果没有找到路径，返回None
    return None

# 输出所有根节点与其子节点
for root in roots:
    child_nodes = [node[1] for node in distances if node[0] == root]
    print(f"{root} -> {child_nodes}")

# 输入一个子节点
random_child_node = input("请输入一个子节点: ")

# 找到该子节点到其父节点的距离
visited_nodes = set()
distance = dfs(random_child_node, 'root1', distances, visited_nodes)
if distance is not None:
    print(f"The distance from {random_child_node} to root1 is {distance}.")
else:
    print(f"There is no path from {random_child_node} to root1.")

# 计算根节点到中心节点的距离
center_node = 'root1'
root_to_center_distances = {}
for root in roots:
    if root != center_node:
        visited_nodes = set()
        distance = dfs(root, center_node, distances, visited_nodes)
        if distance is not None:
            root_to_center_distances[root] = distance

# 输出根节点到中心节点的距离
for root, distance in root_to_center_distances.items():
    print(f"The distance from {root} to {center_node} is {distance}.")