import math
from sys import maxsize
from itertools import permutations


search_space = []
paths = []


def main():
    # Get the raw input.
    num_of_activities = int(input())
    activities = []

    for _ in range(num_of_activities):
        activities.append(input().strip().split())

    print(activities)

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

    print(graph)

    visited_nodes = [False for i in range(num_of_activities)]
    visited_nodes[0] = True
    print(visited_nodes)

    solve_travelling_salesman_problem(graph, visited_nodes, 0, num_of_activities, 1, 0)

    print(search_space)
    print(round(min(search_space, key=lambda x: x[0]), 3))


def solve_travelling_salesman_problem(graph, visited_nodes, curr_pos, num_of_activities, count, cost):
    if (count == num_of_activities) and graph[curr_pos][0]:
        search_space.append((cost + graph[curr_pos][0], 42))
        return

    for i in range(num_of_activities):
        if (visited_nodes[i] is False) and graph[curr_pos][i]:
            visited_nodes[i] = True
            solve_travelling_salesman_problem(graph, visited_nodes, i, num_of_activities, count + 1, cost + graph[curr_pos][i])
            visited_nodes[i] = False


def get_distance(pos1, pos2):
    return round(math.sqrt(((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)) * 1000, 3)


if __name__ == '__main__':
    main()
