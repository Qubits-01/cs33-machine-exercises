def main():
    weight_capacity = int(input())
    no_of_items = int(input())
    items = []

    for i in range(no_of_items):
        temp_item = input().strip().split()
        items.append((int(temp_item[0]), int(temp_item[1]), int(temp_item[2])))

    max_value, included_items = solve_knapsack_problem(weight_capacity, items)
    included_items.sort(reverse=True)

    print(max_value)
    for item_key in included_items:
        print(item_key)


# Using the Dynamic Programming Paradigm.
def solve_knapsack_problem(weight_capacity, items):
    dp = [[0 for w in range(weight_capacity + 1)] for i in range(len(items) + 1)]

    # Build the dp table (from bottom-up).
    for i in range(len(items) + 1):
        for w in range(weight_capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i - 1][1] <= w:
                dp[i][w] = max(items[i - 1][2] + dp[i - 1][w - items[i - 1][1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # The maximum total value for the knapsack.
    max_value = dp[len(items)][weight_capacity]

    # Determine the item/s that were included in the knapsack.
    temp_weight = weight_capacity
    temp_max_value = max_value
    included_items = []

    for i in range(len(items), 0, -1):
        if temp_max_value <= 0:
            break
        if temp_max_value == dp[i - 1][temp_weight]:
            continue
        else:
            included_items.append(items[i - 1][0])

            temp_max_value = temp_max_value - items[i - 1][2]
            temp_weight = temp_weight - items[i - 1][1]

    return max_value, included_items


if __name__ == '__main__':
    main()
