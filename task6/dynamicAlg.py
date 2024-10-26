def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]
    item_list = list(items.items())

    for item, info in item_list:
        for b in range(budget, info['cost'] - 1, -1):
            if dp[b - info['cost']] + info['calories'] > dp[b]:
                dp[b] = dp[b - info['cost']] + info['calories']
                selected_items[b] = selected_items[b - info['cost']] + [item]

    total_cost = sum(items[item]['cost'] for item in selected_items[budget])
    return selected_items[budget], dp[budget], total_cost


# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print(dynamic_programming(items, budget))