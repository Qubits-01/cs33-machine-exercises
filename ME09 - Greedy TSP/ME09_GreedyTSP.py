import math
from sys import maxsize


def main():
    # Get the raw input.
    num_of_activities = int(input())
    activities = []

    for _ in range(num_of_activities):
        activities.append(input().strip().split())

    # Build the complete edge-weighted graph.
    graph = []
    for i in range(num_of_activities):
        temp_row = []
        for j in range(num_of_activities):
            if i == j:
                temp_row.append(0)
                continue

            pos1 = (float(activities[i][2]), float(activities[i][3]))
            pos2 = (float(activities[j][2]), float(activities[j][3]))
            temp_row.append(get_distance(pos1, pos2))

        graph.append(temp_row)

    path, total_cost = solve_travelling_salesman_problem(graph, 0)

    print(round(total_cost, 3))
    for activity_index in path:
        print(activities[activity_index][0])

    print(activities[0][0])


def solve_travelling_salesman_problem(graph, starting_node):
    mst = build_mst(graph)  # Build the MST.

    # Rearrange the subtrees accordingly.
    for node in mst:
        node[1].sort(key=lambda x: x[1])

    # Do a DFS to the MST.
    path = []
    dfs(mst, starting_node, path)

    # Get the total cost of the path.
    total_cost = get_total_cost(graph, path)

    return path, total_cost


def build_mst(graph):
    no_of_nodes = len(graph)
    no_edge = 0
    selected_nodes = [False for _ in range(no_of_nodes)]
    selected_nodes[0] = True
    mst = [[False, []] for _ in range(no_of_nodes)]

    while no_edge < no_of_nodes - 1:
        minimum = maxsize
        x = 0
        y = 0

        for i in range(no_of_nodes):
            if selected_nodes[i]:
                for j in range(no_of_nodes):
                    if (not selected_nodes[j]) and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        mst[x][1].append((y, graph[x][y]))
        selected_nodes[y] = True
        no_edge += 1

    return mst


def dfs(tree, curr_node, path):
    if tree[curr_node][0] is not True:
        path.append(curr_node)
        tree[curr_node][0] = True

        for adjacent_node in tree[curr_node][1]:
            dfs(tree, adjacent_node[0], path)


def get_total_cost(graph, path):
    total_cost = 0
    for node in range(len(path) - 1):
        temp_initial = path[node]
        temp_final = path[node + 1]
        total_cost += graph[temp_initial][temp_final]

    # Add the cost from the last node of the path to the starting node.
    temp_initial = path[-1]
    temp_final = path[0]
    total_cost += graph[temp_initial][temp_final]

    return total_cost


def get_distance(pos1, pos2):
    return math.sqrt(((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)) * 1000


if __name__ == '__main__':
    main()
