import math
from sys import maxsize
from itertools import permutations


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

    s = 0
    min_path = solve_travelling_salesman_problem(graph, s, num_of_activities)
    print(min_path)

    print(round(min_path[0], 3))

    print(activities[0][0])
    for activity_index in min_path[1]:
        print(activities[activity_index][0])

    print(activities[0][0])

def solve_travelling_salesman_problem(graph, s, no_of_activities):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(no_of_activities):
        if i != s:
            vertex.append(i)
    print(vertex)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    # list_permutations = list(next_permutation)
    # print(list_permutations)

    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path, i


def get_distance(pos1, pos2):
    return round(math.sqrt(((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)) * 1000, 3)


if __name__ == '__main__':
    main()
