import math
from sys import maxsize
from itertools import permutations


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

    s = 0
    min_path = solve_travelling_salesman_problem(graph, s, num_of_activities)

    print(round(min_path[0], 3))
    print(activities[0][0])

    for activity_index in min_path[1]:
        print(activities[activity_index][0])

    print(activities[0][0])


def solve_travelling_salesman_problem(graph, starting_node, no_of_activities):
    # Determine the all the nodes (except for the start node).
    nodes = []
    for i in range(no_of_activities):
        if i != starting_node:
            nodes.append(i)

    # Find minimum weight (Hamiltonian cycle).
    prev_min_path_weight = None
    curr_min_path_weight = maxsize
    min_path = ()
    iter_permutations = permutations(nodes)

    for i in iter_permutations:
        curr_path_weight = 0

        k = starting_node
        for j in i:
            curr_path_weight += graph[k][j]
            k = j
        curr_path_weight += graph[k][starting_node]

        # Update the minimum weight (with partial Hamiltonian path).
        curr_min_path_weight = min(curr_min_path_weight, curr_path_weight)

        if prev_min_path_weight is None:
            prev_min_path_weight = curr_min_path_weight
            min_path = i

        if curr_min_path_weight < prev_min_path_weight:
            prev_min_path_weight = curr_min_path_weight
            min_path = i

    return curr_min_path_weight, min_path


def get_distance(pos1, pos2):
    return math.sqrt(((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)) * 1000


if __name__ == '__main__':
    main()
